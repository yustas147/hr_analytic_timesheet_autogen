# hr_analytic_timesheet_autogen
Generates hr.analytic.timesheet null time records if attendance exists without corresponding timesheet activity

Automatically create timesheet activity hr.analytic.timesheet with 0 time for every day with attendance without 
existing timesheet activity in that day (timesheet period must exist for these dates).

Activity is created using fallback analytic account for this purpose (which is created by this module's data) or using 
predefined analytic account specified on the employee's field analytic_account_id            

            