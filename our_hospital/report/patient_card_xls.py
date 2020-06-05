from odoo import models


class PatientCardXLS(models.AbstractModel):
    _name = 'report.our_hospital.report_patient_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        print('lines', lines)

        format1 = workbook.add_format({'font_size': 14, 'align': 'vcenter', 'bold': True})
        format3=workbook.add_format({'font_size':14,'align':'vcenter','bold':True,})
        format2 = workbook.add_format({'font_size': 14, 'align': 'vcenter', 'bold': True,'color':'blue' })
        sheet = workbook.add_worksheet('Patient Card')
        sheet.right_to_left()#That function is RTL Format Function
        sheet.write(0, 1, 'Name', format1)
        sheet.write(1, 1, lines.name, format2)
        sheet.write(0, 2, 'Age', format1)
        sheet.write(1, 2, lines.age, format2)
        sheet.write(0,3,'Email',format3)
        sheet.write(1,3,lines.email,format3)
