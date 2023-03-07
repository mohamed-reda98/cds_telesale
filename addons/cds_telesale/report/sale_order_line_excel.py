# -*- coding: utf-8 -*-
import base64
import io

from odoo import models


class SaleOrderXlsx(models.AbstractModel):
    _name = 'report.cds_telesale.report_saleorder_excel'
    _inherit = 'report.report_xlsx.abstract'
    _description = 'Get Sale Order Lines as Excel.'

    def generate_xlsx_report(self, workbook, data, products):
        # products = self.env['sale.order'].search([])
        # sale_orders = self.env['sale.order'].browse(products)
        sale_orders = self.env['sale.order'].browse(products)
        sale_order_lines = products.mapped('order_line')
        product_ids = sale_order_lines.mapped('product_id')
        print("Hi From Excel Class")
        print(data, product_ids)
        row = 1
        bold = workbook.add_format({'bold': True})
        sheet = workbook.add_worksheet()
        # Header
        sheet.write(0, 0, 'Product Image', bold)
        sheet.write(0, 1, 'Product Name', bold)
        sheet.write(0, 2, 'Quantity', bold)
        sheet.write(0, 3, 'Total', bold)
        total_price = 0
        total_qty = 0
        for obj in product_ids:
            # report_name = obj.name
            # One sheet by partner
            product_lines = sale_order_lines.filtered(lambda l: l.product_id == obj)
            pr_qty = sum([l.product_uom_qty for l in product_lines])
            pr_amount = sum([l.price_subtotal for l in product_lines])
            total_price += pr_amount
            total_qty += pr_qty
            # for line in pr_amount:
            #     total_price += line
            #     print(total_price)

            # total_sum = sum([l.price_subtotal for l in product_lines])
            pr_data = {
                'product': obj,
                'qty': pr_qty,
                'amount': pr_amount,
            }

            if obj.image_128:
                product_image = io.BytesIO(base64.b64decode(obj.image_128))
                sheet.insert_image(row, 0, "image.png", {'image_data': product_image, 'x_scale': 0.5, 'y_scale': 0.5}, )
                row += 3
            # sheet.write(row, 0, pr_data['product'].display_name)
            sheet.write(row, 1, pr_data['product'].name)
            # sheet.write(row, 1, pr_data['qty'])
            sheet.write(row, 2, pr_data['qty'])
            sheet.write(row, 3, pr_data['amount'])
            row += 2

        sheet.write(row, 3, total_price, bold)
        sheet.write(row, 2, total_qty, bold)
        sheet.write(row, 0, 'Totals', bold)

        # print(data, product_ids.name)

        # sheet.write(0, 0, obj.name, bold)
        # sheet.write(0, 0, obj.user_id, bold)
