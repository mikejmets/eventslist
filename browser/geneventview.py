import logging
from datetime import timedelta
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
  days = ['Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
  terms = []
  for day in days:
    val = days.index(day) + 1
    term = SimpleTerm(value=val, token=str(val), title=day)
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
    start_date = schema.Datetime(title=_(u"Start Date"),
        description=_(u"Use format CCYY-MM-DD HH:MM"),
          required=True)
    end_date = schema.Datetime(title=_(u"End Date"),
          description=_(u"Use format CCYY-MM-DD HH:MM"),
          required=True)
    venue = schema.Choice(title=_(u"Venue"),
          description=_(u"If venue is not in this list, go to Venues and add it first"),
          source='Products.eventslist.vocabularies.VenueVocabulary',
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

        event_date = data['start_date']
        start_delta = timedelta(
            hours=event_date.hour, minutes=event_date.minute)
        event_date = event_date - start_delta
        end_date = data['end_date']
        end_delta = timedelta(
            hours=end_date.hour, minutes=end_date.minute)
        dows = data['dows']
        venue = data['venue']

        cnt = 1
        while True:
          if event_date > end_date:
            break
          dow = event_date.isoweekday()
          if dow in dows:
            id = context.generateUniqueId('ELEvent')
            obj = ELEvent(id)
            notify(ObjectCreatedEvent(obj))
            context._setObject(id, obj)
            obj = context._getOb(id)
            #default if no Subject
            sub_title = "%s" % context.Title()
            if len(context.Subject()) > 0:
              sub_title = "%s" % context.Subject()[0]
            sub_start_date = event_date + start_delta
            sub_end_date = event_date + end_delta
            kwargs = {
                'title': sub_title,
                'startDate': dt2DT(sub_start_date),
                'endDate': dt2DT(sub_end_date),
                }
            if venue:
                kwargs['venue'] = venue
            obj.initializeArchetype(**kwargs)
            notify(ObjectModifiedEvent(obj))
            cnt += 1
          event_date += timedelta(1)

        # Issue a status message
        confirm = _(u"Generated events")
        IStatusMessage(self.request).addStatusMessage(
                 confirm, type='info')

        self.request.response.redirect(
            "%s" % context.absolute_url())
        return ''

