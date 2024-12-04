# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Iran - Accounting',
    'website': 'https://www.modoo.ir/',
    #'icon': '/account/static/description/l10n.png',
    'countries': ['ir'],
    'author': 'Tech Receptives',
    'category': 'Accounting/Localizations/Account Charts',
    'description': """
Iran accounting chart and localization.
=======================================================
    """,
    'depends': [
        'base',
        'account',
    ],
    'auto_install': ['account'],
    'data': [
        'data/l10n_ir_data.xml',
        #'data/account_tax_report_data.xml',
        'data/res.bank.csv',
        #'views/report_invoice_templates.xml',
        #'views/account_move.xml',
    ],
    'license': 'LGPL-3',
}
