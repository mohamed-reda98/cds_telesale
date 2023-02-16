# -*- coding: utf-8 -*-
{
    'name': "Telesales",
    'summary': """ Telesales Module
    """,
    'description': """
    Telesales for orders and Quotations and Sale Orders
    """,
    'author': "CDS Solutions SRL",
    'website': "www.cdsegypt.com",
    'contributors': [
        'Ramadan Khalil <rkhalil1990@gmail.com>',
        'Mohamed Reda <mohamed_reda741@gmail.com>',
    ],
    'version': '0.1',
    'depends': ['base', 'sale'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/menu.xml',
        'views/telesale.xml',
        'views/orderline.xml',
    ],
    "pre_init_hook": None,
    "post_init_hook": None,
}
