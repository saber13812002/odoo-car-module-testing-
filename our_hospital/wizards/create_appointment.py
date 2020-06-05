from odoo import models, fields, api, _


class CreateAppointment(models.TransientModel):
    _name = "create.appointment"
    _description = "for create appointment"

    patient_id = fields.Many2one("our.patient", string="Patient")
    appointment_date = fields.Date(string="Appointment Date")

    def create_appointment(self):
        vals = {
            'patient_id': self.patient_id.id,
            'Date': self.appointment_date,
            'notes': 'Created From The Wizard/Code'
        }
        # adding a message to the chatter from code
        self.patient_id.message_post(body="Test string ", subject="Appointment Creation")
        # creating appointments from the code

        new_appointment=self.env['our.appointment'].create(vals)
        context=dict(self.env.context)
        #context['form_view_initial_mode']='edit'
        #
        return{
             'type':'ir.actions.act_window',
             'view_type':'form',
             'view_mode':'form',
             'res_model':'our.appointment',
             'res_id':new_appointment.id,
             'context':context

        }

    def print_report(self):
        #print('kkkk',self.read()[0])
        data = {
            'model': 'create.appointment',
            'form': self.read()[0]

        }

        selected_patient=data['form']['patient_id'][0]
        appointment=self.env['our.appointment'].search([('patient_id','=',selected_patient)])
        data['docs']=appointment
        # print('Data', data)
        return self.env.ref('our_hospital.report_appointment').with_context(landscape=True).report_action(self, data=data)

    def get_data(self):
        print("That is Get Data")
        appointments = self.env['our.appointment'].search([('patient_id', '=', 7)])
        print('appointments', appointments)
        for rec in appointments:
            print('Appointment Name', rec.name)

        return {
            'type': 'ir.actions.do_nothing'
        }

    # That is fOR DELETE DATA button use unlink function
    def delete_data(self):
        for rec in self:
            rec.patient_id.unlink()
