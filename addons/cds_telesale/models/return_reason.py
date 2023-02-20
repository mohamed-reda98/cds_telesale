# -*- coding: utf-8 -*-
from odoo import fields, models


class ReturnReason(models.Model):
    _name = 'return.reason'
    _description = 'Return Reason'

    name = fields.Char(string='Return Reason')



    # def change_record_reason(self):
    #     # Add code here
    #     for record in records:
    #         record