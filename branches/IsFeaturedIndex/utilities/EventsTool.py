# -*- coding: utf-8 -*-
#
# File: EventsTool.py
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


from Products.CMFCore.utils import UniqueObject

    
##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((


),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

EventsTool_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class EventsTool(UniqueObject, BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IEventsTool)

    meta_type = 'EventsTool'
    _at_rename_after_creation = True

    schema = EventsTool_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header


    # tool-constructors have no id argument, the id is fixed
    def __init__(self, id=None):
        BaseContent.__init__(self,'portal_eventstool')
        self.setTitle('')
        
        ##code-section constructor-footer #fill in your manual code here
        ##/code-section constructor-footer


    # tool should not appear in portal_catalog
    def at_post_edit_script(self):
        self.unindexObject()
        
        ##code-section post-edit-method-footer #fill in your manual code here
        ##/code-section post-edit-method-footer


    # Methods

    security.declarePublic('validateEvent')
    def validateEvent(self, event):
        top = event.getTopEvent()

        errors = []
        #Validate top event first
        """ Contact name requried for bookings
        """
        if hasattr(top, 'terms') and top.terms == False:
          errors.append({'objects': (top,),
            'msg':'You must assent to the terms and conditions of EventsList'})

        if top.isBookable:
            if len(top.contactName) == 0:
                errors.append({'objects': (top,),
                  'msg':'Contact name is required for bookings'})

        """ Contact email requried for bookings
        """
        if top.isBookable:
            if len(top.contactEmail) == 0:
                errors.append({'objects': (top,),
                  'msg':'Contact email is required for bookings'})

        if not top.hasSubEvents():
            """ Start date required for top if no subs exist
            """
            if top.startDate is None:
                errors.append({'objects': (top,),
                  'msg':'event requires a start date '})

            """ End date required for top if no subs exist
            """
            if top.endDate is None:
                errors.append({'objects': (top,),
                  'msg':'event requires a end date '})

            """ Venue required for top if no subs exist
            """
            if len(top.getVenueName()) == 0:
                errors.append({'objects': (top,),
                  'msg':'event requires a venue '})

        #Validate all subevents
        for sub in top.getSubEvents():
            """ Start date required for subs if top doesn't exist
            """
            if sub.startDate is None and top.startDate is None:
                errors.append({'objects': (sub, top,),
                  'msg':'Either top or sub event requires a start date '})

            """ End date required for subs if top doesn't exist
            """
            if sub.endDate is None and top.endDate is None:
                errors.append({'objects': (sub, top,),
                  'msg':'Either top or sub event requires a end date '})

            """ Venue required for subs if top doesn't exist
            """
            if len(top.getVenueName()) == 0 and len(sub.getVenueName()) == 0:
                errors.append({'objects': (sub, top,),
                  'msg':'Either top or sub event requires a Venue '})
        #The End
        return errors


registerType(EventsTool, PROJECTNAME)
# end of class EventsTool

##code-section module-footer #fill in your manual code here
##/code-section module-footer

