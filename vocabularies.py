from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from Products.CMFCore.utils import getToolByName

def dow_vocabulary(context):
  """Vocabulary with days of the week
  """
  days = ['Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
  terms = []
  for day in days:
    val = days.index(day) + 1
    terms.append(SimpleTerm(value=val, token=str(val), title=day))
  return SimpleVocabulary(terms)

def event_type_vocabulary(context):
  """Vocabulary with event types
  """
  categories = ['Concert', 'Conference', 'Exhibition', 
                'Festival', 'Market', 'Show', 'Sport']
  terms = []
  for cat in categories:
    terms.append(SimpleTerm(value=cat, token=cat, title=cat))
  return SimpleVocabulary(terms)

def venue_vocabulary(context):
  """Vocabulary with event types
  """
  urltool = getToolByName(context, 'portal_url')
  portal = urltool.getPortalObject()
  folder = portal['eventslists-venues']
  #Pull parents
  venues = obs = folder.objectValues(spec='Venue')
  #pull children
  for ob in obs:
    subs = ob.objectValues(spec='Venue')
    if subs:
      venues.extend(subs)
  #sort
  venues.sort(
      lambda x, y: cmp(x.getFullTitle().upper(), y.getFullTitle().upper()))
  #create vocab
  terms = []
  terms.append(SimpleTerm(
      value=0, token=0, title='--Other--'))
  for venue in venues:
    terms.append(SimpleTerm(
      value=venue.UID(), token=venue.UID(), title=venue.getFullTitle()))
  return SimpleVocabulary(terms)



