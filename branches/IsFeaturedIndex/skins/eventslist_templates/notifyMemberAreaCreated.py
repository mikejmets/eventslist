# script to automatically create events folder in member's user area

context.plone_log("Post create script running")
context.plone_log("Create myevents")
elfId = 'myevents'
elfTitle = 'My Events'
context.invokeFactory('ELFolder',id=elfId)
elffolder = getattr(context, elfId)
elffolder.setTitle(elfTitle)
elffolder.reindexObject()

context.plone_log("Create myimages")
fId = 'myimages'
fTitle = 'My Images'
context.invokeFactory('Folder',id=fId)
folder = getattr(context, fId)
folder.setTitle(fTitle)
folder.reindexObject()
wft = context.portal_workflow
wft.doActionFor(folder, 'submit')
