# -*- coding: utf-8 -*-
#
# File: elfolderview.py
#
# Copyright (c) 2010 by Webtide (C)2010
#
# GNU General Public License (GPL)
#

__author__ = """Mike Metcalfe <mike@webtide.co.za>, Jurgen Blignaut <jurgen@webtide.co.za>"""
__docformat__ = 'plaintext'

import logging
from DateTime import DateTime
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName

from zope import interface
from zope import component
from Products.CMFPlone import utils
from Products.Five import BrowserView
from zope.interface import implements
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin


class ListingView(BrowserView):
    """
    """

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
        return 'EventManager' in roles


    def getEventByUID(self, UID):
        """ fetch an object by uid """
        pc = getToolByName(self, 'portal_catalog')
        brains = pc.searchResults(portal_type='ELEvent', UID=UID)
        if len(brains) == 1 :
            return brains[0].getObject()
        else :
            return None

    def getEvents(self,
           filter=None, sort_order='ascending', review_state='published'):

        #Using portal catalog
        query = {
            'portal_type':'ELEvent',
            'sort_on': 'getStartDate',
            'sort_order': sort_order,
            }

        if review_state == 'all':
          query['review_state'] = ['submitted', 'published']
        else:
          query['review_state'] = review_state

        if filter == 'current':
          query['getEndDate'] = {'query':DateTime(), 'range':'min'}
        elif filter == 'past':
          query['getEndDate'] = {'query':DateTime(), 'range':'max'}

        logging.info('getEvents: %s' % query)
        pc = getToolByName(self, 'portal_catalog')
        events = pc.searchResults(query)
        return events


