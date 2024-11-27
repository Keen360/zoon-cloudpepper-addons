# -*- coding: utf-8 -*-
{
    'name': "Sprint Odoo Connector",


    'summary': "This module will Connect Odoo partners With Sprint.",

    'description': """
    """,

    'author': "Waqas Ahmad",
    'category': 'contacts',
    'version': '17.0',
    'depends': ['contacts'],
    'data': [
        'security/ir.model.access.csv',
        'security/groups.xml',
        'security/record_rule.xml',
        'views/views.xml',
        'views/templates.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
}

