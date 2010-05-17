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
    def __call__(self):
        """ Handle the form submissions
            * edit venue
        """
        # get the context
        context = aq_inner(self.context)

        # turn of the editable border
        self.request.set('disable_border', True)

        form = self.request.form
        if form.get('form.submitted', False):
            save_edit_button = form.get('form.button.save_edit', None) is not None
            post_back = False

            if save_edit_button:

                if post_back:
                    self.request.set('input_errors',
                                    u'Please correct the errors indicated below')
                else:
                    # save edited values 
                    for key in form.keys():
                        field = context.getField(key)
                        if field and field.mode == 'rw':
                            #logging.info('Set %s to %s' % (key, form[key]))
                            field.getMutator(context)(form[key])
                    context.update()
                    context.reindexObject()
                    self.request.response.redirect(context.absolute_url() + "/view")
                    return ''

        # return the page if the form has not been submitted,
        # or there were errors on the form
        #self.request.response.redirect(context.absolute_url() + "/view")
        return self.index()


    ##/code-section class-header_VenueView



##code-section module-footer #fill in your manual code here
##/code-section module-footer


