from odoo import models,fields,api

class AppointmentReport(models.Model):
    _name='report.our_hospital.report_appointment'
    _description='Appointment Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        print('kkk',docids,data['form'],['patient_id'])
        print('kkk', docids, data['form'], ['appointment_date'])
        # print("docids", docids)
        # docs = self.env['our.patient'].browse(docids[0])
        appointments = self.env['our.appointment'].search([('patient_id', '=', data['form']['patient_id'][0])])
        # appointment_list = []
        # for app in appointments:
        #     vals = {
        #         'name': app.name,
        #         'note': app.note,
        #         'date': app.date,
        #         'patient_id': app.patient_id,
        #         'age': app.age
        #     }
        #     appointment_list.append(vals)
        print("appointments", appointments)
        # print("appointment_list", appointment_list)
        return {
            'doc_model': 'our.patient',
            'docs': appointments,
            # 'appointment_list': appointment_list,
        }


