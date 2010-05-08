# -*- coding: utf-8 -*-
#
# File: kssview.py
#
# Copyright (c) 2010 by Webtide (C)2010
#
# GNU General Public License (GPL)
#

__author__ = """Mike Metcalfe <mike@webtide.co.za>, Jurgen Blignaut <jurgen@webtide.co.za>"""
__docformat__ = 'plaintext'

from kss.core import kssaction
from plone.app.kss.plonekssview import PloneKSSView
from Acquisition import aq_inner
from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from zope.component import getMultiAdapter
from Products.FinanceFields.Money import Money
from DateTime import DateTime


class Calculations(PloneKSSView):

    @kssaction
    def calculateTotal(self):
        """ Calculate and display the event signup cost
        """
        event = aq_inner(self.context)

        # check that we have a logged in member
        portal_state = getMultiAdapter((event, self.request),
                                        name=u'plone_portal_state')
        if portal_state.anonymous():
            return

        # get the tools we need
        rc = getToolByName(event, 'reference_catalog')

        # Get the selections for package and internal and 
        #   external events from the form
        form = self.request.form
        package_uid = form.get('package', None)
        internal_uids = form.get('internal_event', None)
        external_uids = form.get('external_event', None)

        # start with nada
        total = Money(0, 'ZAR')

        # get the base package and add its costs
        if package_uid is not None:
            package = rc.lookupObject(package_uid)
            total += package.getUnitPrice()

            # check for early bird rebates or late registration penalties
            now = DateTime()
            if now <= event.getEarlybirdEndDate():
                total -= package.getEarlyBirdRebate()
            elif now > event.getSignupEndDate() and now <= event.end():
                total += package.getLateComerPenalty()

        # add the optional event costs
        # (I just discovered duck typing!)
        if internal_uids is not None:
            try:
                for uid in internal_uids:
                    evt = rc.lookupObject(uid)
                    total += evt.getItemCost()
            except AttributeError:
                evt = rc.lookupObject(internal_uids)
                total += evt.getItemCost()

        if external_uids is not None:
            try:
                for uid in external_uids:
                    evt = rc.lookupObject(uid)
                    total += evt.getItemCost()
            except AttributeError:
                evt = rc.lookupObject(external_uids)
                total += evt.getItemCost()

        # return the result to the page
        ksscore = self.getCommandSet('core')
        visible = ksscore.getHtmlIdSelector('total_amount_display')
        ksscore.replaceInnerHTML(visible, str(total))
        invisible = ksscore.getHtmlIdSelector('total_amount_hidden')
        ksscore.setAttribute(invisible, 'value', str(total))
