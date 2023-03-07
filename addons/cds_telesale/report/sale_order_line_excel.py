# -*- coding: utf-8 -*-
import base64
import io
from datetime import datetime

from odoo import models


class SaleOrderXlsx(models.AbstractModel):
    _name = 'report.cds_telesale.report_saleorder_excel'
    _inherit = 'report.report_xlsx.abstract'
    _description = 'Get Sale Order Lines as Excel.'

    def add_company_data(self, company, sheet, workbook):
        company_name = company.name
        if company.logo:
            image_data = io.BytesIO(base64.b64decode(company.logo))
            sheet.insert_image(0, 0, "logo.png",
                               {'image_data': image_data, 'x_scale': .5, 'y_scale': .5, }, )
            sheet.write(1, 0, company_name)
            sheet.set_row(0, 80)
            sheet.set_column(0, 0, 20)
            format_date = workbook.add_format({'num_format': 'd mmm yyyy hh:mm AM/PM'})
            time_now = datetime.now()
            sheet.write(2, 0, time_now, format_date)

    def generate_xlsx_report(self, workbook, data, products, ):
        # products = self.env['sale.order'].search([])
        # sale_orders = self.env['sale.order'].browse(products)
        bold = workbook.add_format({'bold': True})
        sheet = workbook.add_worksheet()
        company = self.env.company
        self.add_company_data(company, sheet, workbook)
        sale_orders = self.env['sale.order'].browse(products)
        sale_order_lines = products.mapped('order_line')
        product_ids = sale_order_lines.mapped('product_id')
        print("Hi From Excel Class")
        print(data, product_ids)
        row = 4

        # body
        sheet.set_column(3, 6, 25)
        # sheet.set_row(3, 80)
        sheet.write(3, 3, 'Product Image', bold)
        sheet.write(3, 4, 'Product Name', bold)
        sheet.write(3, 5, 'Quantity', bold)
        sheet.write(3, 6, 'Total', bold)

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
                sheet.insert_image(row, 3, "image.png",
                                   {'image_data': product_image, 'x_scale': 0.5, 'y_scale': 0.5, }, )

            # sheet.write(row, 0, pr_data['product'].display_name)
            sheet.write(row, 4, pr_data['product'].name)
            # sheet.write(row, 1, pr_data['qty'])
            sheet.write(row, 5, pr_data['qty'])
            sheet.write(row, 6, pr_data['amount'])
            sheet.set_row(row, 60)
            row += 1

        sheet.write(row, 6, total_price, bold)
        sheet.write(row, 5, total_qty, bold)
        sheet.write(row, 3, 'Totals', bold)

        # print(data, product_ids.name)

        # sheet.write(0, 0, obj.name, bold)
        # sheet.write(0, 0, obj.user_id, bold)
