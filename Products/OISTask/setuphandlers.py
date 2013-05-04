from Products.CMFCore.utils import getToolByName
from Products.OISTask import config

def setupVarious(context):
    """ Setup preferred default_member_type """
    if context.readDataFile('oistask-setup-plugins.txt') is None:
        return
    portal = context.getSite()
