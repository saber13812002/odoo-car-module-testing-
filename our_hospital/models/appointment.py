from odoo import models, fields, api, _
import pytz


class Appointment(models.Model):
    _name = "our.appointment"
    _description = "create appointment"

    _inherit = ['mail.thread', 'mail.activity.mixin']

    patient_id = fields.Many2one("our.patient", string='Patient')
    date = fields.Datetime(string="Date", default=fields.Datetime.now)
    # partner_id = fields.Many2one('res.partner', string='Customer')
    # order_id = fields.Many2one('sale.order', string='Sale Order')
    allday = fields.Many2one('calendar.event', string='All Day')
    note = fields.Text(string="Registration Note")
    Date = fields.Date(string="End Date", required=False)
    ammount = fields.Integer(string='Ammount')
    doctor_id = fields.Many2one('doctor', string='Doctor')
    partner_id = fields.Many2one('res.partner', string='Customer')
    order_id = fields.Many2one('sale.order', string='Sale Order')
    age = fields.Integer(string="Age", related="patient_id.age")
    name = fields.Char(string='Appointment ID', required=True, copy=False, readonly=True,
                       index=True, default=lambda self: _('New'))
    appointment_line = fields.One2many("hospital.appointment.lines", 'appointment_id', string="Appointment Lines")
    state = fields.Selection([
        ('draft', "Draft"),
        ('confirm', 'Confirm',),
        ('done', 'Done'),
        ('cancel', 'Cancelled')], string='Status', readonly=True, default='draft')
    doctor_note = fields.Text(string="Doctor Notes")
    pharmacy_note = fields.Text(string="Pharmacy Notes")

    # FOR MAKE NEW SEQUENCE
    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'our.appointment.sequence') or _('New')

        result = super(Appointment, self).create(vals)
        return result

    #FOR USED mapped() and sorted()
    def test_recordset(self):
        for rec in self:
            partners=self.env['res.partner'].search([])
            print('Partners',partners.mapped('email'))
            print('Sorted Partners', partners.sorted(lambda o: o.write_date,reverse=True))
            print('Filtered Partners',partners.filtered(lambda l:not l.customer))



    def delete_lines(self):
        for rec in self:
            print("Time in UTC", rec.date)  # Convert Datetime to UserTimeZone
            user_tz = pytz.timezone(
                self.env.context.get('tz') or self.env.user.tz)  # Convert Datetime to UserTimeZone

            date_today = pytz.utc.localize(rec.date, ).astimezone(user_tz)  # Convert Datetime to UserTimeZone
            print(date_today)
            rec.appointment_line = [(5, 0, 0)]

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'
            return {
                'effect':
                    {
                        'fadeout': 'slow',
                        'message': 'Appointment Confirmed',
                        'type': 'rainbow_man',
                    }
            }

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_notify(self):
        for rec in self:
            rec.doctor_id.user_id.notify_success('Appointment')

    @api.model
    def default_get(self, fields):
        res = super(Appointment, self).default_get(fields)

        print("zaw naing linnn")
        res['patient_id'] = 8
        res['Date'] = 12 / 4 / 2020
        res['note'] = 'Hello computer are simply value or the set of value'
        return res

    # That Onchange function is used for customer and order id
    @api.onchange('partner_id')
    def onchange_partner_id(self):
        for rec in self:
            return {'domain': {'order_id': [('partner_id', '=', rec.partner_id.id)]}}


class HospitalAppointmentLines(models.Model):
    _name = 'hospital.appointment.lines'
    _description = 'Appointment Lines'

    product_id = fields.Many2one('product.product', string='Medicine')
    # That fields is for Widger Handle
    sequence = fields.Integer(string="Sequence")
    product_qty = fields.Integer(string="Quantity")
    appointment_id = fields.Many2one('our.appointment', string='Appointment ID')
