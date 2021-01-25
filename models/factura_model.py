# -*- coding: utf-8 -*-

from odoo import models, fields, api


class factura_model(models.Model):
    _name = 'tienda_app.factura_model'
    _description = 'Modelo de los facturas'

    name = fields.Char(String = "ref",index= True,required=True)
    fecha = fields.Date(String = "Fecha",index= True,required=True)
    Cliente = fields.Many2one("tienda_app.cliente_model")
    base = fields.Many2one("tienda_app.producto_model")
    iva = fields.Selection(string="IVA", default='21', selection=[('21%','21'),('15%', '15'),('7%', '7'),('0%', '0')], required=True)
    total = fields.Integer(String = "Total precio",index= True,required=True)
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
