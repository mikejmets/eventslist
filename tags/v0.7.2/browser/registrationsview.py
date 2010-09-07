# -*- coding: utf-8 -*-
#
# File: registrationsview.py
#
# Copyright (c) 2010 by Webtide (C)2010
#
# GNU General Public License (GPL)
#

__author__ = """Mike Metcalfe <mike@webtide.co.za>, Jurgen Blignaut <jurgen@webtide.co.za>"""
__docformat__ = 'plaintext'

from zope import interface
from zope import component
from Products.CMFPlone import utils
from Products.Five import BrowserView
from zope.interface import implements
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Acquisition import aq_inner, aq_base
from Products.CMFCore.utils import getToolByName
from zope.component import getMultiAdapter
import logging


class RegistrationsView(BrowserView):
    """
    """

    def __call__(self):
        """ disable the editable border
        """
        self.request.set('disable_border', True)

        return self.index()

    def getBookingWorkflowStates(self):
        """ get the workflow states for the Booking class
        """
        context = aq_inner(self.context)
        result = []
        wft = getToolByName(context, 'portal_workflow')
        chain = wft.getChainForPortalType('Booking')
        for wf_id in chain:
            wf = wft.getWorkflowById(wf_id)
            if wf is not None:
                states = list(wf.states)
                states.reverse()
                result.extend(states)
        return result

    def getEventBookingsInState(self, review_state='submitted'):
        """ retrieve a list of the bookings on the event
            for a specific review state
        """
        event = aq_inner(self.context)

        # get the booking backreferences to this event
        refcat = getToolByName(event, 'reference_catalog')
        references = refcat.getBackReferences(event, 'booking_elevent')
        bookingUIDs = [ref.sourceUID for ref in references]

        # get the bookings that are in the specified review state
        pc = getToolByName(event, 'portal_catalog')
        brains = pc(UID=bookingUIDs,
                    review_state=review_state)
        return [brain.getObject() for brain in brains]
