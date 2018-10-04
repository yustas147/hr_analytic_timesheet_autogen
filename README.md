# hr_analytic_timesheet_autogen
for USERS:

Buttons: 
    Employee form: "Autogenerate Timesheet Activities" -- for this employee ts generating
    Fortnet-> .. backends -> "Autogenerate Timesheet Activities" -- for all employees with backend id ...
        
for TECHs:

Generates hr.analytic.timesheet null time records if attendance exists without corresponding timesheet activity

Automatically create timesheet activity hr.analytic.timesheet with 0 time for every day with attendance without 
existing timesheet activity in that day (timesheet period must exist for these dates).

Activity is created using fallback analytic account for this purpose (which is created by this module's data) or using 
predefined analytic account specified on the employee's field analytic_account_id            

Employee should belong to fortnet users, e.g. he should have fortnet id
            