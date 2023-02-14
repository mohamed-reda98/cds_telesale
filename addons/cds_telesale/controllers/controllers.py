# -*- coding: utf-8 -*-

##############################################################################
#
#
#    Copyright (C) 2019-TODAY .
#    Author: Eng.Ramadan Khalil (<rkhalil1990@gmail.com>)
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
##############################################################################


from odoo import http

# class ModuleTemplate(http.Controller):
#     @http.route('/module_template/module_template/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module_template/module_template/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module_template.listing', {
#             'root': '/module_template/module_template',
#             'objects': http.request.env['module_template.module_template'].search([]),
#         })

#     @http.route('/module_template/module_template/objects/<model("module_template.module_template"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module_template.object', {
#             'object': obj
#         })