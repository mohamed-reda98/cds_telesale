# -*- coding: utf-8 -*-
from odoo import fields, models


class Telesale(models.Model):
    _inherit = 'sale.order'

    is_tele_sale = fields.Boolean(string="TeleSale", default=False)
