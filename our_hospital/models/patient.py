from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


# # FOR SALE ORDER INHERIT
# class SaleOrderInherit(models.Model):
#     _inherit = "sale.order"
#
#     patient_name = fields.Char(string="Patient Name")


class ResPartners(models.Model):
    _inherit = 'res.partner'
    company_type = fields.Selection(selection_add=[('om', 'zaw naing'), ('my', 'Python')])


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def action_confirm(self):
        print('Odoo Mates')
        res = super(SaleOrderInherit , self).action_confirm()
        return res


    patient_name = fields.Char(string="Patient Name")


class Patient(models.Model):
    _name = "our.patient"
    _description = "for create patient"

    _inherit = ['mail.thread', 'mail.activity.mixin']

    def action_patients(self):
        print('That is action patient')
        return {
            'name': _('Patients Server Action'),
            'domain': [],
            'view_type': 'form',
            'res_model': 'our.patient',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',

        }
    name = fields.Char(string="Name")
    email = fields.Char(string='Email')
    age = fields.Integer(string="Age", track_visibility="always")
    age1 = fields.Float(string='Age2')
    gender = fields.Selection([('male', "Male"), ('female', 'Female'), ], string='Gender')
    image = fields.Binary(string="Image", attachement=True)
    age_group = fields.Selection([('minor', 'Minor'), ('major', 'Major'), ], compute="set_age_group",
                                 string="Age Group", store=True)
    # Domain for a base field
    date = fields.Datetime(string="DateTime", default=fields.Datetime.now)
    active = fields.Boolean(string="Active", default=True)

    note = fields.Text(string="Description")
    user_id = fields.Many2one('res.users', string="PRO")
    name_seq = fields.Char(string='Patient ID', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))
    patient_name_upper = fields.Char(compute='_compute_upper_name', inverse='_inverse_upper_name',
                                     string='Patient Name Upper')
    appointment_count = fields.Integer(string='Appointment', compute='get_appointment_count')

    doctor_gender = fields.Selection([('male', 'Male'), ('female', "Female"), ], default="male",
                                     string="Doctor Gender")
    doctor_id = fields.Many2one('doctor', string='Doctor')

    @api.onchange('doctor_id')
    def set_doctor_gender(self):
        for rec in self:
            if rec.doctor_id:
                rec.doctor_gender = rec.doctor_id.gender

    # FOR AGE GROUP Compute Fields
    @api.depends('age')
    def set_age_group(self):
        for rec in self:
            if rec.age:
                if rec.age < 18:
                    rec.age_group = 'minor'
                else:
                    rec.age_group = 'major'

    # FOR MAKE NEW SEQUENCE
    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code(
                'our.patient.sequence') or _('New')

        result = super(Patient, self).create(vals)
        return result

    # Constraint Fields FOR ERROR MESSAGES
    # for validation error

    @api.constrains('age')
    def check_age(self):
        for rec in self:
            if rec.age <= 5:
                raise ValueError(_("age must be greater than 5"))

    # FOR COMPUTE UPPER AND LOWER FILEDS
    @api.depends('name')
    def _compute_upper_name(self):
        for rec in self:
            rec.patient_name_upper = rec.name.upper() if rec.name else False

    def _inverse_upper_name(self):
        for rec in self:
            rec.name = rec.patient_name_upper.lower() if rec.patient_name_upper else False

    # For Open button appointment
    @api.multi
    def open_patients_appointments(self):
        return {
            'name': _('Appointments'),
            'domain': [('patient_id', '=', self.id)],
            'view_type': 'form',
            'res_model': 'our.appointment',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',

        }

    def get_appointment_count(self):
        count = self.env['our.appointment'].search_count([('patient_id', '=', self.id)])
        self.appointment_count = count

    def action_send_card(self):

        template_id = self.env.ref("our_hospital.patient_card_email_template").id
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)

    @api.model
    def test_cron_job(self):
        print("Hello Python")

    # Name get function is used for name
    @api.multi
    def name_get(self):
        res = []
        for a in self:
            res.append((a.id, '%s - %s' % (a.name_seq, a.name)))
        return res

    # For Button Click for Print Button
    @api.multi
    def print_report(self):
        # Hospital is Project folder name and report_patient_card is pdf report file.xml name id
        return self.env.ref('our_hospital.report_patient_card').report_action(self)

    @api.multi
    def print_report_excel(self):
        return self.env.ref('our_hospital.report_patient_card_xls').report_action(self)
