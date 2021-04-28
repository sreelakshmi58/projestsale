{
    'name': 'Saleorder',
    'version': '13.0.1.2.2',
    'category': 'sale',
    'summary': 'Sale Order',
    'sequence': '10',
    'author': 'Odoo Mates, Odoo SA',
    'license': 'LGPL-3',

    'demo': [],
    'data': [
        'views/details_view.xml',
        'views/product_view.xml',
        'views/productsale_view.xml',
        'security/ir.model.access.csv',
        'report/report.xml',
        'report/sales_report.xml',

    ],

    'installable': True,
    'application': True,
    'auto_install': False,

}

