# -*- coding: utf-8 -*-
#
# File: internaleventview.py
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
from Products.CMFCore.utils import getToolByName
from zope.component import getMultiAdapter
##/code-section module-header

from zope import interface
from zope import component
from Products.CMFPlone import utils
from Products.Five import BrowserView
from zope.interface import implements
from Products.eventslist.content.internalevent import InternalEvent
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin


class InternalEventView(BrowserView):
    """
    """

    ##code-section class-header_InternalEventView #fill in your manual code here
    ##/code-section class-header_InternalEventView



    def __call__(self):
        self.request.set('disable_border', True)
        return self.index()


    def userCanEdit(self, user):
        context = aq_inner(self.context)
        roles = user.getRolesInContext(context)
        #if user has role
        if 'EventManager' in roles or 'EventContributor' in roles:
            #user has local access
            return 'Contributor' in roles
        return False


    def getELEventParent(self):
        """ return the containing event
        """
        context = aq_inner(self.context)
        context_state = getMultiAdapter((context, self.request),
                                            name=u"plone_context_state")
        parent = context_state.parent()
        if parent and parent.portal_type == 'ELEvent':
            return parent
        return None


    def getNextWorkflowActions(self):
        """ get the available workflow actions on the object
        """
        context = aq_inner(self.context)
        wft = getToolByName(context, 'portal_workflow')
        return wft.listActions(object=context)


##code-section module-footer #fill in your manual code here
##/code-section module-footer
