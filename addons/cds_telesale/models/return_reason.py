# -*- coding: utf-8 -*-
from odoo import fields, models


class ReturnReason(models.Model):
    _name = 'return.reason'
    _description = 'Return Reason'

    name = fields.Char(string='Return Reason')
