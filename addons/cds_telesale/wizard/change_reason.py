# -*- coding: utf-8 -*-
from odoo import fields, models


class ChangeReasonWiz(models.TransientModel):
    _name = 'return.reason.wizard'
    _description = 'Change Reason'

    reason = fields.Many2one(comodel_name="return.reason", string="Return Reason")
