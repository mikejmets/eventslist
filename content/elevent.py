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

from Products.eventslist.config import *

# additional imports from tagged value 'import'
from Products.ATContentTypes.content.event import ATEvent

##code-section module-header #fill in your manual code here
from DateTime import DateTime
from Products.CMFCore.utils import getToolByName
##/code-section module-header

schema = Schema((

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

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

ELEvent_schema = BaseFolderSchema.copy() + \
    getattr(ATEvent, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
ELEvent_schema.moveField('text', after='description')
ELEvent_schema.moveField('eventUrl', after='text')
ELEvent_schema.moveField('location', after='eventUrl')
ELEvent_schema.moveField('startDate', after='location')
ELEvent_schema.moveField('endDate', after='startDate')
ELEvent_schema.moveField('signupStartDate', after='endDate')
ELEvent_schema.moveField('earlybirdEndDate', after='signupStartDate')
ELEvent_schema.moveField('signupEndDate', after='earlybirdEndDate')
ELEvent_schema.moveField('cancelEndDate', after='signupEndDate')
ELEvent_schema.moveField('contactName', after='cancelEndDate')
ELEvent_schema.moveField('contactEmail', after='contactName')
ELEvent_schema.moveField('contactPhone', after='contactEmail')
ELEvent_schema.moveField('contactMobile', after='contactPhone')
ELEvent_schema.moveField('contactFax', after='contactMobile')
ELEvent_schema.moveField('attendees', after='contactFax')
ELEvent_schema.moveField('eventType', after='attendees')
ELEvent_schema.moveField('registrationIsOpen', after='eventType')
ELEvent_schema.moveField('liabilityClause', after='registrationIsOpen')
ELEvent_schema.moveField('declarationAndConfirmation', after='liabilityClause')

#Set default values from configlet tool
ELEvent_schema['liabilityClause'].default_method = \
    'getLiabilityClause'
ELEvent_schema['declarationAndConfirmation'].default_method = \
    'getDeclarationAndConfirmation'

#Set required fields for emails
ELEvent_schema['contactName'].required = True
ELEvent_schema['contactEmail'].required = True


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

    def getLiabilityClause(self):
        configtool = getToolByName(self, 'portal_eventsconfiglet')
        return configtool.getLiabilityClause()

    def getDeclarationAndConfirmation(self):
        configtool = getToolByName(self, 'portal_eventsconfiglet')
        return configtool.getDeclarationAndConfirmation()



registerType(ELEvent, PROJECTNAME)
# end of class ELEvent

##code-section module-footer #fill in your manual code here
##/code-section module-footer



