from odoo import api,fields,models

class ProductDetails(models.Model):
    _name = "customer.details"
    description = "customer records"

    name = fields.Char(string="name")