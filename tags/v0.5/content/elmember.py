# -*- coding: utf-8 -*-
#
# File: elmember.py
#
# Copyright (c) 2010 by Webtide (C)2010
# Generator: ArchGenXML Version 2.4.1
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

# imports needed by remember
from Products.remember.content.member import BaseMember
from Products.remember.permissions import \
        VIEW_PUBLIC_PERMISSION, EDIT_ID_PERMISSION, \
        EDIT_PROPERTIES_PERMISSION, VIEW_OTHER_PERMISSION,  \
        VIEW_SECURITY_PERMISSION, EDIT_PASSWORD_PERMISSION, \
        EDIT_SECURITY_PERMISSION, MAIL_PASSWORD_PERMISSION, \
        ADD_MEMBER_PERMISSION
from AccessControl import ModuleSecurityInfo
from Products.eventslist.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='salutation',
        widget=SelectionWidget(
            label='Salutation',
            label_msgid='eventslist_label_salutation',
            i18n_domain='eventslist',
        ),
        required=False,
        regfield="True",
        vocabulary=(('Mr', 'Mr'), ('Ms', 'Ms'), ('Mrs', 'Mrs'), ('Miss','Miss'), ('Rev', 'Rev'), ('Hon', 'Hon'), ('Dr', 'Dr'), ('Prof', 'Prof'),),
    ),
    StringField(
        name='firstname',
        widget=StringField._properties['widget'](
            label='Firstname',
            label_msgid='eventslist_label_firstname',
            i18n_domain='eventslist',
        ),
        required=True,
        regfield="True",
    ),
    StringField(
        name='surname',
        widget=StringField._properties['widget'](
            label='Surname',
            label_msgid='eventslist_label_surname',
            i18n_domain='eventslist',
        ),
        required=True,
        regfield="True",
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

ELMember_schema = BaseFolderSchema.copy() + \
    BaseMember.schema.copy() + \
    ExtensibleMetadata.schema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
ELMember_schema['fullname'].regfield = 0
ELMember_schema['fullname'].widget.visible = False
ELMember_schema['wysiwyg_editor'].widget.visible = False
ELMember_schema['portrait'].widget.visible = False
ELMember_schema['make_private'].widget.visible = False
##/code-section after-schema

class ELMember(BaseMember, BrowserDefaultMixin, BaseFolder):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IELMember)

    meta_type = 'ELMember'
    _at_rename_after_creation = True

    schema = ELMember_schema

    base_archetype = BaseFolder

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header


    # A member's __call__ should not render itself, this causes recursion
    def __call__(self, *args, **kwargs):
        return self.getId()
        

    # Methods

    # Manually created methods

    security.declarePublic('getFullname')
    def getFullname(self):
        result = ''
        if self.getFirstname():
            result += self.getFirstname()
        if self.getSurname():
            result += ' ' + self.getSurname()
        if result:
            return result.strip()
        else:
            return self.getId()



registerType(ELMember, PROJECTNAME)
# end of class ELMember

##code-section module-footer #fill in your manual code here
##/code-section module-footer



