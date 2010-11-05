# -*- coding: utf-8 -*-
#
# File: elfolderview.py
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
##/code-section module-header

from zope import interface
from zope import component
from Products.CMFPlone import utils
from Products.Five import BrowserView
from zope.interface import implements
from Products.eventslist.content.elfolder import ELFolder
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin


class ELFolderView(BrowserView):
    """
    """

    ##code-section class-header_ELFolderView #fill in your manual code here
    ##/code-section class-header_ELFolderView



    def __call__(self):
        """ disable the editable border
        """
        context = aq_inner(self.context)

        # turn of the editable border
        self.request.set('disable_border', True)

        # check if the sign up form has been submitted
        form = self.request.form
        if form.get('form.submitted', False):

            post_back = False
            count = 0
            for k in form.keys():
                obj = self.getEventByUID(k)
                if obj:
                    count += 1
                    logging.info('%s %s' % (obj.Title(), form[k]))
                    subjects = form[k]
                    obj.setSubject(subjects)
                else:
                    logging.info('=========NOT FOUND %s' % (k))
            logging.info('Found %s events' % (count))

        return self.index()


    def userCanEdit(self, user):
        context = aq_inner(self.context)
        roles = user.getRolesInContext(context)
        #if user has role
        if 'EventManager' in roles or 'EventContributor' in roles:
            #user has local access
            return 'Contributor' in roles
        return False


    def getEventByUID(self, UID):
        """ fetch an object by uid """
        pc = getToolByName(self, 'portal_catalog')
        bs = pc.searchResults(portal_type='ELEvent', UID=UID)
        if len(bs) == 1 :
            return bs[0].getObject()
        else :
            return None


##code-section module-footer #fill in your manual code here
##/code-section module-footer


