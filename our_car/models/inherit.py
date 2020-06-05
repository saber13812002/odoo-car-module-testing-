from odoo import models, fields


class Inherit(models.Model):
    _inherit = 'our.car'

    car=fields.Char(string="Carrrr")




