{
    'name' : "HR Analytic Timesheet Line Autogen",
    'version' : "1.0.4",
    'website': 'qarea.com',
    'author' : "Y.Stasovsky, O.Drozdyuk",
    'category' : 'Accounting',
    'depends' : ['hr_attendance', 'hr_timesheet_sheet', 'fortnet'],
    'data' : [
        'data/data.xml',
        'views/hr_view_employee_form_inh.xml',
        'views/fortnet_view_inh.xml'
        ],
    'application': True,
    'installable': True,
    'auto_install': False,
}