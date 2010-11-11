# -*- coding: utf-8 -*-
#
# File: eventattendance.py
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

from Products.eventslist.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='initials',
        widget=StringField._properties['widget'](
            label='Initials',
            label_msgid='eventslist_label_initials',
            i18n_domain='eventslist',
        ),
    ),
    StringField(
        name='telephone',
        widget=StringField._properties['widget'](
            label='Telephone',
            label_msgid='eventslist_label_telephone',
            i18n_domain='eventslist',
        ),
    ),
    StringField(
        name='mobile',
        widget=StringField._properties['widget'](
            label='Mobile',
            label_msgid='eventslist_label_mobile',
            i18n_domain='eventslist',
        ),
    ),
    StringField(
        name='iceNumber',
        widget=StringField._properties['widget'](
            label="Emergency Number",
            label_msgid='eventslist_label_iceNumber',
            i18n_domain='eventslist',
        ),
    ),
    StringField(
        name='fax',
        widget=StringField._properties['widget'](
            label='Fax',
            label_msgid='eventslist_label_fax',
            i18n_domain='eventslist',
        ),
    ),
    StringField(
        name='company',
        widget=StringField._properties['widget'](
            label='Company',
            label_msgid='eventslist_label_company',
            i18n_domain='eventslist',
        ),
    ),
    StringField(
        name='jobTitle',
        widget=StringField._properties['widget'](
            label="Job Title",
            label_msgid='eventslist_label_jobTitle',
            i18n_domain='eventslist',
        ),
    ),
    StringField(
        name='mealPreference',
        widget=StringField._properties['widget'](
            label='Mealpreference',
            label_msgid='eventslist_label_mealPreference',
            i18n_domain='eventslist',
        ),
    ),
    StringField(
        name='otherMealPreference',
        widget=StringField._properties['widget'](
            label='Othermealpreference',
            label_msgid='eventslist_label_otherMealPreference',
            i18n_domain='eventslist',
        ),
    ),
    StringField(
        name='country',
        widget=StringField._properties['widget'](
            label='Country',
            label_msgid='eventslist_label_country',
            i18n_domain='eventslist',
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

EventAttendance_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class EventAttendance(BaseFolder, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IEventAttendance)

    meta_type = 'EventAttendance'
    _at_rename_after_creation = True

    schema = EventAttendance_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(EventAttendance, PROJECTNAME)
# end of class EventAttendance

##code-section module-footer #fill in your manual code here
##/code-section module-footer

