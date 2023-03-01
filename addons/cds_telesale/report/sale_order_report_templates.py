# -*- coding: utf-8 -*-
from odoo import api, models


class ReportSaleOrderLines(models.AbstractModel):
    _name = 'report.cds_telesale.report_saleorder_with_product_image'
    _description = 'Get Sale Order Lines as PDF.'

    @api.model
    def _get_report_values(self, docids, data=None):
        # sale_order_lines = self.env['sale.order.line'].browse(docids)
        sale_orders = self.env['sale.order'].browse(docids)
        sale_order_lines = sale_orders.mapped('order_line')
        product_ids = sale_order_lines.mapped('product_id')
        product_data = []
        for product in product_ids:
            product_lines = sale_order_lines.filtered(lambda l: l.product_id == product)
            pr_qty = sum([l.product_uom_qty for l in product_lines])
            pr_amount = sum([l.price_subtotal for l in product_lines])
            pr_data = {
                'product': product,
                'qty': pr_qty,
                'amount': pr_amount

            }
            product_data.append(pr_data)

        return {
            'doc_ids': docids,
            'doc_model': self.env['sale.order'],
            'data': data,
            'product_data': product_data,
        }
