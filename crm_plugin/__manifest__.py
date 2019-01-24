# -*- coding: utf-8 -*-
{
    'name': "CRM Plugin",

    'summary': """Add fields in CRM module""",

    'description': """This module adds some fields to opportunities (CRM module)""",

    'author': "AtomX System",

    'website': "http://atomxsystem.eu",

    'category': 'Tools',

    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['contact_plugin', 'crm'],

    # always loaded
    'data': [
        'views/form_view2.xml',
        'views/kanban_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}