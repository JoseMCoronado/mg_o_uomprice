# -*- coding: utf-8 -*-
{
    'name': 'UoM Pricelist for Products',
    'category': 'Sales',
    'author': 'Jose M. Coronado',
    'summary': 'Custom',
    'version': '1.0',
    'description': """
Provides the ability to assign different prices for different product UoM.
        """,
    'depends': ['base','sale'],
    'data': [
        'data/ir_model.xml',
        'data/ir_model_fields.xml',
        'data/ir_ui_view.xml',
        'data/ir_actions_server_automation.xml',
    ],
    'installable': True,
}
