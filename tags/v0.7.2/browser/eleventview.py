# -*- coding: utf-8 -*-
#
# File: eleventview.py
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
from Acquisition import aq_inner
from DateTime import DateTime
from Products.CMFCore.utils import getToolByName
from zope.component import getMultiAdapter
from Products.FinanceFields.Money import Money
import logging
##/code-section module-header

from zope import interface
from zope import component
from Products.CMFPlone import utils
from Products.Five import BrowserView
from zope.interface import implements
from Products.eventslist.content.elevent import ELEvent
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin


class ELEventView(BrowserView):
    """
    """

    ##code-section class-header_ELEventView #fill in your manual code here
    ##/code-section class-header_ELEventView



    def userCanEdit(self, user):
        context = aq_inner(self.context)
        roles = user.getRolesInContext(context)
        logging.info('Folder: user has roles: %s' % roles)
        #if user has role
        if 'EventManager' in roles or 'EventContributor' in roles:
            #user has local access
            return 'Contributor' in roles
        return False


    def getSubEvents(self):
        """ get the available workflow actions on the object
        """
        context = aq_inner(self.context)
        return context.getSubEvents()


    def listPackages(self):
        """ list the event packages
        """
        event = aq_inner(self.context)
        pc = getToolByName(event, 'portal_catalog')
        brains = pc(portal_type='Package',
                    review_status='published',
                    path='/'.join(event.getPhysicalPath()))
        return [item.getObject() for item in brains]


    def getEventParent(self):
        """ check if this instance is a sub-event of a event
        """
        context = aq_inner(self.context)
        context_state = getMultiAdapter((context, self.request),
                                            name=u"plone_context_state")
        parent = context_state.parent()
        if parent and parent.portal_type == 'ELEvent':
            return parent
        return None


    def eventIsValid(self):
        """ test if event is valid
        """
        context = aq_inner(self.context)
        et = getToolByName(context, 'portal_eventstool')
        return len(et.validateEvent(event=context)) == 0


    def listAgendaItems(self):
        """ list the event agenda items
        """
        event = aq_inner(self.context)
        pc = getToolByName(event, 'portal_catalog')
        brains = pc(portal_type='AgendaItem',
                    path='/'.join(event.getPhysicalPath()),
                    sort_on='getItemStarts')
        return [item.getObject() for item in brains]


    def getNextWorkflowActions(self):
        """ get the available workflow actions on the object
        """
        context = aq_inner(self.context)
        wft = getToolByName(context, 'portal_workflow')
        return wft.listActions(object=context)


    def __call__(self):
        """ Handle the form submissions
            * sign up
            * add event
        """
        # get the context
        context = aq_inner(self.context)

        # turn of the editable border
        self.request.set('disable_border', True)

        # check if the sign up form has been submitted
        form = self.request.form
        if form.get('form.submitted', False):
            sign_up_button = form.get('form.button.SignUp', None) is not None
            add_sub_event_button = \
                form.get('form.button.AddSubEvent', None) is not None

            post_back = False

            if sign_up_button:
                # check that the disclaimer was accepted
                if not form.get('accept_disclaimer', False):
                    self.request.set('disclaimer_error', u'Please accept the disclaimer')
                    post_back = True

                # check that at least a package linked to the main event has been checked
                package = form.get('package', '')
                if not package:
                    self.request.set('package_error', u'Please select a pacakage')
                    post_back = True

                if post_back:
                    self.request.set('input_errors',
                                    u'Please correct the errors indicated below')
                else:
                    # get the logged in member
                    mt = getToolByName(context, 'portal_membership')
                    member = mt.getAuthenticatedMember()
                    #find the member's event attendance object
                    if 'event_attendance' not in member.objectIds():
                        member.invokeFactory('EventAttendance', 'event_attendance', \
                                title='Attendance Attributes and Bookings')
                    event_prefs = member['event_attendance']

                    # create the event booking
                    rid = event_prefs.generateUniqueId('Booking')
                    event_prefs.invokeFactory('Booking', rid)
                    booking = getattr(event_prefs, rid)
                    booking.setTitle(context.Title())
                    booking.setElevents(context.UID())
                    booking.setElmembers(member.UID())

                    # set the references to the optional events
                    # the member is signing up for
                    booking.setPackages(package)
                    internal_events = form.get('internal_event',[])
                    booking.setInternalevents(internal_events)
                    external_events = form.get('external_event', [])
                    booking.setExternalevents(external_events)
                    total_cost = form.get('total_amount', 'R 0.00')
                    logging.info('Total cost on form: %s', total_cost)
                    booking.setTotalCost(Money(total_cost, 'ZAR'))
                    logging.info('Booking total cost: %s', booking.getTotalCost())

                    booking.reindexObject()
                    logging.info('After reindex total cost: %s', booking.getTotalCost())

                    # redirect the member to capture their personal details
                    self.request.response.redirect(booking.absolute_url() + "/edit")
                    return ''

            if add_sub_event_button:
                # check that the disclaimer was accepted
                if not form.get('event_title', False):
                    self.request.set(
                        'event_title', u'Title is required')
                    post_back = True
                if not form.get('event_start_date', False):
                    self.request.set(
                        'event_start_date', u'Start date is required')
                    post_back = True
                if not form.get('event_end_date', False):
                    self.request.set(
                        'event_end_date', u'End date is required')
                    post_back = True
                if post_back:
                    self.request.set('input_errors',
                                u'Please correct the errors indicated below')
                    return ''
                else:
                    # create the subevent
                    rid = context.generateUniqueId('ELEvent')
                    context.invokeFactory('ELEvent', rid)
                    sub = getattr(context, rid)
                    sub.setTitle(form.get('event_title'))
                    sub.setStartDate(form.get('event_start_date'))
                    sub.setEndDate(form.get('event_end_date'))
                    sub.reindexObject()
                    return self.index()

        # return the page if the form has not been submitted,
        # or there were errors on the form
        return self.index()


    def getReviewState(self):
        """ get the current workflow state of the object
        """
        context = aq_inner(self.context)
        wft = getToolByName(context, 'portal_workflow')
        state = wft.getInfoFor(context, 'review_state')
        return "%s%s:" % (state[0].upper(), state[1:])


    def validate_event(self):
        """ get the available workflow actions on the object
        """
        context = aq_inner(self.context)
        et = getToolByName(context, 'portal_eventstool')
        return et.validateEvent(event=context)


##code-section module-footer #fill in your manual code here
##/code-section module-footer


