from AccessControl.SecurityInfo import ModuleSecurityInfo
from Products.CMFCore.permissions import setDefaultRoles
    
security = ModuleSecurityInfo('EventsList')
  
security.declarePublic('ManageEvents')
ManageEvents = 'EventsList: Manage Events'
setDefaultRoles(ManageEvents, ('EventManager',))

security.declarePublic('ContributeEvents')
ContributeEvents = 'EventsList: Contribute Events'
setDefaultRoles(ContributeEvents, ('EventContributor',))


