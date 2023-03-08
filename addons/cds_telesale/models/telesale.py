# -*- coding: utf-8 -*-
from odoo import fields, models


class Telesale(models.Model):
    _inherit = 'sale.order'

    reason = fields.Many2one(comodel_name="return.reason", string="Return Reason")
    is_tele_sale = fields.Boolean(string="TeleSale", default=False)

    def calling_wizard_change_reason(self):
        # return self.env.ref('cds_telesale.change_reason_action')
        ctx = dict(self.env.context)
        ctx.update({'active_ids': self.ids})

        action = self.env["ir.actions.actions"]._for_xml_id('cds_telesale.change_reason_action')

        action['context'] = ctx
        return action

        # action = self.env["ir.actions.actions"]._for_xml_id('cds_telesale.test_wizard_view_action')
        # return {
        #     'name': 'Change Reason new',
        #     'type': 'ir.actions.act_window',
        #     'res_model': 'return.reason.wizard',
        #     'view_mode': 'form',
        #     'target': 'new',
        # }
