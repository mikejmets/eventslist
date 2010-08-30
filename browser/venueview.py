# -*- coding: utf-8 -*-
#
# File: venueview.py
#
# Copyright (c) 2010 by Webtide (C)2010
# Generator: ArchGenXML Version 2.4.1
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """Mike Metcalfe <mike@webtide.co.za>, Jurgen Blignaut <jurgen@webtide.co.za>"""
__docformat__ = 'plaintext'

##code-section module-header #fill in your manual code here
import logging
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from DateTime import DateTime
##/code-section module-header

from zope import interface
from zope import component
from Products.CMFPlone import utils
from Products.Five import BrowserView
from zope.interface import implements
from Products.eventslist.content.venue import Venue
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin


class VenueView(BrowserView):
    """
    """

    ##code-section class-header_VenueView #fill in your manual code here
    ##/code-section class-header_VenueView



    def getEvents(self):
        context = self.context
        tool = getToolByName(context, 'reference_catalog')
        refs = tool.getBackReferences(context, 'elevent_venue')
        if not refs:
            return []
        else:
            wft = getToolByName(context, 'portal_workflow')
            current = []
            for ref in refs:
                event = ref.getSourceObject()
                if wft.getInfoFor(event, 'review_state') == 'published' \
                    and event.getEndDate() > DateTime():
                   current.append(event)
            return current


##code-section module-footer #fill in your manual code here
##/code-section module-footer


