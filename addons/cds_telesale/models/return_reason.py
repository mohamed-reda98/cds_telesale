# -*- coding: utf-8 -*-
from odoo import fields, models


class ReturnReason(models.Model):
    _name = 'return.reason'
    _description = 'Return Reason'

    name = fields.Char(string='Return Reason')

    # def action_open_wizard_change_reason(self):
    #     action = {
    #         "name": "Change Reason",
    #         "type": "ir.actions.act_window",
    #         "res_model": "sale.order",
    #         "views": [[self.env.ref('cds_telesale.change_reason_action').id, "form"]],
    #         # "res_id": self.id,
    #     }
    #     return action

