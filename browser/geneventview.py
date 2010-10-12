from zope.interface import Interface
from zope import schema
from zope.formlib import form
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from Products.Five.formlib import formbase
from Products.statusmessages.interfaces import IStatusMessage
from Acquisition import aq_inner
from Products.CMFPlone import PloneMessageFactory as _
from Products.eventslist.content.elevent import ELEvent
from Products.ATContentTypes.utils import dt2DT
from zope.event import notify
from zope.lifecycleevent import ObjectCreatedEvent, ObjectModifiedEvent

def _getDOWVocab():
  dows = ['Sun', 'Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat']
  terms = []
  for dow in dows:
    term = SimpleTerm(value=dows.index(dow), token=str(dows.index(dow)), title=dow)
    yield term

dow_vocab = SimpleVocabulary(list(_getDOWVocab()))

class IGenEventForm(Interface):
    """Define the fields of our form
    """
    dows = schema.List(
          title=_(u"D.O.W"),
          description=u"Days of the week",
          value_type = schema.Choice(
            vocabulary=dow_vocab)
          )
    title = schema.TextLine(title=_(u"Title"),
          required=True)
    include_count = schema.Bool(title=_(u"Include Counter In Title?"),
          default=False)
    start_date = schema.Datetime(title=_(u"Start Date"),
          description=_(u"Use format CCYY-MM-DD"),
          required=True)
    end_date = schema.Datetime(title=_(u"End Date"),
          description=_(u"Use format CCYY-MM-DD"),
          required=True)


class GenEventForm(formbase.PageForm):
    form_fields = form.FormFields(IGenEventForm)
    label = _(u"Generate Sub-Events Form")
    description = _(u"Generate sub-events")

    # This trick hides the editable border and tabs in Plone
    def __call__(self):
        self.request.set('disable_border', True)
        return super(GenEventForm, self).__call__()

    @form.action(_(u"Generate"))
    def action_generate(self, action, data):
        """ Generate subevents for current event
        """

        context = aq_inner(self.context)

        event_date = dt2DT(data['start_date'])
        end_date = dt2DT(data['end_date'])
        end_time = end_date.time
        dows = data['dows']
        title = data['title']
        include_count = data['include_count']

        cnt = 1
        while True:
          if event_date > end_date:
            break
          if event_date.dow() in dows:
            id = context.generateUniqueId('ELEvent')
            obj = ELEvent(id)
            notify(ObjectCreatedEvent(obj))
            context._setObject(id, obj)
            obj = context._getOb(id)
            sub_title = title
            if include_count:
              sub_title = "%s - %s" % (title, cnt)
            kwargs = {
                'title': sub_title,
                'startDate': event_date,
                'endDate': event_date - event_date.time + end_time,
                }
            obj.initializeArchetype(**kwargs)
            notify(ObjectModifiedEvent(obj))
            cnt += 1
          event_date += 1

        # Issue a status message
        confirm = _(u"Generated events")
        IStatusMessage(self.request).addStatusMessage(
                 confirm, type='info')

        self.request.response.redirect(
            "%s/sub_event_listing" % context.absolute_url())
        return ''

