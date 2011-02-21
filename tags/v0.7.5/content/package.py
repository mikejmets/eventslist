# -*- coding: utf-8 -*-
#
# File: package.py
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
from Products.FinanceFields.MoneyWidget import MoneyWidget

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    MoneyField(
        name='unitPrice',
        widget=MoneyWidget(
            label="Unit Cost Price",
            label_msgid='eventslist_label_unitPrice',
            i18n_domain='eventslist',
        ),
        required=1,
    ),
    MoneyField(
        name='earlyBirdRebate',
        widget=MoneyWidget(
            label="Early Bird Rebate",
            label_msgid='eventslist_label_earlyBirdRebate',
            i18n_domain='eventslist',
        ),
    ),
    MoneyField(
        name='lateComerPenalty',
        widget=MoneyWidget(
            label="Late Registration Penalty",
            label_msgid='eventslist_label_lateComerPenalty',
            i18n_domain='eventslist',
        ),
    ),
    MoneyField(
        name='cancellationRebate',
        widget=MoneyWidget(
            label="Cancellation Rebate",
            label_msgid='eventslist_label_cancellationRebate',
            i18n_domain='eventslist',
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Package_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Package(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IPackage)

    meta_type = 'Package'
    _at_rename_after_creation = True

    schema = Package_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(Package, PROJECTNAME)
# end of class Package

##code-section module-footer #fill in your manual code here
##/code-section module-footer

