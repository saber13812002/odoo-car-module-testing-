from odoo import models, fields,api,_
from odoo.exceptions import ValidationError




class Car(models.Model):
    _name = 'our.car'
    _description = 'for udemy course testing'

    name = fields.Char(string='Car Name')
    horse_power = fields.Integer(string='Horse Power')
    door_number = fields.Integer(string='Door Numbers')

    driver_id = fields.Many2one('res.partner', string='Driver Name')
    parking_id = fields.Many2one('our.parking', string='Parking')
    feature_id = fields.Many2many('our.feature', string='Feature')
    # That is Compute Fields function in odoo13

    total_speed = fields.Integer(string='Total Speed', compute='get_total_speed')
    random_message = fields.Char(string='Message', compute='say_hello')

   #First Way of sequence
    name_seq = fields.Char(string='CarSS', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code(
                'my.car.sequence') or _('New')

        result = super(Car, self).create(vals)
        return result

    #Second Way of Udemy Course

    car_sequence = fields.Char(string='Sequence')

    @api.model
    def create(self, vals):
        vals['car_sequence'] = self.env['ir.sequence'].next_by_code('car.sequence')
        result = super(Car, self).create(vals)
        return result





    # FOR STATUS BAR FUNCTION  IN ODOO
    status = fields.Selection([('new', 'New'), ("used", 'Used'), ('sold', 'Sold')], string='Status', default='new')

    def say_hello(self):
        self.random_message = 'Hello' + ' ' + self.driver_id.name

    def get_total_speed(self):
        self.total_speed = self.horse_power + 500
        print(self.total_speed)

    #That is the Overide Create Fuction
    @api.model
    def create(self, vals):
        print("That is override create function")
        print("vals", vals)
        print("name", vals["name"])
        if vals["name"] == "abcd":
            vals["name"] = "Hello"
        result = super(Car, self).create(vals)
        return result
    #that is overide write function


    def write(self, vals):
        print("That is override wrie function")

        if vals['horse_power']<10:
            #vals['horse_power'] = 6
            raise ValidationError(_("Horse power must be greate than 10"))
        result = super(Car, self).write(vals)
        return result

    def unlink(self):
        for rec in self:
            if rec.horse_power==12:
                raise ValidationError(_("Remove not possible "))
        result = super(Car, self).unlink()
        return result


    # For STATUS BAR  BUTTON
    def set_car_to_used(self):
        self.status = "used"

    def set_car_to_sold(self):
        self.status = "sold"

    # FOR STATUS SECOND WAY BY ODOO MATES

    def action_used(self):
        for rec in self:
            rec.status = 'used'

    def action_sold(self):
        for rec in self:
            rec.status = 'sold'


class Parking(models.Model):
    _name = 'our.parking'
    _description = 'for car parking'

    name = fields.Char(string='Name')
    car_id = fields.One2many('our.car', 'parking_id', string='Car')


class CarFeature(models.Model):
    _name = 'our.feature'
    _description = 'for car Feature'

    name = fields.Char(string='Name')
    value = fields.Char(string='value')


class ResPartner(models.Model):
    _inherit = 'res.partner'

    #message = fields.Char(string='Custom Message')
    # num1=fields.Integer(string='Hello')
