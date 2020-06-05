
{
    'name':"Hospital",
    'category':"Extra Tools",
    'website':'www.odoo.com',
    'version':"12.0.0.0.12",
    'descriptions':"For Hospital Management",
    'depends':['mail','sale','board','web_timeline','muk_web_searchpanel','web_notify','smile_web_auto_refresh'],
    'data':
        [
        'wizards/create_appointment.xml',
        'views/patient.xml',
        'views/server_action.xml',

        'views/appointment.xml',
        'views/doctor.xml',
        'views/template.xml',
        'views/setting.xml',
        'views/sale_order.xml',
        'views/dashboard.xml',
        'views/create_ticket.xml',
        'security/ir.model.access.csv',
        'report/report.xml',
        'report/patient_card.xml',
        'report/appointment_report.xml',
        'data/sequence.xml',
        # 'data/data.xml',
        'security/security.xml',

        'data/mail_template.xml',
        'data/corn.xml',

        'report/sale_report_inherit.xml',


        ],
    'installable':True,
    'auto_install':False,
    'application':True,

}