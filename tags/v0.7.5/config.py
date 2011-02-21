# -*- coding: utf-8 -*-
#
# File: eventslist.py
#
# Copyright (c) 2010 by Webtide (C)2010
# Generator: ArchGenXML Version 2.5
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """Mike Metcalfe <mike@webtide.co.za>, Jurgen Blignaut <jurgen@webtide.co.za>"""
__docformat__ = 'plaintext'


# Product configuration.
#
# The contents of this module will be imported into __init__.py, the
# workflow configuration and every content type module.
#
# If you wish to perform custom configuration, you may put a file
# AppConfig.py in your product's root directory. The items in there
# will be included (by importing) in this file if found.

from Products.CMFCore.permissions import setDefaultRoles
from Products.remember.permissions import ADD_MEMBER_PERMISSION
##code-section config-head #fill in your manual code here
VERSION = "0.2 Beta"
##/code-section config-head


PROJECTNAME = "eventslist"

# Permissions
DEFAULT_ADD_CONTENT_PERMISSION = "Add portal content"
setDefaultRoles(DEFAULT_ADD_CONTENT_PERMISSION, ('Manager', 'Owner', 'Contributor'))
ADD_CONTENT_PERMISSIONS = {
    'ELEvent': 'eventslist: Add ELEvent',
    'Booking': 'eventslist: Add Booking',
    'ExternalEvent': 'eventslist: Add ExternalEvent',
    'Payment': 'eventslist: Add Payment',
    'Package': 'eventslist: Add Package',
    'ELFolder': 'eventslist: Add ELFolder',
    'AgendaItem': 'eventslist: Add AgendaItem',
    'InternalEvent': 'eventslist: Add InternalEvent',
    'EventAttendance': 'eventslist: Add EventAttendance',
    'ELMember': ADD_MEMBER_PERMISSION,
    'Venue': 'eventslist: Add Venue',
    'VenueFolder': 'eventslist: Add VenueFolder',
}

setDefaultRoles('eventslist: Add ELEvent', ('Manager', 'EventContributor', 'EventManager'))
setDefaultRoles('eventslist: Add Booking', ('Manager','Owner'))
setDefaultRoles('eventslist: Add ExternalEvent', ('Manager','Owner'))
setDefaultRoles('eventslist: Add Payment', ('Manager','Owner'))
setDefaultRoles('eventslist: Add Package', ('Manager','Owner'))
setDefaultRoles('eventslist: Add ELFolder', ('Manager','Owner'))
setDefaultRoles('eventslist: Add AgendaItem', ('Manager','Owner'))
setDefaultRoles('eventslist: Add InternalEvent', ('Manager','Owner'))
setDefaultRoles('eventslist: Add EventAttendance', ('Manager','Owner'))
setDefaultRoles('eventslist: Add Venue', ('Manager','Owner'))
setDefaultRoles('eventslist: Add VenueFolder', ('Manager','Owner'))

product_globals = globals()

# Dependencies of Products to be installed by quick-installer
# override in custom configuration
DEPENDENCIES = []

# Dependend products - not quick-installed - used in testcase
# override in custom configuration
PRODUCT_DEPENDENCIES = []

##code-section config-bottom #fill in your manual code here
##/code-section config-bottom


# Load custom configuration not managed by archgenxml
try:
    from Products.eventslist.AppConfig import *
except ImportError:
    pass
