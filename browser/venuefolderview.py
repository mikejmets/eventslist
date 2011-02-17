# -*- coding: utf-8 -*-
#
# File: venuefolderview.py
#
# Copyright (c) 2010 by Webtide (C)2010
# Generator: ArchGenXML Version 2.5
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """Mike Metcalfe <mike@webtide.co.za>, Jurgen Blignaut <jurgen@webtide.co.za>"""
__docformat__ = 'plaintext'

##code-section module-header #fill in your manual code here
from Acquisition import aq_inner
import logging
from Products.CMFCore.utils import getToolByName
##/code-section module-header

from zope import interface
from zope import component
from Products.CMFPlone import utils
from Products.Five import BrowserView
from zope.interface import implements
from Products.eventslist.content.venuefolder import VenueFolder
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin


class VenueFolderView(BrowserView):
    """
    """

    ##code-section class-header_VenueFolderView #fill in your manual code here
    ##/code-section class-header_VenueFolderView



    def __call__(self):
        """ disable the editable border
        """
        context = aq_inner(self.context)

        # turn of the editable border
        self.request.set('disable_border', True)

        return self.index()


    def userCanEdit(self, user):
        context = aq_inner(self.context)
        roles = user.getRolesInContext(context)
        #if user has role
        if 'EventManager' in roles or 'EventContributor' in roles:
            #user has local access
            return 'Manager' in roles
        return False


    def getWhere(self, venue):
        """ Contract where from address"""
        where = ""
        if venue.subRegion:
          where += venue.subRegion
        if where and where[-1] != ',':
          where += ', '
        if venue.suburb:
          where += venue.suburb
        if where and where[-2] == ',':
          where = where[:-2]
        return where


    def getVenues(self):
        """ Pull all venues in this folder"""
        context = aq_inner(self.context)
        obs = context.objectValues(spec='Venue')
        obs.sort(lambda x, y: cmp(x.Title().upper(), y.Title().upper()))
        return obs


    def getNextWorkflowActions(self):
        """ get the available workflow actions on the object
        """
        context = aq_inner(self.context)
        wft = getToolByName(context, 'portal_workflow')
        return wft.listActions(object=context)


##code-section module-footer #fill in your manual code here
##/code-section module-footer
