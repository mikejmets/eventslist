# -*- coding: utf-8 -*-
#
# File: setuphandlers.py
#
# Copyright (c) 2010 by Webtide (C)2010
# Generator: ArchGenXML Version 2.4.1
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """Mike Metcalfe <mike@webtide.co.za>, Jurgen Blignaut <jurgen@webtide.co.za>"""
__docformat__ = 'plaintext'


import logging
logger = logging.getLogger('eventslist: setuphandlers')
from Products.eventslist.config import PROJECTNAME
from Products.eventslist.config import DEPENDENCIES
import os
from Products.CMFCore.utils import getToolByName
import transaction
##code-section HEAD
from Products.eventslist.content.elfolder import ELFolder
##/code-section HEAD

def isNoteventslistProfile(context):
    return context.readDataFile("eventslist_marker.txt") is None

def setupHideToolsFromNavigation(context):
    """hide tools"""
    if isNoteventslistProfile(context): return 
    # uncatalog tools
    site = context.getSite()
    toolnames = ['portal_eventsconfiglet']
    portalProperties = getToolByName(site, 'portal_properties')
    navtreeProperties = getattr(portalProperties, 'navtree_properties')
    if navtreeProperties.hasProperty('idsNotToList'):
        for toolname in toolnames:
            try:
                portal[toolname].unindexObject()
            except:
                pass
            current = list(navtreeProperties.getProperty('idsNotToList') or [])
            if toolname not in current:
                current.append(toolname)
                kwargs = {'idsNotToList': current}
                navtreeProperties.manage_changeProperties(**kwargs)


from Products.membrane.interfaces import ICategoryMapper
from Products.membrane.utils import generateCategorySetIdForType
from Products.remember.utils import getAdderUtility

def setupMemberTypes(context):
    """Adds our member types to MemberDataContainer.allowed_content_types."""
    if isNoteventslistProfile(context): return 
    site = context.getSite()
    types_tool = getToolByName(site, 'portal_types')
    act = types_tool.MemberDataContainer.allowed_content_types
    types_tool.MemberDataContainer.manage_changeProperties(allowed_content_types=act+('ELMember', ))
    # registers with membrane tool ...
    membrane_tool = getToolByName(site, 'membrane_tool')
    

def updateRoleMappings(context):
    """after workflow changed update the roles mapping. this is like pressing
    the button 'Update Security Setting' and portal_workflow"""
    if isNoteventslistProfile(context): return 
    wft = getToolByName(context.getSite(), 'portal_workflow')
    wft.updateRoleMappings()

def postInstall(context):
    """Called as at the end of the setup process. """
    # the right place for your custom code
    if isNoteventslistProfile(context): return
    site = context.getSite()

    # create the ELFolder to contain ELEvents
    if 'eventslist_folder' not in site.objectIds():
        folder = ELFolder('eventslist_folder')
        site._setObject('eventslist_folder', folder)

        # get the new folder
        folder = site['eventslist_folder']
        folder.setTitle('EventsList Folder')

        # set the view permission on the eventslist folder to Manager and Owner
        folder.manage_permission('View', roles=['Manager', 'Owner'], acquire=0)

        # publish the events folder
        # wft = getToolByName(site, 'portal_workflow')
        # wft.doActionFor(folder, 'publish')

    # do other configuration stuff
    enableMemberSelfRegistration(site)
    setupEventsListOther(site)



##code-section FOOT
def enableMemberSelfRegistration(site):
    # add Anonymous to the 'Add portal member' permission to allow
    # visitors to register as members
    app_perms = site.rolesOfPermission(permission='Add portal member')
    reg_roles = []
    for appperm in app_perms:
        if appperm['selected'] == 'SELECTED':
            reg_roles.append(appperm['name'])
    if 'Anonymous' not in reg_roles:
        reg_roles.append('Anonymous')
    site.manage_permission('Add portal member', roles=reg_roles, acquire=0)

    # Add 'Add Portal Content' permission for Anonymous on portal_memberdata, eina!
    # This is to get around this reported problem:
    # http://www.coactivate.org/projects/remember/lists/remember/archive/2009/07/1249079824818/forum_view
    pmt = getToolByName(site, 'portal_memberdata')
    pmt.manage_permission('Add portal content', roles=['Anonymous'], acquire=1)

    # members have to respond to an email to validate their account
    site.validate_email = True

    # set the default 'remember' member type
    adder = getAdderUtility(site)
    adder.default_member_type = 'ELMember'

    # # # enable member folder creation
    # portal_membership = getToolByName(site, 'portal_membership')
    # portal_membership.memberareaCreationFlag = True


def setupEventsListOther(site):
    # Add ELEvent as a type to be displayed in the Events folder
    # Update the events collection portal types criteria topic with ELEvent
    plone_events_folder = getToolByName(site, 'events')
    if plone_events_folder:
        ptc = plone_events_folder.aggregator.crit__Type_ATPortalTypeCriterion
        if ptc:
            portal_types = [t for t in ptc.Value()]
            if 'ELEvent' not in portal_types:
                portal_types.append('ELEvent')
            ptc.setValue(tuple(portal_types))

    # Add ELEvent as a type to be displayed in the calendar portlet
    ct = getToolByName(site, 'portal_calendar')
    ct.edit_configuration(show_types=('Event', 'ELEvent'),
                          use_session=False, 
                          show_states=('published',),
                          firstweekday=0)

##/code-section FOOT
