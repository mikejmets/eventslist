# -*- coding: utf-8 -*-
#
# File: booking.py
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
from Products.eventslist.config import *

# additional imports from tagged value 'import'
from Products.FinanceFields.MoneyField import MoneyField

##code-section module-header #fill in your manual code here
from Products.CMFCore.utils import getToolByName
import logging
##/code-section module-header

schema = Schema((

    StringField(
        name='salutation',
        widget=SelectionWidget(
            label="Salutation",
            label_msgid='eventslist_label_salutation',
            i18n_domain='eventslist',
        ),
        vocabulary=(('mr', 'Mr'), ('mrs', 'Mrs'), ('miss','Miss'), ('rev', 'Rev'), ('hon', 'Hon'), ('dr', 'Dr'), ('prof', 'Prof'),),
    ),
    StringField(
        name='initials',
        widget=StringField._properties['widget'](
            label="Initials",
            label_msgid='eventslist_label_initials',
            i18n_domain='eventslist',
        ),
        required=False,
    ),
    StringField(
        name='mobile',
        widget=StringField._properties['widget'](
            label="Mobile Number",
            label_msgid='eventslist_label_mobile',
            i18n_domain='eventslist',
        ),
    ),
    StringField(
        name='icenumber',
        widget=StringField._properties['widget'](
            label="Emergency Number",
            label_msgid='eventslist_label_icenumber',
            i18n_domain='eventslist',
        ),
        required=False,
    ),
    StringField(
        name='mealPreference',
        widget=SelectionWidget(
            label="Meal Preference",
            description="Indicate Your Meal Preference if Applicable",
            format="radio",
            label_msgid='eventslist_label_mealPreference',
            description_msgid='eventslist_help_mealPreference',
            i18n_domain='eventslist',
        ),
        vocabulary=(('kosher', 'Kosher'), ('halaal', 'Halaal'), ('vegetarian', 'Vegetarian'), ('other', 'Other')),
    ),
    StringField(
        name='otherMealPreference',
        widget=StringField._properties['widget'](
            label="Other Meal Preference",
            description="Describe any other meal preference if you selected Other above",
            label_msgid='eventslist_label_otherMealPreference',
            description_msgid='eventslist_help_otherMealPreference',
            i18n_domain='eventslist',
        ),
    ),
    MoneyField(
        name='totalCost',
        widget=MoneyField._properties['widget'](
            label='Totalcost',
            label_msgid='eventslist_label_totalCost',
            i18n_domain='eventslist',
        ),
    ),
    StringField(
        name='surname',
        widget=StringField._properties['widget'](
            label="Surname",
            label_msgid='eventslist_label_surname',
            i18n_domain='eventslist',
        ),
        required=1,
    ),
    StringField(
        name='firstname',
        widget=StringField._properties['widget'](
            label="First Names",
            label_msgid='eventslist_label_firstname',
            i18n_domain='eventslist',
        ),
        required=1,
    ),
    StringField(
        name='email',
        widget=StringField._properties['widget'](
            label="Email Address",
            label_msgid='eventslist_label_email',
            i18n_domain='eventslist',
        ),
        required=1,
    ),
    StringField(
        name='phone',
        widget=StringField._properties['widget'](
            label="Telephone Number",
            label_msgid='eventslist_label_phone',
            i18n_domain='eventslist',
        ),
        required=False,
    ),
    StringField(
        name='fax',
        widget=StringField._properties['widget'](
            label="Fax Number",
            label_msgid='eventslist_label_fax',
            i18n_domain='eventslist',
        ),
        required=False,
    ),
    StringField(
        name='company',
        widget=StringField._properties['widget'](
            label="Company / Employer",
            label_msgid='eventslist_label_company',
            i18n_domain='eventslist',
        ),
        required=False,
    ),
    StringField(
        name='function',
        widget=StringField._properties['widget'](
            label="Job Title",
            label_msgid='eventslist_label_function',
            i18n_domain='eventslist',
        ),
    ),
    StringField(
        name='country',
        widget=StringField._properties['widget'](
            label="Country",
            label_msgid='eventslist_label_country',
            i18n_domain='eventslist',
        ),
    ),
    ReferenceField(
        name='elevents',
        widget=ReferenceBrowserWidget(
            label='Elevents',
            label_msgid='eventslist_label_elevents',
            i18n_domain='eventslist',
        ),
        allowed_types=('ELEvent',),
        multiValued=0,
        relationship='booking_elevent',
    ),
    ReferenceField(
        name='elmembers',
        widget=ReferenceBrowserWidget(
            label='Elmembers',
            label_msgid='eventslist_label_elmembers',
            i18n_domain='eventslist',
        ),
        allowed_types=('ELMember',),
        multiValued=0,
        relationship='booking_elmember',
    ),
    ReferenceField(
        name='externalevents',
        widget=ReferenceBrowserWidget(
            label='Externalevents',
            label_msgid='eventslist_label_externalevents',
            i18n_domain='eventslist',
        ),
        allowed_types=('ExternalEvent',),
        multiValued=1,
        relationship='booking_externalevent',
    ),
    ReferenceField(
        name='packages',
        widget=ReferenceBrowserWidget(
            label='Packages',
            label_msgid='eventslist_label_packages',
            i18n_domain='eventslist',
        ),
        allowed_types=('Package',),
        multiValued=0,
        relationship='booking_package',
    ),
    ReferenceField(
        name='internalevents',
        widget=ReferenceBrowserWidget(
            label='Internalevents',
            label_msgid='eventslist_label_internalevents',
            i18n_domain='eventslist',
        ),
        allowed_types=('InternalEvent',),
        multiValued=1,
        relationship='booking_internalevent',
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Booking_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
# Booking_schema['title'].widget.visible = False
Booking_schema['totalCost'].widget.visible = {'edit':'hidden', 'view':'visible'}
Booking_schema.changeSchemataForField('internalevents', 'related')
Booking_schema.changeSchemataForField('elmembers', 'related')
Booking_schema.changeSchemataForField('packages', 'related')
Booking_schema.changeSchemataForField('externalevents', 'related')
Booking_schema.changeSchemataForField('elevents', 'related')
Booking_schema.moveField('salutation', after='title')
Booking_schema.moveField('surname', after='salutation')
Booking_schema.moveField('initials', after='surname')
Booking_schema.moveField('firstname', after='initials')
Booking_schema.moveField('email', after='firstname')
Booking_schema.moveField('phone', after='email')
Booking_schema.moveField('mobile', after='phone')
Booking_schema.moveField('icenumber', after='mobile')
Booking_schema.moveField('fax', after='icenumber')
Booking_schema.moveField('company', after='fax')
Booking_schema.moveField('function', after='company')
Booking_schema.moveField('country', after='function')
Booking_schema.moveField('mealPreference', after='country')
Booking_schema.moveField('otherMealPreference', after='mealPreference')
Booking_schema['salutation'].default_method='getDefaultSalutation'
Booking_schema['surname'].default_method='getDefaultLastName'
Booking_schema['initials'].default_method='getDefaultInitials'
Booking_schema['firstname'].default_method='getDefaultFirstName'
Booking_schema['email'].default_method='getDefaultEmail'
Booking_schema['phone'].default_method='getDefaultPhone'
Booking_schema['mobile'].default_method='getDefaultMobile'
Booking_schema['icenumber'].default_method='getDefaultICE'
Booking_schema['fax'].default_method='getDefaultFax'
Booking_schema['company'].default_method='getDefaultCompany'
Booking_schema['function'].default_method='getDefaultFunction'
Booking_schema['mealPreference'].default_method='getDefaultMealPreference'
Booking_schema['otherMealPreference'].default_method='getDefaultOtherPref'
Booking_schema['country'].default_method='getDefaultCountry'
##/code-section after-schema

class Booking(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IBooking)

    meta_type = 'Booking'
    _at_rename_after_creation = False

    schema = Booking_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    # Manually created methods

    def _getEventAttendancePrefs(self):
        mt = getToolByName(self, 'portal_membership')
        member = mt.getAuthenticatedMember()
        if member.getId() not in ['admin', 'Anonymous User']:
            # home = mt.getHomeFolder(member.getId())
            if 'event_attendance' in member.objectIds():
                return member['event_attendance']
        return None

    def getDefaultSalutation(self):
        mt = getToolByName(self, 'portal_membership')
        member = mt.getAuthenticatedMember()
        if member.getId() not in ['admin', 'Anonymous User']:
            return member.getSalutation()

    def getDefaultLastName(self):
        mt = getToolByName(self, 'portal_membership')
        member = mt.getAuthenticatedMember()
        if member.getId() not in ['admin', 'Anonymous User']:
            return member.getSurname()

    def getDefaultInitials(self):
        etp = self._getEventAttendancePrefs()
        if etp:
            return etp.getInitials()

    def getDefaultFirstName(self):
        mt = getToolByName(self, 'portal_membership')
        member = mt.getAuthenticatedMember()
        if member.getId() not in ['admin', 'Anonymous User']:
            return member.getFirstname()

    def getDefaultEmail(self):
        mt = getToolByName(self, 'portal_membership')
        member = mt.getAuthenticatedMember()
        if member.getId() not in ['admin', 'Anonymous User']:
            return member.getEmail()

    def getDefaultPhone(self):
        etp = self._getEventAttendancePrefs()
        if etp:
            return etp.getTelephone()

    def getDefaultMobile(self):
        etp = self._getEventAttendancePrefs()
        if etp:
            return etp.getMobile()

    def getDefaultICE(self):
        etp = self._getEventAttendancePrefs()
        if etp:
            return etp.getIceNumber()

    def getDefaultFax(self):
        etp = self._getEventAttendancePrefs()
        if etp:
            return etp.getFax()

    def getDefaultCompany(self):
        etp = self._getEventAttendancePrefs()
        if etp:
            return etp.getCompany()

    def getDefaultFunction(self):
        etp = self._getEventAttendancePrefs()
        if etp:
            return etp.getJobTitle()

    def getDefaultMealPreference(self):
        etp = self._getEventAttendancePrefs()
        if etp:
            return etp.getMealPreference()

    def getDefaultOtherPref(self):
        etp = self._getEventAttendancePrefs()
        if etp:
            return etp.getOtherMealPreference()

    def getDefaultCountry(self):
        etp = self._getEventAttendancePrefs()
        if etp:
            return etp.getCountry()



registerType(Booking, PROJECTNAME)
# end of class Booking

##code-section module-footer #fill in your manual code here
##/code-section module-footer



