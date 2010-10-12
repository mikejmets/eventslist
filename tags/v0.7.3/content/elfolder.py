# -*- coding: utf-8 -*-
#
# File: elfolder.py
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
from DateTime import DateTime
import logging
##/code-section module-header

schema = Schema((


),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

ELFolder_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class ELFolder(BaseFolder, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IELFolder)

    meta_type = 'ELFolder'
    _at_rename_after_creation = True

    schema = ELFolder_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    # Manually created methods

    def getEvents(self,
           filter=None, sort_order='ascending', review_state='published'):

        #Using portal catalog
        query = {
            'portal_type':'ELEvent',
            'sort_on': 'getStartDate',
            'sort_order': sort_order,
            }

        if review_state == 'all':
          query['review_state'] = ['private', 'submitted', 'published']
        else:
          query['review_state'] = review_state

        if filter == 'current':
          query['getEndDate'] = {'query':DateTime(), 'range':'min'}
        elif filter == 'past':
          query['getEndDate'] = {'query':DateTime(), 'range':'max'}

        logging.info('getEvents: %s' % query)
        events = self.getFolderContents(query)
        return events



registerType(ELFolder, PROJECTNAME)
# end of class ELFolder

##code-section module-footer #fill in your manual code here
##/code-section module-footer



