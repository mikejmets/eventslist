# script to automatically create events folder in member's user area

context.plone_log("Post create script running")
elfId = 'myevents'
elfTitle = 'My Events'
context.invokeFactory('ELFolder',id=elfId)
elffolder = getattr(context, elfId)
elffolder.setTitle(elfTitle)
elffolder.reindexObject()

