from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    message = fields.Char(string='Custom Message')

    other_information=fields.Char(string="Information")
