# Restrict normal users to add any content 

member = context.portal_membership.getAuthenticatedMember()
notAddableTypes = ['Favorite']
if not member or not member.has_role('Manager'):
  user_list = ['ELFolder', 'VenueFolder', 'CalendarXFolder', 
               'Document', 'Event', 'File', 'Link', 'NewsItem',
               'Folder']
  notAddableTypes.extend(user_list)

return notAddableTypes
