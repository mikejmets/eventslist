# -*- coding: utf-8 -*-
#
# File: venueview.py
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
import logging
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from DateTime.DateTime import DateTime
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



    def userCanEdit(self, user):
        context = aq_inner(self.context)
        roles = user.getRolesInContext(context)
        #if user has role
        if 'EventManager' in roles or 'EventContributor' in roles:
            #user has local access
            return 'Contributor' in roles or 'Manager' in roles
        return False


    def getEvents(self):
        context = self.context
        path = "/".join(context.getPhysicalPath())
        pc = getToolByName(context, 'portal_catalog')
        query = {
            'portal_type':'ELEvent',
            'isTopEvent': True,
            'getVenuePath': {'query': path, 'depth':2},
            'review_state':'published',
            'getEndDate':{'query': DateTime(),
                          'range': 'min'},
            'sort_on':'getStartDate',
            }
        logging.info('getEvents query = "%s"' % query)
        brains = pc.searchResults(query)

        return brains

        """
        tool = getToolByName(context, 'reference_catalog')
        refs = tool.getBackReferences(context, 'elevent_venue')
        subvenues = context.objectValues(spec='Venue')
        for subvenue in subvenues:
            subrefs = tool.getBackReferences(subvenue, 'elevent_venue')
            if subrefs:
              refs.extend(subrefs)
        if not refs:
            return []
        else:
            ids = [r.sourceUID for r in refs]
            pc = getToolByName(context, 'portal_catalog')
            #today = DateTime('2010/06/06')
            #logging.info('TODAY HAS BEEN HACKED!!!!!!!!!!!!!!!!!!!!!!!')
            today = DateTime()
            brains = pc.searchResults(
                portal_type='ELEvent',
                UID=ids,
                review_state='published',
                getEndDate={'query': today,
                            'range': 'min'},
                sort_on='getStartDate',
                )
            return brains
        """


##code-section module-footer #fill in your manual code here
##/code-section module-footer
