from AccessControl.SecurityInfo import ModuleSecurityInfo
from Products.CMFCore.permissions import setDefaultRoles
    
security = ModuleSecurityInfo('EventsList')
  
security.declarePublic('Manage Events')
MyPermission = 'EventsList: Manage Events'
setDefaultRoles(MyPermission, ('EventManager',))


