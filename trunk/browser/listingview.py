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

from Products.eventslist.vocabularies \
    import event_type_vocabulary, venue_vocabulary

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
        #if form.get('form.submitted', False):

        return self.index()


    def userCanEdit(self, user):
        context = aq_inner(self.context)
        roles = user.getRolesInContext(context)
        #if user has role
        return 'EventManager' in roles

    def getRegions(self):
        context = aq_inner(self.context)
        pc = getToolByName(self, 'portal_catalog')
        brains = pc.searchResults(portal_type='Venue', review_state="published")
        regions = []
        for brain in brains:
          if brain.getRegion not in regions:
            regions.append(brain.getRegion)

        return regions

    def getEventByUID(self, UID):
        """ fetch an object by uid """
        pc = getToolByName(self, 'portal_catalog')
        brains = pc.searchResults(portal_type='ELEvent', UID=UID)
        if len(brains) == 1 :
            return brains[0].getObject()
        else :
            return None

    def getEventTypeVocab(self):
      vocab = event_type_vocabulary(self).by_value.keys()
      vocab.sort()
      return vocab
        
    def getEvents(self,
           filter=None, region=None, event_type=None, 
           start_date='', end_date='',
           sort_order='ascending', review_state='published'):

        #Using portal catalog
        query = {
            'portal_type': 'ELEvent',
            'isTopEvent': True,
            'sort_on': 'getStartDate',
            'sort_order': sort_order,
            }

        if region != 'all' and region is not None:
          query['getVenueRegion'] = region

        if event_type != 'all' and event_type is not None:
          query['Subject'] = event_type

        if review_state == 'all':
          query['review_state'] = ['submitted', 'published']
        else:
          query['review_state'] = review_state

        if len(start_date) > 0 and len(end_date) > 0:
          #query['getStartDate'] = {'query':[start_date, end_date], 'range':'minmax'}
          start_date_list = start_date.split('/')
          start_date = "%s/%s/%s" % (
              start_date_list[1], start_date_list[0], start_date_list[2])
          end_date_list = end_date.split('/')
          end_date= "%s/%s/%s" % (
              end_date_list[1], end_date_list[0], end_date_list[2])
          query['getStartDate'] = {'query':end_date, 'range':'max'}
          query['getEndDate'] = {'query':start_date, 'range':'min'}
        elif len(start_date) > 0:
          start_date_list = start_date.split('/')
          start_date = "%s/%s/%s" % (
              start_date_list[1], start_date_list[0], start_date_list[2])
          query['getEndDate'] = {'query':start_date, 'range':'min'}
        elif len(end_date) > 0:
          end_date_list = end_date.split('/')
          end_date= "%s/%s/%s" % (
              end_date_list[1], end_date_list[0], end_date_list[2])
          query['getStartDate'] = {'query':end_date, 'range':'min'}
        else:
          if filter == 'current':
            query['getEndDate'] = {'query':DateTime(), 'range':'min'}
          elif filter == 'past':
            query['getEndDate'] = {'query':DateTime(), 'range':'max'}

        logging.info('getEvents: %s' % query)
        pc = getToolByName(self, 'portal_catalog')
        events = pc.searchResults(query)
        return events


