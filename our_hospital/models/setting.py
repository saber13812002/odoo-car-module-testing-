from odoo import models, fields, api, _


class HospitalSetting(models.TransientModel):
    _inherit = 'res.config.settings'

    note = fields.Char(string='Notes')
    module_stock_landed_costs = fields.Boolean(string='STOCK COST')
    module_crm = fields.Boolean(string='CRM')
    product_ids = fields.Many2many('product.product', string='Medicines')

    def set_values(self):
        res = super(HospitalSetting, self).set_values()
        self.env['ir.config_parameter'].set_param('our_hospital.note', self.note)
        print('that is test ', self.product_ids.ids)
        self.env['ir.config_parameter'].set_param('our_hospital.product_ids', self.product_ids.ids)
        return res

    @api.model
    def get_values(self):
        res = super(HospitalSetting, self).get_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()
        notes = ICPSudo.get_param('our_hospital.note')
        product_ids=self.env['ir.config_parameter'].sudo().get_param('our_hospital.product_ids')
        print('product_ids',product_ids)
        res.update(note=notes)
        return res
