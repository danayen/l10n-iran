# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, Command
from odoo.addons.account.models.chart_template import template


class AccountChartTemplate(models.AbstractModel):
    _inherit = 'account.chart.template'

    @template('ir')
    def _get_ir_template_data(self):
        return {
            'property_account_receivable_id': 'ir_account_111411',
            'property_account_payable_id': 'ir_account_211009',
            'property_account_expense_categ_id': 'ir_account_621309',
            'property_account_income_categ_id': 'ir_account_411003',
            'code_digits': '6',
        }

    @template('ir', 'res.company')
    def _get_ir_res_company(self):
        '''sales_tax_xmlid = {
            'AZ': 'uae_sale_tax_5_abu_dhabi',
            'AJ': 'uae_sale_tax_5_ajman',
            'DU': 'uae_sale_tax_5_dubai',
            'FU': 'uae_sale_tax_5_fujairah',
            'RK': 'uae_sale_tax_5_ras_al_khaima',
            'SH': 'uae_sale_tax_5_sharjah',
            'UQ': 'uae_sale_tax_5_umm_al_quwain',
        }.get(self.env.company.state_id.code, 'uae_sale_tax_5_abu_dhabi')
        '''
        return {
            self.env.company.id: {
                'account_fiscal_country_id': 'base.ir',
                'bank_account_code_prefix': '1014',
                'cash_account_code_prefix': '1015',
                'transfer_account_code_prefix': '1017',
                'account_default_pos_receivable_account_id': 'l10n_ir_chart_111411',
                #'income_currency_exchange_account_id': 'uae_account_500011',
                ##'expense_currency_exchange_account_id': 'uae_account_400053',
                #'account_journal_early_pay_discount_loss_account_id': 'uae_account_400071',
                #'account_journal_early_pay_discount_gain_account_id': 'uae_account_500014',
                #'account_sale_tax_id': sales_tax_xmlid,
                #'account_purchase_tax_id': 'uae_purchase_tax_5',
            },
        }
'''
    @template('ir', 'account.journal')
    def _get_ir_account_journal(self):
        """ If UAE chart, we add 2 new journals TA and IFRS"""
        return {
            "tax_adjustment":{
                "name": "Tax Adjustments",
                "code": "TA",
                "type": "general",
                "show_on_dashboard": True,
                "sequence": 1,
            },
            "ifrs16": {
                "name": "IFRS 16",
                "code": "IFRS",
                "type": "general",
                "show_on_dashboard": True,
                "sequence": 10,
            }
        }

    @template('ae', 'account.account')
    def _get_ae_account_account(self):
        return {
            "uae_account_100101": {
                'allowed_journal_ids': [Command.link('ifrs16')],
            },
            "uae_account_100102": {
                'allowed_journal_ids': [Command.link('ifrs16')],
            },
            "uae_account_400070": {
                'allowed_journal_ids': [Command.link('ifrs16')],
            },
        }
'''