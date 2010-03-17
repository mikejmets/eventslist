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
        self.request.set('disable_border', True)

        return self.index()


##code-section module-footer #fill in your manual code here
##/code-section module-footer


