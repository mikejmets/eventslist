# -*- coding: utf-8 -*-
#
# File: wfsubscribers.py
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


def isValid(obj, event):
    """generated workflow subscriber."""
    # do only change the code section inside this function.
    if not event.transition \
       or event.transition.id not in ['submit', 'publish'] \
       or obj != event.object:
        return
    ##code-section isValid #fill in your manual code here
    ##/code-section isValid



##code-section module-footer #fill in your manual code here
##/code-section module-footer

