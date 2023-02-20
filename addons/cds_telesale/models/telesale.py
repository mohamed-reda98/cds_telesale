# -*- coding: utf-8 -*-
from odoo import fields, models


class Telesale(models.Model):
    _inherit = 'sale.order'

    reason = fields.Many2one(comodel_name="return.reason", string="Return Reason" )
    is_tele_sale = fields.Boolean(string="TeleSale", default=False)
