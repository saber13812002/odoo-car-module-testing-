from odoo import models, fields, _


class Doctor(models.Model):
    _name = 'doctor'
    _description = "for create doctor"

    name = fields.Char(string="Doctor Name")
    email = fields.Char(string="Email")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ], string="Gender")
    user_id = fields.Many2one('res.users', string='Related User')
    image = fields.Binary(string="Image", attachement=True)
    # image = fields.Binary(string="Image", attachement=True)
