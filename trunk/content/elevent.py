# -*- coding: utf-8 -*-
#
# File: elevent.py
#
# Copyright (c) 2010 by Webtide (C)2010
# Generator: ArchGenXML Version 2.5
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """Mike Metcalfe <mike@webtide.co.za>, Jurgen Blignaut <jurgen@webtide.co.za>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import \
    ReferenceBrowserWidget
from Products.eventslist.config import *

# additional imports from tagged value 'import'
from Products.ATContentTypes.content.event import ATEvent

##code-section module-header #fill in your manual code here
import logging
from DateTime import DateTime
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone import PloneMessageFactory as _
from Products.eventslist.vocabularies \
    import event_type_vocabulary, venue_vocabulary
##/code-section module-header

schema = Schema((

    BooleanField(
        name='isInternal',
        default=False,
        widget=BooleanField._properties['widget'](
            label="Hosted with EventsList?",
            label_msgid='eventslist_label_isInternal',
            i18n_domain='eventslist',
        ),
        read_permission="EventsList: Manage Events",
        write_permission="EventsList: Manage Events",
    ),
    BooleanField(
        name='isBookable',
        default= False,
        widget=BooleanField._properties['widget'](
            label="Bookable event?",
            description="Enable online bookings",
            label_msgid='eventslist_label_isBookable',
            description_msgid='eventslist_help_isBookable',
            i18n_domain='eventslist',
        ),
        read_permission="EventsList: Manage Events",
        write_permission="EventsList: Manage Events",
    ),
    DateTimeField(
        name='earlybirdEndDate',
        widget=DateTimeField._properties['widget'](
            label="Last Date for Early Bird Registration",
            label_msgid='eventslist_label_earlybirdEndDate',
            i18n_domain='eventslist',
        ),
        read_permission="EventsList: Manage Events",
        write_permission="EventsList: Manage Events",
    ),
    DateTimeField(
        name='cancelEndDate',
        widget=DateTimeField._properties['widget'](
            label="Last Date for Cancellation",
            label_msgid='eventslist_label_cancelEndDate',
            i18n_domain='eventslist',
        ),
        read_permission="EventsList: Manage Events",
        write_permission="EventsList: Manage Events",
    ),
    StringField(
        name='contactMobile',
        widget=StringField._properties['widget'](
            label="Contact Mobile Number",
            label_msgid='eventslist_label_contactMobile',
            i18n_domain='eventslist',
        ),
    ),
    StringField(
        name='contactFax',
        widget=StringField._properties['widget'](
            label="Contact Person Fax Number",
            label_msgid='eventslist_label_contactFax',
            i18n_domain='eventslist',
        ),
        read_permission="EventsList: Manage Events",
        write_permission="EventsList: Manage Events",
    ),
    TextField(
        name='liabilityClause',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="Liability Clause Text",
            label_msgid='eventslist_label_liabilityClause',
            i18n_domain='eventslist',
        ),
        default_output_type='text/html',
        read_permission="EventsList: Manage Events",
        write_permission="EventsList: Manage Events",
    ),
    TextField(
        name='declarationAndConfirmation',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="Declaration and Confirmation Text",
            label_msgid='eventslist_label_declarationAndConfirmation',
            i18n_domain='eventslist',
        ),
        default_output_type='text/html',
        read_permission="EventsList: Manage Events",
        write_permission="EventsList: Manage Events",
    ),
    DateTimeField(
        name='signupStartDate',
        widget=DateTimeField._properties['widget'](
            label="Registration Start Date",
            label_msgid='eventslist_label_signupStartDate',
            i18n_domain='eventslist',
        ),
        read_permission="EventsList: Manage Events",
        write_permission="EventsList: Manage Events",
    ),
    DateTimeField(
        name='signupEndDate',
        widget=DateTimeField._properties['widget'](
            label="Registration End Date",
            label_msgid='eventslist_label_signupEndDate',
            i18n_domain='eventslist',
        ),
        read_permission="EventsList: Manage Events",
        write_permission="EventsList: Manage Events",
    ),
    BooleanField(
        name='registrationIsOpen',
        widget=BooleanField._properties['widget'](
            label="Registration is Open",
            label_msgid='eventslist_label_registrationIsOpen',
            i18n_domain='eventslist',
        ),
        read_permission="EventsList: Manage Events",
        write_permission="EventsList: Manage Events",
    ),
    ComputedField(
        name='venueName',
        widget=ComputedField._properties['widget'](
            label='Venuename',
            label_msgid='eventslist_label_venueName',
            i18n_domain='eventslist',
        ),
    ),
    ComputedField(
        name='venueRegion',
        widget=ComputedField._properties['widget'](
            label='VenueRegion',
            label_msgid='eventslist_label_venueName',
            i18n_domain='eventslist',
        ),
    ),
    ComputedField(
        name='parentTitle',
        widget=ComputedField._properties['widget'](
            label='Parenttitle',
            label_msgid='eventslist_label_parentTitle',
            i18n_domain='eventslist',
        ),
    ),
    ComputedField(
        name='fullTitle',
        widget=ComputedField._properties['widget'](
            label='Fulltitle',
            label_msgid='eventslist_label_fullTitle',
            i18n_domain='eventslist',
        ),
    ),
    StringField(
        name='reviewUrl',
        widget=StringField._properties['widget'](
          label="Review URL",
          description=u"Provide the URL of where this event has been reviewed",
          label_msgid='eventslist_label_reviewUrl',
          i18n_domain='eventslist',
        ),
        validators=('isURL',),
    ),
    StringField(
        name='ticketUrl',
        widget=StringField._properties['widget'](
            label="Ticket URL",
            description=u"Provide the URL of where a ticket for the event can be purchased online",
            label_msgid='eventslist_label_ticketURL',
            i18n_domain='eventslist',
        ),
        validators=('isURL',),
    ),
    StringField(
        name='priceRange',
        widget=StringField._properties['widget'](
            label="Price Range",
            description=u"Enter the ticket price range. Eg. R100 - R250",
            label_msgid='eventslist_label_priceRange',
            i18n_domain='eventslist',
        ),
    ),
    ReferenceField(
        name='venue',
        vocabulary='getVenueVocab',
        widget=SelectionWidget(
            label='Venue',
            description=u"Select a venue. Note: if your venue is not in the list, enter it the 'New Venue' field below",
            label_msgid='eventslist_label_venue',
            i18n_domain='eventslist',
        ),
        allowed_types=('Venue',),
        multiValued=0,
        relationship='elevent_venue',
    ),
    BooleanField(
        name='terms',
        widget=BooleanField._properties['widget'](
            label="Terms and Conditions",
            label_msgid='eventslist_label_terms',
            i18n_domain='eventslist',
        ),
    ),
    ImageField('tileImage',
        required = False,
        #storage = AnnotationStorage(),
        languageIndependent = True,
        max_size = (400,400),
        sizes= { 'preview' : (400, 400),
                'mini'    : (200, 200),
                'thumb'   : (128, 128),
                'tile'    :  (64, 64),
                'icon'    :  (32, 32),
                'listing' :  (16, 16),
               },
        validators = (('isNonEmptyFile', True)),
        widget = ImageWidget(
            label= _(u'label_tile_image', default=u'Tile Image'),
            show_content_type = False)
        ),
    

),
)


ELEvent_schema = BaseFolderSchema.copy() + \
    getattr(ATEvent, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
ELEvent_schema.moveField('isInternal', after='title')
ELEvent_schema.moveField('isBookable', after='isInternal')
ELEvent_schema.moveField('eventType', after='isBookable')
ELEvent_schema.moveField('text', after='description')
ELEvent_schema.moveField('eventUrl', after='text')
ELEvent_schema.moveField('ticketUrl', after='eventUrl')
ELEvent_schema.moveField('reviewUrl', after='ticketUrl')
ELEvent_schema.moveField('venue', after='reviewUrl')
ELEvent_schema.moveField('location', after='venue')
ELEvent_schema.moveField('startDate', after='location')
ELEvent_schema.moveField('endDate', after='startDate')
ELEvent_schema.moveField('priceRange', after='endDate')
ELEvent_schema.moveField('registrationIsOpen', after='priceRange')
ELEvent_schema.moveField('signupStartDate', after='registrationIsOpen')
ELEvent_schema.moveField('earlybirdEndDate', after='signupStartDate')
ELEvent_schema.moveField('signupEndDate', after='earlybirdEndDate')
ELEvent_schema.moveField('cancelEndDate', after='signupEndDate')
ELEvent_schema.moveField('contactName', after='cancelEndDate')
ELEvent_schema.moveField('contactEmail', after='contactName')
ELEvent_schema.moveField('contactPhone', after='contactEmail')
ELEvent_schema.moveField('contactMobile', after='contactPhone')
ELEvent_schema.moveField('contactFax', after='contactMobile')
ELEvent_schema.moveField('attendees', after='contactFax')
ELEvent_schema.moveField('liabilityClause', after='attendees')
ELEvent_schema.moveField('declarationAndConfirmation', after='liabilityClause')
ELEvent_schema.moveField('tileImage', after='declarationAndConfirmation')
ELEvent_schema.moveField('terms', after='tileImage')

#Set default values from configlet tool
ELEvent_schema['liabilityClause'].default_method = \
    'getDefaultLiabilityClause'
ELEvent_schema['declarationAndConfirmation'].default_method = \
    'getDefaultDeclarationAndConfirmation'

#Set dates fields to NOT be required
ELEvent_schema['startDate'].required = False
ELEvent_schema['startDate'].default_method = 'getDefaultStartDate'
ELEvent_schema['startDate'].widget.description=_(u"Enter the first date of the event and it's starting time (DD/MM/CCYY HH:MM)")
ELEvent_schema['endDate'].required = False
ELEvent_schema['endDate'].default_method = 'getDefaultEndDate'
ELEvent_schema['endDate'].widget.description=_(u"Enter the last date of the event and it's ending time (DD/MM/CCYY HH:MM)")

#Change field labels and descriptions
ELEvent_schema['title'].widget.label = 'Event Title'
ELEvent_schema['title'].widget.description=u"Submit your event title. Please keep it short"
ELEvent_schema['eventType'].widget.label = 'Event Type'
ELEvent_schema['eventType'].widget.description=u"Select one event catagory"
ELEvent_schema['eventType'].widget =  \
      SelectionWidget(
            label="Event Type",
            label_msgid='eventslist_label_eventtype',
            i18n_domain='eventslist',
            description=u"Select one event catagory",
            format='select',)
ELEvent_schema['eventType'].vocabulary = "getEventTypeVocab"

ELEvent_schema['description'].widget.label = 'Short Event Description'
ELEvent_schema['description'].widget.description=u"Enter a short description on your event. Note that this is important as it is used in our RSS feed"
ELEvent_schema['text'].widget.label = 'Long Event Description'
ELEvent_schema['text'].widget.description=u"Enter the full details of your event"
ELEvent_schema['location'].widget.label = 'New Venue'
ELEvent_schema['location'].widget.description=u"Sumbit a new venue and we'll add it for you"
ELEvent_schema['eventUrl'].widget.label = 'Performer URL'
ELEvent_schema['eventUrl'].widget.description=u"Provide the URL of performer's website"

ELEvent_schema['attendees'].read_permission="EventsList: Manage Events,"
ELEvent_schema['attendees'].write_permission="EventsList: Manage Events,"
##/code-section after-schema

class ELEvent(BaseFolder, ATEvent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IELEvent)

    meta_type = 'ELEvent'
    _at_rename_after_creation = True

    schema = ELEvent_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    # Manually created methods

    def canSignup(self):
        # check if registration is enabled
        if not self.getRegistrationIsOpen():
            return False

        # Check that we have an authenticated member
        # and it is not admin
        mt = getToolByName(self, 'portal_membership')
        member = mt.getAuthenticatedMember()
        if mt.isAnonymousUser() or member.getId() == 'admin':
            return False

        # check that we are between the sign up start and end dates
        # TODO: check dates!
        start = self.getSignupStartDate()
        end = self.getSignupEndDate()
        now = DateTime()
        if start and start > now:
            return False
        if end and end <= now:
            return False

        return True

    def isTopEvent(self):
      return not self.getParentEvent()

    def getTopEvent(self):
      top = self
      while top.getParentEvent():
          top = top.getParentEvent()
      return top

    def hasSubEvents(self):
        return len(self.objectIds(spec='ELEvent')) > 0

    def getSubEvents(self):
        subs = self.objectValues(spec='ELEvent')
        if len(subs) > 1:
            subs.sort(lambda x, y: cmp(x.getStartDate(), y.getStartDate()))
        return subs

    def getDefaultLiabilityClause(self):
        configtool = getToolByName(self, 'portal_eventsconfiglet')
        return configtool.getLiabilityClause()

    def getDefaultDeclarationAndConfirmation(self):
        configtool = getToolByName(self, 'portal_eventsconfiglet')
        return configtool.getDeclarationAndConfirmation()

    def getParentTitle(self):
        parent = getParentEvent(self)
        if parent:
            gparent = getParentEvent(parent)
            if gparent:
                return '%s - %s' % (
                    gparent.getParentTitle(),
                    parent.getField('title').get(parent))
            else:
                return parent.getField('title').get(parent)
        #otherwise
        return ''

    def getFullTitle(self):
        parent = getParentEvent(self)
        if parent:
            return '%s - %s' % (
              parent.getFullTitle(),
              self.getField('title').get(self))
        else:
          	return self.getField('title').get(self)

    def Description(self):
        desc = self.getField('description').get(self)
        if len(desc) > 0:
            return desc
        parent = getParentEvent(self)
        if parent:
            return parent.getField('description').get(parent)
        #otherwise
        return ''

    def getText(self):
        txt = self.getField('text').get(self)
        if len(txt) > 0:
            return txt
        parent = getParentEvent(self)
        if parent:
            return parent.getField('text').get(parent)
        #otherwise
        return ''

    def getStartDate(self):
        if self.startDate:
            return self.startDate
        if self.hasSubEvents():
            subs = self.getSubEvents()
            return subs[0].startDate
        #otherwise
        return ''

    def getEndDate(self):
        if self.endDate:
            return self.endDate
        if self.hasSubEvents():
            subs = self.getSubEvents()
            return subs[-1].endDate
        #otherwise
        return ''

    def getDefaultStartDate(self):
        return

    def getDefaultEndDate(self):
        return

    def Subject(self):
        subject = self.getField('subject').get(self)
        if len(subject) > 0:
            return subject
        parent = getParentEvent(self)
        if parent:
            return parent.Subject()
        return ()

    def getLocation(self):
        if hasattr(self,'location'):
            if len(self.location) > 0:
                return self.location
            parent = getParentEvent(self)
            if parent:
                return parent.getLocation()
        #otherwise
        return ''

    def getContactName(self):
        if self.contactName and len(self.contactName) > 0:
            return self.contactName
        parent = getParentEvent(self)
        if parent:
            return parent.contactName

    def getContactEmail(self):
        if self.contactEmail and len(self.contactEmail) > 0:
            return self.contactEmail
        parent = getParentEvent(self)
        if parent:
            return parent.contactEmail

    def getContactMobile(self):
        if self.isTemporary():
            return ''
        if self.contactMobile and len(self.contactMobile) > 0:
            return self.contactMobile
        parent = getParentEvent(self)
        if parent:
            return parent.contactMobile

    def getNextWorkflowActions(self):
        """ get the available workflow actions on the object
        """
        wft = getToolByName(self, 'portal_workflow')
        return wft.listActions(object=self)

    def getReviewState(self):
        """ get workflow state
        """
        wft = getToolByName(self, 'portal_workflow')
        return wft.getInfoFor(self, 'review_state')

    def getParentEvent(self):
        if self.aq_inner.aq_parent:
            portal_type = self.aq_inner.aq_parent.get('portal_type', None)
            if portal_type:
                if portal_type == 'ELFolder':
                    return
                if portal_type == 'ELEvent':
                    return self.aq_inner.aq_parent
                return getParentEvent(self.aq_inner.aq_parent)
            return getParentEvent(self.aq_inner.aq_parent)

    def getEventFolder(self):
        if self.aq_inner.aq_parent:
            parent = self.aq_inner.aq_parent
            portal_type = parent.get('portal_type', None)
            if portal_type:
                if portal_type == 'ELFolder':
                    return parent
                return parent.getEventFolder()
            return parent.getEventFolder()

    def getVenueFolder(self):
        urltool = getToolByName(self, 'portal_url')
        portal = urltool.getPortalObject()
        folder = portal['eventslists-venues']
        return folder.absolute_url()

    def getVenueObject(self):
        venue = self.getVenue()
        if venue:
           return venue
        else:
           parent = self.getParentEvent()
           if parent:
               return parent.getVenueObject()

    def getVenueName(self):
        """ Use this to get location name. if venue not set use other location
        """
        venue = self.getVenueObject()
        if venue:
            return venue.getShortName()
        #otheriwse
        return self.getLocation()

    def setVenue(self, value):
        """ Set the venue
        """
        #Delete existing values
        rc = getToolByName(self, 'reference_catalog')
        rc.deleteReferences(self, relationship='elevent_venue')
        self.venue = None
        if value == '0':
          return
        self.venue = value
        venue = rc.lookupObject(value)
        rc.addReference(self, venue, relationship='elevent_venue')

    def getVenuePath(self):
        """ Use this to get the path to the venue
        """
        venue = self.getVenueObject()
        if venue:
            path = "/".join(venue.getPhysicalPath())
            logging.info('getVenuePath = "%s"' % path)
            return path
        return ''

    def getVenueRegion(self):
        venue = self.getVenueObject()
        if venue:
            return venue.getRegion()

    def getEventTypeVocab(self):
      vocab = event_type_vocabulary(self).by_value.keys()
      vocab.sort()
      return vocab

    def getVenueVocab(self):
      vocab = [(i.value, i.title) for i in venue_vocabulary(self)]
      return vocab


    def getRSSText(self):
        """ Return the text that will go out on the RSS Feed for an elevent
        """
        txt = ""
        try:
          if len(self.Description()) > 0:
            txt += "<b>%s</b><br />" % self.Description()
        except UnicodeDecodeError, e:
          msg = 'unicodeerror in description of event %s (%s): [%s]' % (
            self.getParentTitle(), self.absolute_url(), e)
          logging.warn(msg)
          #self.MailHost.send(msg, 'info@webtide.co.za',
          #    'mike@webtide.co.za', 'Unicode error in content')
        txt += "%s at %s<br />" % (
          self.getStartDate().Date(),
          self.getStartDate().Time()[:-3])
        try:
          txt += "%s<br />" % self.getVenueName()
        except UnicodeDecodeError, e:
          msg = 'UnicodeError in venue of event %s (%s): [%s]' % (
            self.getParentTitle(), self.absolute_url(), e)
          logging.warn(msg)
          #self.MailHost.send(msg, 'info@webtide.co.za',
          #    'mike@webtide.co.za', 'Unicode error in content')
        try:
          if len(self.getText()) > 0:
            txt += "%s" % self.getText()
        except UnicodeDecodeError, e:
          msg = 'UnicodeError in body of event %s (%s): [%s]' % (
            self.getParentTitle(), self.absolute_url(), e)
          logging.warn(msg)
          #self.MailHost.send(msg, 'info@webtide.co.za',
          #    'mike@webtide.co.za', 'Unicode error in content')
          #Ignore event
        return txt


registerType(ELEvent, PROJECTNAME)
# end of class ELEvent

def getParentEvent(obj):
    if obj.id == '':
        return
    if obj.aq_inner.aq_parent:
        portal_type = obj.aq_inner.aq_parent.get('portal_type', None)
        if portal_type:
            if portal_type == 'ELFolder':
                return
            if portal_type == 'ELEvent':
                return obj.aq_inner.aq_parent
            return getParentEvent(obj.aq_inner.aq_parent)
        return 

