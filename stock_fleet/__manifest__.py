# -*- coding: utf-8 -*-
{
    'name': "Stock Fleet",

    'summary': """
        Link Stock with Fleet""",

    'description': """
        Add vehicles and drivers assignation on Picking Orders and waves. These Statistics can also be accessed directly from the vehicle view.
    """,

    'author': "BADEP",
    'website': "https://badep.ma",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '16.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['stock', 'fleet'],
    'images': ['static/src/img/banner.png'],
    'license': 'AGPL-3',

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/stock_view.xml',
        'views/fleet_view.xml',
    ],
    'installable': False,
    'price': 29.00,
    'currency': 'EUR',
}