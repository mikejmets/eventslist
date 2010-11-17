from datetime import datetime, timedelta
from Acquisition import aq_inner
from zope import schema
from zope.event import notify
from zope.lifecycleevent import ObjectCreatedEvent, ObjectModifiedEvent
from zope.interface import Interface
from z3c.form import form, button, field
from z3c.form.interfaces import INPUT_MODE
from plone.app.z3cform.layout import wrap_form
from plone.z3cform.z2 import setup_locale
from collective.z3cform.datetimewidget import DatetimeWidget

from Products.statusmessages.interfaces import IStatusMessage
from Products.ATContentTypes.utils import dt2DT
from Products.CMFPlone import PloneMessageFactory as _
from plone.app.textfield import RichText

from Products.eventslist.content.elevent import ELEvent
from Products.eventslist.content.interfaces import IELEvent

class IAddEventForm(Interface):
    """Define the fields of our form
    """
    title = schema.TextLine(title=_(u"Event Title"),
          description=u"Submit you event title. Please keep it short",
          required=True)
    event_type = schema.Choice(
          title=_(u"Event Type"),
          description=u"Select event catagory",
          source='Products.eventslist.vocabularies.EventTypeVocabulary',
          )
    description = schema.Text(title=_(u"Short Event Description"),
          description=u"Enter a short description on your event. Note that this is important as it is used in our RSS feed",
          required=False) #MJM HACK
    text = RichText(title=_(u"Long Event Description"),
          description=u"Enter the full details of your event",
          required=False)
    venue = schema.Choice(
          title=_(u"Venue"),
          description=u"Select a venue. If it is not in the list enter it into the field below 'Other Venue'",
          source='Products.eventslist.vocabularies.VenueVocabulary',
          )
    other_venue = schema.TextLine(title=_(u"Other Venue"),
          description=u"If the venue is not in the list above",
          required=False)
    event_url = schema.URI(title=_(u"Performer URL"),
          description=u"Provide the URL of performer's website",
          required=False)
    review_url = schema.URI(title=_(u"Review URL"),
          description=u"Provide the URL of where this event has been reviewed",
          required=False)
    ticket_url = schema.URI(title=_(u"Ticket URL"),
          description=u"Provide the URL of where a ticket for the event can be purchased online",
          required=False)
    start_date = schema.Datetime(title=_(u"Start Date"),
          description=_(u"Use format DD-MM-CCYY HH:MM"),
          default=datetime.now() + timedelta(hours=1)- timedelta(minutes=datetime.now().minute),
          required=False) #MJM HACK
    end_date = schema.Datetime(title=_(u"End Date"),
          description=_(u"Use format DD-MM-CCYY HH:MM"),
          default=datetime.now() + timedelta(hours=2)- timedelta(minutes=datetime.now().minute),
          required=False) # MJM HACK
    dows = schema.List(
          title=_(u"D.O.W"),
          description=u"Days of the week",
          required=False,
          value_type=schema.Choice(
            source='Products.eventslist.vocabularies.DOWVocabulary',),
          )


class AddEventForm(form.Form):
    ignoreContext = True
    fields = field.Fields(IAddEventForm)

    def updateWidgets(self):
      form.Form.updateWidgets(self)
      #Ensure date widgets work
      self.request.locale = setup_locale(self.request)
      #Hide the editable border and tabs in Plone
      self.request.set('disable_border', True)
      #self.fields['start_date'].default = datetime.now()
    
    @button.buttonAndHandler(u'Submit')
    def handleApply(self, action):
        data, errors = self.extractData()

        if errors:
            return

        context = aq_inner(self.context)
        start_date = data['start_date']
        start_delta = timedelta(
            hours=start_date.hour, minutes=start_date.minute)
        event_date = start_date - start_delta
        end_date = data['end_date']
        end_delta = timedelta(
            hours=end_date.hour, minutes=end_date.minute)
        mulitple_events = True
        if event_date == end_date - end_delta:
            mulitple_events = False
        dows = data['dows']
        title = data['title']
        event_type = data['event_type']
        description = data['description']
        text = data['text']
        venue_uid = data['venue']
        other_venue = data['other_venue']
        
        #Create parent
        id = context.generateUniqueId('ELEvent')
        obj = ELEvent(id)
        notify(ObjectCreatedEvent(obj))
        context._setObject(id, obj)
        obj = context._getOb(id)
        kwargs = {
            'title': title,
            'description': description,
            'text': text.raw,
            'eventType': (event_type,),
            }
        if venue_uid == 0 and other_venue:
          kwargs['location'] = other_venue
        if venue_uid != 0:
          obj.setVenue(venue_uid)
        if not mulitple_events:
          kwargs['startDate'] = dt2DT(start_date)
          kwargs['endDate'] = dt2DT(end_date)
        obj.initializeArchetype(**kwargs)
        notify(ObjectModifiedEvent(obj))

        if mulitple_events:
          #generate dates
          cnt = 1
          while True:
            if event_date > end_date:
              break
            dow = event_date.isoweekday()
            if dow in dows:
              id = obj.generateUniqueId('ELEvent')
              child = ELEvent(id)
              notify(ObjectCreatedEvent(child))
              obj._setObject(id, child)
              child = obj._getOb(id)
              sub_title = "%s - %s" % (title, cnt)
              sub_start_date = event_date + start_delta
              sub_end_date = event_date + end_delta
              kwargs = {
                  'title': sub_title,
                  'startDate': dt2DT(sub_start_date),
                  'endDate': dt2DT(sub_end_date),
                  }
              child.initializeArchetype(**kwargs)
              notify(ObjectModifiedEvent(child))
              cnt += 1
            event_date += timedelta(1)
        obj.reindexObject()

        # Issue a status message
        confirm = _(u"Generated events")
        IStatusMessage(self.request).addStatusMessage(
                 confirm, type='info')

        self.request.response.redirect(
            "%s" % context.absolute_url())
        return ''

    @button.buttonAndHandler(u'Cancel')
    def handleApply(self, action):
        context = aq_inner(self.context)
        self.request.response.redirect(
            "%s" % context.absolute_url())
        return ''

AddEventView = wrap_form(AddEventForm)