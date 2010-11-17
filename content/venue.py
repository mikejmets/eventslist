# -*- coding: utf-8 -*-
#
# File: venue.py
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
        name='country',
        widget=StringField._properties['widget'](
            label='Country',
            label_msgid='eventslist_label_country',
            i18n_domain='eventslist',
        ),
        default_method="getDefaultCountry",
    ),
    StringField(
        name='region',
        widget=StringField._properties['widget'](
            label='Region',
            label_msgid='eventslist_label_region',
            i18n_domain='eventslist',
        ),
        default_method="getDefaultRegion",
    ),
    StringField(
        name='subRegion',
        widget=StringField._properties['widget'](
            label="Sub Region",
            label_msgid='eventslist_label_subRegion',
            i18n_domain='eventslist',
        ),
        default_method="getDefaultSubRegion",
    ),
    StringField(
        name='city',
        widget=StringField._properties['widget'](
            label='City',
            label_msgid='eventslist_label_city',
            i18n_domain='eventslist',
        ),
        default_method="getDefaultCity",
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
            label="Full Post Address",
            label_msgid='eventslist_label_postalAddress',
            i18n_domain='eventslist',
        ),
    ),
    StringField(
        name='website',
        widget=StringField._properties['widget'](
            label='Website',
            label_msgid='eventslist_label_website',
            i18n_domain='eventslist',
        ),
        validators=('isURL',),
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

    # Manually created methods

    def getShortName(self):
        if self.isTopVenue():
            return self.title
        else:
            return '%s, %s' % (self.title, self.getParentVenue().Title())

    def getFullTitle(self):
        if self.isTopVenue():
            return self.title
        else:
            return '%s - %s' % (self.getParentVenue().Title(), self.title)

    def getLongName(self):
        if self.isTopVenue():
            title = self.title
        else:
            title = '%s, %s' % (self.title, self.getParentVenue().Title())

        title += '<br />'

        if self.getSuburb():
            title = '%s %s' % (title, self.getSuburb())

        if self.getCity():
            if self.getSuburb():
                title = '%s, %s' % (title, self.getCity())
            else:
                title = '%s %s' % (title, self.getCity())

        #if self.getRegion():
        #    title = '%s, %s' % (title, self.getRegion())
        return title

    def getDefaultCountry(self):
        if self.isTopVenue():
            return 'South Africa'
        #otherwise
        return ''

    def getCountry(self):
        country = self.getField('country').get(self)
        if len(country) > 0:
            return country
        parent = getParentVenue(self)
        if parent:
            return parent.getCountry()
        #Otherise
        return ''

    def getDefaultRegion(self):
        if self.isTopVenue():
           return 'Western Cape'
        #otherwise
        return ''

    def getRegion(self):
        region = self.getField('region').get(self)
        if len(region) > 0:
            return region
        parent = getParentVenue(self)
        if parent:
            return parent.getField('region').get(parent)
        #Otherise
        return ''

    def getDefaultSubRegion(self):
        if self.isTopVenue():
            return 'Cape Town'
        #otherwise
        return ''

    def getSubRegion(self):
        subRegion = self.getField('subRegion').get(self)
        if len(subRegion) > 0:
            return subRegion
        parent = getParentVenue(self)
        if parent:
            return parent.getField('subRegion').get(parent)
        #Otherise
        return ''

    def getDefaultCity(self):
        if self.isTopVenue():
            return 'Cape Town'
        #otherwise
        return ''

    def getCity(self):
        city = self.getField('city').get(self)
        if len(city) > 0:
            return city
        parent = getParentVenue(self)
        if parent:
            return parent.getField('city').get(parent)
        #Otherise
        return ''

    def getSuburb(self):
        suburb = self.getField('suburb').get(self)
        if len(suburb) > 0:
            return suburb
        parent = getParentVenue(self)
        if parent:
            return parent.getField('suburb').get(parent)
        #Otherise
        return ''

    def getAddress(self):
        address = self.getField('address').get(self)
        if len(address) > 0:
            return address
        parent = getParentVenue(self)
        if parent:
            return parent.getField('address').get(parent)
        #Otherise
        return ''

    def getPhone(self):
        phone = self.getField('phone').get(self)
        if len(phone) > 0:
            return phone
        parent = getParentVenue(self)
        if parent:
            return parent.getField('phone').get(parent)
        #Otherise
        return ''

    def getLatitude(self):
        if self.get('latitude', False):
            latitude = self.getField('latitude').get(self)
            if len(latitude) > 0:
                return latitude
        parent = getParentVenue(self)
        if parent:
            return parent.getField('latitude').get(parent)
        #Otherise
        return ''

    def getLongitude(self):
        if self.get('longitude', False):
            longitude = self.getField('longitude').get(self)
            if len(longitude) > 0:
                return longitude
        parent = getParentVenue(self)
        if parent:
            return parent.getField('longitude').get(parent)
        #Otherise
        return ''

    def getPostalAddress(self):
        postalAddress = self.getField('postalAddress').get(self)
        if len(postalAddress) > 0:
            return postalAddress
        parent = getParentVenue(self)
        if parent:
            return parent.getField('postalAddress').get(parent)
        #Otherise
        return ''

    def getWebsite(self):
        website = self.getField('website').get(self)
        if len(website) > 0:
            return website
        parent = getParentVenue(self)
        if parent:
            return parent.getField('website').get(parent)
        #Otherise
        return ''

    def isTopVenue(self):
      return not self.getParentVenue()

    def getTopVenue(self):
      top = self
      while top.getParentVenue():
          top = top.getParentVenue()
      return top

    def hasSubVenues(self):
        return len(self.objectIds(spec='Venue')) > 0

    def getSubVenues(self):
        subs = self.objectValues(spec='Venue')
        if len(subs) > 1:
            subs.sort(lambda x, y: cmp(x.Title(), y.Title()))
        return subs

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
            return getParentVenue(obj.aq_parent)
        return getParentVenue(obj.aq_parent)
##/code-section module-footer

