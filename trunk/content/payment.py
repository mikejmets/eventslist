# -*- coding: utf-8 -*-
#
# File: payment.py
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

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    ReferenceField(
        name='bookings',
        widget=ReferenceBrowserWidget(
            label='Bookings',
            label_msgid='eventslist_label_bookings',
            i18n_domain='eventslist',
        ),
        allowed_types=('Booking',),
        multiValued=1,
        relationship='payment_booking',
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Payment_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Payment(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IPayment)

    meta_type = 'Payment'
    _at_rename_after_creation = False

    schema = Payment_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(Payment, PROJECTNAME)
# end of class Payment

##code-section module-footer #fill in your manual code here
##/code-section module-footer

