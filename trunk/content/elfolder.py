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

    def getEvents(self, filter=None, reverse=False):
        
        events = self.objectValues(spec='ELEvent')
        filtered = events
        if filter:
            if filter == 'current':
                now = DateTime()
                filtered = [e for e in events if e.getEndDate() >= now]
            elif filter == 'past':
                now = DateTime()
                filtered = [e for e in events if e.getEndDate() < now]

        filtered.sort(
            key=lambda x: x.getStartDate(),
            reverse=reverse)
        return filtered


registerType(ELFolder, PROJECTNAME)
# end of class ELFolder

##code-section module-footer #fill in your manual code here
##/code-section module-footer



