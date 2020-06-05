from odoo import models, fields, api, _


class PatientCardReport(models.Model):
    _name = 'report.our_hospital.report_patient'
    _description='create patient'

    @api.model
    def _get_report_values(self, docids, data=None):
        print("yes entered here in the function")
        print("docids", docids)
        docs = self.env['our.patient'].browse(docids[0])
        appointments = self.env['our.appointment'].search([('patient_id', '=', docids[0])])
        appointment_list = []
        for app in appointments:
            vals = {
                'name': app.name,
                'note': app.note,
                'date': app.date,
                'patient_id': app.patient_id,
                'age': app.age
            }
            appointment_list.append(vals)
        print("appointments", appointments)
        print("appointment_list", appointment_list)
        return {
            'doc_model': 'our.patient',
            'docs': docs,
            'appointment_list': appointment_list,
        }
