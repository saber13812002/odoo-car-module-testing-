{
    'name':'Car',
    'version':'1.1',
    'summary':'For Udemy Course Testing',
    'description':'',
    'depends':[],
    'data': [
           'views/car.xml',
           'views/parking.xml',
           'security/ir.model.access.csv',
           # WORK FOR ONE SEQUENCE ONLY
           'Data/se.xml',
           'Data/sequence.xml',
           'security/car_security.xml',



            ],
    'demo': [

    ],

    'installable': True,
    'auto_install': False,
    'application':True

}