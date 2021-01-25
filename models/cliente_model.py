# -*- coding: utf-8 -*-

from odoo import models, fields, api


class clieten_model(models.Model):
    _name = 'tienda_app.cliente_model'
    _description = 'Modelo de los clientes'

    name = fields.Char(String = "Nombre",index= True,required=True)
    dni = fields.Char(String = "Dni",index= True,required=True)
    foto = fields.Binary(String = "Foto",index= True,required=False)
    apellidos = fields.Char(String = "apellidos",index= True,required=True)
    telf = fields.Integer(String = "telefono",index= True,required=True,size="9")
    email = fields.Char(String = "Correo electronico",index= True,required=True)
    factura_id = fields.One2many("tienda_app.factura_model","Cliente")
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
