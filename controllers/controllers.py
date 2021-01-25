# -*- coding: utf-8 -*-
# from odoo import http


# class TiendaApp(http.Controller):
#     @http.route('/tienda_app/tienda_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tienda_app/tienda_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tienda_app.listing', {
#             'root': '/tienda_app/tienda_app',
#             'objects': http.request.env['tienda_app.tienda_app'].search([]),
#         })

#     @http.route('/tienda_app/tienda_app/objects/<model("tienda_app.tienda_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tienda_app.object', {
#             'object': obj
#         })
