# -*- coding: utf-8 -*-
#
# File: elevent.py
#
# Copyright (c) 2010 by Webtide (C)2010
# Generator: ArchGenXML Version 2.4.1
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
from Products.ATVocabularyManager.namedvocabulary import NamedVocabulary
from Products.eventslist.config import *

# additional imports from tagged value 'import'
from Products.ATContentTypes.content.event import ATEvent

##code-section module-header #fill in your manual code here
import logging
from DateTime import DateTime
from Products.CMFCore.utils import getToolByName
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import \
    ReferenceBrowserWidget
from Products.CMFPlone import PloneMessageFactory as _
##/code-section module-header

schema = Schema((

    BooleanField(
        name='isInternal',
        default="False",
        widget=BooleanField._properties['widget'](
            label="Hosted with EventsList?",
            label_msgid='eventslist_label_isInternal',
            i18n_domain='eventslist',
        ),
    ),
    BooleanField(
        name='isBookable',
        default="False",
        widget=BooleanField._properties['widget'](
            label="Bookable event?",
            description="Enable online bookings",
            label_msgid='eventslist_label_isBookable',
            description_msgid='eventslist_help_isBookable',
            i18n_domain='eventslist',
        ),
    ),
    DateTimeField(
        name='earlybirdEndDate',
        widget=DateTimeField._properties['widget'](
            label="Last Date for Early Bird Registration",
            label_msgid='eventslist_label_earlybirdEndDate',
            i18n_domain='eventslist',
        ),
    ),
    DateTimeField(
        name='cancelEndDate',
        widget=DateTimeField._properties['widget'](
            label="Last Date for Cancellation",
            label_msgid='eventslist_label_cancelEndDate',
            i18n_domain='eventslist',
        ),
    ),
    StringField(
        name='contactMobile',
        widget=StringField._properties['widget'](
            label="Contact Person Mobile Number",
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
    ),
    DateTimeField(
        name='signupStartDate',
        widget=DateTimeField._properties['widget'](
            label="Registration Start Date",
            label_msgid='eventslist_label_signupStartDate',
            i18n_domain='eventslist',
        ),
    ),
    DateTimeField(
        name='signupEndDate',
        widget=DateTimeField._properties['widget'](
            label="Registration End Date",
            label_msgid='eventslist_label_signupEndDate',
            i18n_domain='eventslist',
        ),
    ),
    BooleanField(
        name='registrationIsOpen',
        widget=BooleanField._properties['widget'](
            label="Registration is Open",
            label_msgid='eventslist_label_registrationIsOpen',
            i18n_domain='eventslist',
        ),
    ),
    LinesField(
        name='category',
        widget=InAndOutWidget(
            label='Category',
            label_msgid='eventslist_label_category',
            i18n_domain='eventslist',
        ),
        vocabulary=NamedVocabulary("""event_catagories"""),
    ),
    ReferenceField(
        name='venues',
        widget=ReferenceBrowserWidget(
            label='Venues',
            label_msgid='eventslist_label_venues',
            i18n_domain='eventslist',
        ),
        allowed_types=('Venue',),
        multiValued=0,
        relationship='elevent_venue',
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

ELEvent_schema = BaseFolderSchema.copy() + \
    getattr(ATEvent, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
ELEvent_schema.moveField('isInternal', after='title')
ELEvent_schema.moveField('isBookable', after='isInternal')
ELEvent_schema.moveField('category', after='isInternal')
ELEvent_schema.moveField('eventType', after='category')
ELEvent_schema.moveField('text', after='description')
ELEvent_schema.moveField('eventUrl', after='text')
ELEvent_schema.moveField('venues', after='eventUrl')
ELEvent_schema.moveField('location', after='venues')
ELEvent_schema.moveField('startDate', after='location')
ELEvent_schema.moveField('endDate', after='startDate')
ELEvent_schema.moveField('registrationIsOpen', after='endDate')
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

#Set default values from configlet tool
ELEvent_schema['liabilityClause'].default_method = \
    'getDefaultLiabilityClause'
ELEvent_schema['declarationAndConfirmation'].default_method = \
    'getDefaultDeclarationAndConfirmation'

#Set dates fields to NOT be required
ELEvent_schema['startDate'].required = False
ELEvent_schema['startDate'].default_method = 'getDefaultStartDate'
ELEvent_schema['endDate'].required = False
ELEvent_schema['endDate'].default_method = 'getDefaultEndDate'

#Change field labels and descriptions
ELEvent_schema['venues'].widget.label = 'Venue'
ELEvent_schema['location'].widget.label = 'Other Location'
ELEvent_schema['location'].widget.description = 'Venue not found? Add it here.'

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
        return self.objectValues(spec='ELEvent')

    def getDefaultLiabilityClause(self):
        configtool = getToolByName(self, 'portal_eventsconfiglet')
        return configtool.getLiabilityClause()

    def getDefaultDeclarationAndConfirmation(self):
        configtool = getToolByName(self, 'portal_eventsconfiglet')
        return configtool.getDeclarationAndConfirmation()

    def getStartDate(self):
        if self.startDate:
            return self.startDate
        if self.isTopEvent():
            subs = self.objectValues(spec='ELEvent')
            return subs[0].startDate
        else:
            parent = getParentEvent(self)
            if parent:
                return parent.getStartDate()
            
    def getEndDate(self):
        if self.endDate:
            return self.endDate
        if self.isTopEvent():
            subs = self.objectValues(spec='ELEvent')
            return subs[0].endDate
        else:
            parent = getParentEvent(self)
            if parent:
                return parent.getEndDate()

    def getDefaultStartDate(self):
        return

    def getDefaultEndDate(self):
        return

    def getSubject(self):
        if len(self.Subject()) > 0:
            return self.Subject()
        parent = getParentEvent(self)
        if parent:
            return parent.Subject()
        return ()

    def getLocation(self):
        venues = self.getVenues()
        if venues:
            return venues.title
        if len(self.location) > 0:
            return self.location
        parent = getParentEvent(self)
        if parent:
            return parent.getLocation()

    def getContactName(self):
        if len(self.contactName) > 0:
            return self.contactName
        parent = getParentEvent(self)
        if parent:
            return parent.contactName

    def getContactEmail(self):
        if len(self.contactEmail) > 0:
            return self.contactEmail
        parent = getParentEvent(self)
        if parent:
            return parent.contactEmail

    def getNextWorkflowActions(self):
        """ get the available workflow actions on the object
        """
        wft = getToolByName(self, 'portal_workflow')
        return wft.listActions(object=self)

    def getParentEvent(self):
        if self.aq_parent:
            portal_type = self.aq_parent.get('portal_type', None)
            if portal_type:
                if portal_type == 'ELFolder':
                    return
                if portal_type == 'ELEvent':
                    return self.aq_parent
                return getParentEvent(self.aq_parent)
            return getParentEvent(self.aq_parent)



registerType(ELEvent, PROJECTNAME)
# end of class ELEvent

##code-section module-footer #fill in your manual code here
def getParentEvent(obj):
    if obj.aq_parent:
        portal_type = obj.aq_parent.get('portal_type', None)
        if portal_type:
            if portal_type == 'ELFolder':
                return
            if portal_type == 'ELEvent':
                return obj.aq_parent
            return getParentEvent(obj.aq_parent)
        return getParentEvent(obj.aq_parent)
##/code-section module-footer



