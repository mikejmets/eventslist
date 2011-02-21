from zope.interface import Interface
from zope import schema
from zope.formlib import form
from Products.Five.formlib import formbase
from Products.statusmessages.interfaces import IStatusMessage
from Acquisition import aq_inner
from Products.CMFPlone import PloneMessageFactory as _
from Products.eventslist.content.elevent import ELEvent
from Products.ATContentTypes.utils import dt2DT


class ISubEventForm(Interface):
    """Define the fields of our form
    """
    title = schema.TextLine(title=_(u"Title"),
          required=True)
    start = schema.Datetime(title=_(u"Start Date"),
          description=_(u"Use format CCYY-MM-DD hh:mm"),
          required=True)
    end = schema.Datetime(title=_(u"End Date"),
          description=_(u"Use format CCYY-MM-DD hh:mm"),
          required=True)


class SubEventForm(formbase.PageForm):
    form_fields = form.FormFields(ISubEventForm)
    label = _(u"Sub-Events Creation Form")
    description = _(u"Create minimalistic sub-event")

    # This trick hides the editable border and tabs in Plone
    def __call__(self):
        self.request.set('disable_border', True)
        return super(SubEventForm, self).__call__()

    @form.action(_(u"Add"))
    def action_add(self, action, data):
        """ Add a subevent to current event
        """

        context = aq_inner(self.context)

        from zope.event import notify
        from zope.lifecycleevent import ObjectCreatedEvent, ObjectModifiedEvent
        id = context.generateUniqueId('ELEvent')
        obj = ELEvent(id)
        notify(ObjectCreatedEvent(obj))
        context._setObject(id, obj)
        obj = context._getOb(id)
        kwargs = {
            'title': data['title'],
            'startDate': dt2DT(data['start']),
            'endDate': dt2DT(data['end']),
            }
        obj.initializeArchetype(**kwargs)
        notify(ObjectModifiedEvent(obj))

        # Issue a status message
        confirm = _(u"Sub-events created")
        IStatusMessage(self.request).addStatusMessage(
                 confirm, type='info')

        self.request.response.redirect(
            "%s" % context.absolute_url())
        return ''

