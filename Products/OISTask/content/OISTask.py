# File: OISTask.py
#
# Copyright (c) 2006 by []
# Generator: ArchGenXML Version 1.4.1
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content import base
from Products.ATContentTypes.interfaces import IATContentType
from Products.OISTask.config import *
from DateTime.DateTime import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='title',
        widget=StringWidget(
            label="Task Name",
            description="Title of task",
            label_msgid='OISTask_label_title',
            description_msgid='OISTask_help_title',
            i18n_domain='OISTask',
        ),
        required=True,
        accessor="Title",
        searchable=True
    ),

    TextField(
        name='summary',
        widget=TextAreaWidget(
            label="Task Summary",
            description="Description of task",
            rows=2,
            label_msgid='OISTask_label_summary',
            description_msgid='OISTask_help_summary',
            i18n_domain='OISTask',
        ),
        required=True,
        accessor="Summary",
        searchable=True
    ),

    StringField(
        name='customer',
        widget=StringWidget(
            label="Customer Name",
            description="Name of customer related to task",
            label_msgid='OISTask_label_customer',
            description_msgid='OISTask_help_customer',
            i18n_domain='OISTask',
        ),
        required=True,
        default_method="setCustomerText",
        accessor="Customer",
        searchable=True
    ),

    StringField(
        name='location',
        widget=StringWidget(
            label="Customer Location",
            description="Address of customer",
            label_msgid='OISTask_label_location',
            description_msgid='OISTask_help_location',
            i18n_domain='OISTask',
        ),
        required=False,
        accessor="Location",
        searchable=True
    ),

    LinesField(
        name='status',
        widget=MultiSelectionWidget(
            label='Status',
            label_msgid='OISTask_label_status',
            i18n_domain='OISTask',
        ),
        multiValued=1,
        vocabulary=['To Do', 'In Progress', 'Completed']
    ),

    DateTimeField(
        name='date_of_service',
	required=1,
	searchable=1,
        default_method = DateTime,
        widget=CalendarWidget(
            label='Target Date of Completion',
            format="%Y-%m-%d",
	    description=("Date task is expected to be finished."),
            show_hm=False,
            label_msgid='JobTicket_label_date_of_service',
            i18n_domain='JobTicket',
        )
    ),

    StringField(
        name='consultant',
        widget=StringWidget(
            label="Consultant Name",
            description="Name of consultant responsible for this task",
            label_msgid='OISTask_label_consultant',
            description_msgid='OISTask_help_consultant',
            i18n_domain='OISTask',
        ),
        required=True,
        default_method="setConsultantText",
        accessor="Consultant",
        searchable=True
    ),

    TextField(
        name='detail',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="Task Detail",
            description="Additional information about the task",
            label_msgid='OISTask_label_detail',
            description_msgid='OISTask_help_detail',
            i18n_domain='OISTask',
        ),
        required=False,
        searchable=True,
        default_output_type='text/html',
        accessor="Detail"
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

OISTask_schema = schemata.ATContentTypeSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class OISTask(base.ATCTContent):
    __implements__ = (base.ATCTContent.__implements__, IATContentType) 

    meta_type = 'OISTask'
    portal_type = 'OISTask'

    #DKT added 1/4/07 for oistask shortname rename BUT WILL NOT WORK UNTIL OISTask is changed to OISTask per "santized short name" google this
    _at_rename_after_creation = True

    schema = OISTask_schema
    def setCustomerText(self):
        """determines the default text for the 
	    function """
        return self.getFolderWhenPortalFactory().id
 
    def setConsultantText(self):
        """determines the default text for the 
	    function """
        return self.Creator()
    
    def start(self):
        return self.getDate_of_service()

    def end(self):
        return self.getDate_of_service()


    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

registerType(OISTask,PROJECTNAME)
# end of class OISTask

##code-section module-footer #fill in your manual code here
##/code-section module-footer



