# -*- coding: utf-8 -*-
from odoo import fields, models


class Telesale(models.Model):
    _inherit = 'sale.order'

    reason = fields.Many2one(comodel_name="return.reason", string="Return Reason")
    is_tele_sale = fields.Boolean(string="TeleSale", default=False)

    def calling_wizard_change_reason(self):
        # return self.env.ref('cds_telesale.change_reason_action')
        return {
            'name': 'Change Reason',
            'type': 'ir.actions.act_window',
            'res_model': 'return.reason.wizard',
            'view_mode': 'form',
            'target': 'new',
        }
