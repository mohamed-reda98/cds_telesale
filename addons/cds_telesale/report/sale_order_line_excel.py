# -*- coding: utf-8 -*-
from odoo import models


class SaleOrderXlsx(models.AbstractModel):
    _name = 'report.cds_telesale.report_saleorder_excel'
    _inherit = 'report.report_xlsx.abstract'
    _description = 'Get Sale Order Lines as Excel.'

    def generate_xlsx_report(self, workbook, data, products):
        print("Hi From Excel Class")
        print(data, products)
        for obj in products:
            report_name = obj.name
            # One sheet by partner
            sheet = workbook.add_worksheet(report_name[:31])
            bold = workbook.add_format({'bold': True})
            sheet.write(0, 0, obj.name, bold)
