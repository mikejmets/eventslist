# -*- coding: utf-8 -*-
#
# File: EventsConfiglet.py
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


from Products.CMFCore.utils import UniqueObject

    
##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    TextField(
        name='liabilityClause',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label='Liabilityclause',
            label_msgid='eventslist_label_liabilityClause',
            i18n_domain='eventslist',
        ),
        default_output_type='text/html',
    ),
    TextField(
        name='declarationAndConfirmation',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label='Declarationandconfirmation',
            label_msgid='eventslist_label_declarationAndConfirmation',
            i18n_domain='eventslist',
        ),
        default_output_type='text/html',
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

EventsConfiglet_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
EventsConfiglet_schema['liabilityClause'].default_method='getLiabilityClause'
EventsConfiglet_schema['declarationAndConfirmation'].default_method='getDeclarationAndConfirmation'
##/code-section after-schema

class EventsConfiglet(UniqueObject, BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IEventsConfiglet)

    meta_type = 'EventsConfiglet'
    _at_rename_after_creation = True

    schema = EventsConfiglet_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header


    # tool-constructors have no id argument, the id is fixed
    def __init__(self, id=None):
        BaseContent.__init__(self,'portal_eventsconfiglet')
        self.setTitle('')
        
        ##code-section constructor-footer #fill in your manual code here
        ##/code-section constructor-footer


    # tool should not appear in portal_catalog
    def at_post_edit_script(self):
        self.unindexObject()
        
        ##code-section post-edit-method-footer #fill in your manual code here
        ##/code-section post-edit-method-footer


    # Methods

    # Manually created methods

    def getLiabilityClause(self):
        return """
EventsList or any individual of the Organising Committee of the Workshop, cannot be held responsible for any loss, damage, injury, accident, delay or inconvenience experienced by the attending delegate or guest during their travel or stay. No guarantees of acceptance can be given for late registration or arrival.
        """

    def getDeclarationAndConfirmation(self):
        return """
I / we understand and accept the conditions as given above and agree to pay accordingly.
        """



registerType(EventsConfiglet, PROJECTNAME)
# end of class EventsConfiglet

##code-section module-footer #fill in your manual code here
##/code-section module-footer



