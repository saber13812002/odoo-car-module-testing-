from odoo import http
from odoo.http import request


class Hospital(http.Controller):
    @http.route('/hospital/patient/', auth='public', website=True)
    def hospital_patient(self, **kw):
        patients = request.env['our.patient'].sudo().search([])

        return request.render({'patients': patients})
        #return request.render("our_hospital.hospital_patient_page", {'patients': patients})
        # return 'Hello Zaw Naing Linn'

    @http.route('/api/patient', type='json', auth='user')
    def get_project(self):
        print('Yes Get Data')

        project_rec = request.env['our.patient'].search([])
        project = []
        for rec in project_rec:
            vals = {
                'id': rec.id,
                'name': rec.name,
            }
            project.append(vals)
            print(project)
        data = {'status': 200, 'response': project, 'message': 'Success'}
        return data


class Patient(http.Controller):

    @http.route('/ticket_webform/', type="http", auth="public", website=True)
    def ticket_webform(self, **kw):
        patient=request.env['doctor'].sudo().search([])
        return http.request.render('our_hospital.create_ticket', {'patient':patient})

    @http.route('/create/ticket/', tyep="http", auth="public", website=True)
    def create_ticket(self, **kw):

        a=request.env['our.patient'].sudo().create(kw)
        return request.render('our_hospital.patient_thanks', {'a':a})
