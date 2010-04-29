# -*- coding: utf-8 -*-
#
# File: venue.py
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

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='country',
        default="South Africa",
        widget=StringField._properties['widget'](
            label='Country',
            label_msgid='eventslist_label_country',
            i18n_domain='eventslist',
        ),
    ),
    StringField(
        name='region',
        default="Western Cape",
        widget=StringField._properties['widget'](
            label='Region',
            label_msgid='eventslist_label_region',
            i18n_domain='eventslist',
        ),
    ),
    StringField(
        name='city',
        widget=StringField._properties['widget'](
            label='City',
            label_msgid='eventslist_label_city',
            i18n_domain='eventslist',
        ),
    ),
    StringField(
        name='suburb',
        widget=StringField._properties['widget'](
            label='Suburb',
            label_msgid='eventslist_label_suburb',
            i18n_domain='eventslist',
        ),
    ),
    TextField(
        name='address',
        widget=TextAreaWidget(
            label='Address',
            label_msgid='eventslist_label_address',
            i18n_domain='eventslist',
        ),
    ),
    StringField(
        name='phone',
        widget=StringField._properties['widget'](
            label='Phone',
            label_msgid='eventslist_label_phone',
            i18n_domain='eventslist',
        ),
    ),
    FixedPointField(
        name='latitude',
        widget=FixedPointField._properties['widget'](
            label='Latitude',
            label_msgid='eventslist_label_latitude',
            i18n_domain='eventslist',
        ),
    ),
    FixedPointField(
        name='longitude',
        widget=FixedPointField._properties['widget'](
            label='Longitude',
            label_msgid='eventslist_label_longitude',
            i18n_domain='eventslist',
        ),
    ),
    TextField(
        name='postalAddress',
        widget=TextAreaWidget(
            label='Postaladdress',
            label_msgid='eventslist_label_postalAddress',
            i18n_domain='eventslist',
        ),
        label="Full Post Address",
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Venue_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Venue(BaseFolder, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IVenue)

    meta_type = 'Venue'
    _at_rename_after_creation = True

    schema = Venue_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    def getCountry(self):
        if len(self.country) > 0:
            return self.country
        parent = getParentVenue(self)
        if parent:
            return parent.getCountry()

    def getParentVenue(self):
        if self.aq_parent:
            portal_type = self.aq_parent.get('portal_type', None)
            if portal_type:
                if portal_type == 'VenueFolder':
                    return
                if portal_type == 'Venue':
                    return self.aq_parent
                return getParentVenue(self.aq_parent)
            return getParentVenue(self.aq_parent)

registerType(Venue, PROJECTNAME)
# end of class Venue

##code-section module-footer #fill in your manual code here
def getParentVenue(obj):
    if obj.aq_parent:
        portal_type = obj.aq_parent.get('portal_type', None)
        if portal_type:
            if portal_type == 'VenueFolder':
                return
            if portal_type == 'Venue':
                return obj.aq_parent
            return getParentEvent(obj.aq_parent)
        return getParentEvent(obj.aq_parent)
##/code-section module-footer



