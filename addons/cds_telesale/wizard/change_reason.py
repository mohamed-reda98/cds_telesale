# -*- coding: utf-8 -*-
from odoo import fields, models


class ChangeReasonWiz(models.TransientModel):
    _name = 'return.reason.wizard'
    _description = 'Change Reason'

    reason = fields.Many2one(comodel_name="return.reason", string="Return Reason")

    def change_reason_apply(self):
        records = self.env['sale.order'].browse(self.env.context.get('active_ids', []))

        # print(records)
        for record in records:
            record.reason = self.reason

        # .update({'name': self.reason.id})
        # return True
        # self.env['crm.lead'].browse(self.env.context.get('active_ids'))
        #     def change_reason_apply(self):
        # records = self.env['sale.order'].browse(self._context.get("active_ids"))
        #     # .update({'reason': self.reason})
