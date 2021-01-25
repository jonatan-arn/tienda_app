# -*- coding: utf-8 -*-

from odoo import models, fields, api


class producto_model(models.Model):
    _name = 'tienda_app.producto_model'
    _description = 'Modelo de los productos'

    name = fields.Char(String = "Nombre",index= True,required=True)
    description = fields.Char(String = "Descripcion",index= True,required=True)
    pvp = fields.One2many("tienda_app.factura_model","base")
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
