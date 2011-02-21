# -*- coding: utf-8 -*-
#
# File: externalevent.py
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

# additional imports from tagged value 'import'
from Products.FinanceFields.MoneyField import MoneyField

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    DateTimeField(
        name='itemStarts',
        widget=DateTimeField._properties['widget'](
            label="Event Start Time",
            label_msgid='eventslist_label_itemStarts',
            i18n_domain='eventslist',
        ),
        required=1,
    ),
    DateTimeField(
        name='itemEnds',
        widget=DateTimeField._properties['widget'](
            label="Event End Time",
            label_msgid='eventslist_label_itemEnds',
            i18n_domain='eventslist',
        ),
        required=1,
    ),
    MoneyField(
        name='itemCost',
        widget=MoneyField._properties['widget'](
            label='Itemcost',
            label_msgid='eventslist_label_itemCost',
            i18n_domain='eventslist',
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

ExternalEvent_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
ExternalEvent_schema.changeSchemataForField('location', 'default')
ExternalEvent_schema.changeSchemataForField('description', 'default')
##/code-section after-schema

class ExternalEvent(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IExternalEvent)

    meta_type = 'ExternalEvent'
    _at_rename_after_creation = True

    schema = ExternalEvent_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    # Manually created methods

    security.declarePublic('getPackageInfo')
    def getPackageInfo(self):
        """ Return the first available package. There should only be one.
        """
        packages = self.objectValues(spec='Package')
        if packages:
            return packages[0]
        return None



registerType(ExternalEvent, PROJECTNAME)
# end of class ExternalEvent

##code-section module-footer #fill in your manual code here
##/code-section module-footer

