# -*- coding: utf-8 -*-
#
# File: agendaitem.py
#
# Copyright (c) 2010 by Webtide (C)2010
# Generator: ArchGenXML Version 2.5
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """Mike Metcalfe <mike@webtide.co.za>, Jurgen Blignaut <jurgen@webtide.co.za>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.eventslist.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    DateTimeField(
        name='itemStarts',
        widget=DateTimeField._properties['widget'](
            label="Start Date and Time",
            label_msgid='eventslist_label_itemStarts',
            i18n_domain='eventslist',
        ),
        required=1,
    ),
    IntegerField(
        name='duration',
        widget=IntegerField._properties['widget'](
            label="Duration in minutes",
            label_msgid='eventslist_label_duration',
            i18n_domain='eventslist',
        ),
        required=1,
    ),
    StringField(
        name='building',
        widget=StringField._properties['widget'](
            label="Building housing the event",
            label_msgid='eventslist_label_building',
            i18n_domain='eventslist',
        ),
    ),
    StringField(
        name='room',
        widget=StringField._properties['widget'](
            label="Room number or name",
            label_msgid='eventslist_label_room',
            i18n_domain='eventslist',
        ),
    ),
    LinesField(
        name='presenters',
        widget=LinesField._properties['widget'](
            label="Presenters",
            label_msgid='eventslist_label_presenters',
            i18n_domain='eventslist',
        ),
        required=1,
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

AgendaItem_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
AgendaItem_schema.changeSchemataForField('description', 'default')
AgendaItem_schema.moveField('description', after='title')
##/code-section after-schema

class AgendaItem(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IAgendaItem)

    meta_type = 'AgendaItem'
    _at_rename_after_creation = True

    schema = AgendaItem_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(AgendaItem, PROJECTNAME)
# end of class AgendaItem

##code-section module-footer #fill in your manual code here
##/code-section module-footer

