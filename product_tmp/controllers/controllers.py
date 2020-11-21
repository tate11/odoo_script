# -*- coding: utf-8 -*-
# from odoo import http


# class ProductTmp(http.Controller):
#     @http.route('/product_tmp/product_tmp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_tmp/product_tmp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_tmp.listing', {
#             'root': '/product_tmp/product_tmp',
#             'objects': http.request.env['product_tmp.product_tmp'].search([]),
#         })

#     @http.route('/product_tmp/product_tmp/objects/<model("product_tmp.product_tmp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_tmp.object', {
#             'object': obj
#         })
