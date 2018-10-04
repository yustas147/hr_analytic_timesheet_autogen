# -*- coding: utf-8 -*-
from openerp import api, fields, tools, models, _
import logging


_logger = logging.getLogger(__name__)

class hr_employee(models.Model):
    _inherit = 'hr.employee'

    analytic_account_id = fields.Many2one("account.analytic.account", string="Fallback Analytic Account ")
    
    @api.multi
    def get_dates_to_fill(self):
        res = []
        for inst in self:
            att_dates = set([])
            aal_dates = set([])
            
            attendancies = self.env['hr.attendance'].search([('employee_id','=',inst.id), ('sheet_id', '!=', None)])
#            attendancies = self.env['hr.attendance'].search([('employee_id','=',inst.id), ('worked_hours','!=',0), ('sheet_id', '!=', None)])
            for att in attendancies:
                dt = att.name.split()[0]
                att_dates.add(dt)
                
            account_analytic_lines = self.env['account.analytic.line'].search([('user_id','=',inst.user_id.id)])
            for aal in account_analytic_lines:
                aal_dates.add(aal.date)
                    
            # calc set difference to find dates to create timesheet activities for        
            res = att_dates - aal_dates
                
        return sorted(res, reverse=True)
    
    @api.multi
    def get_fallback_analytic_account(self):
        ''' Here is the logic for fallback aacc designation '''
        
        res_model, res_id = self.env['ir.model.data'].get_object_reference('analytic','fallback')
        res = self.env['account.analytic.account'].browse(res_id)
        return res 
    
    @api.multi
    def ts_autogen(self):
        ''' 
            Automatically create timesheet activity hr.analytic.timesheet with 0 time for every day with attendance without 
            existing timesheet activity in that day.
            Activity is created using fallback analytic account for this purpose (which is created by this module's data) or using 
            predefined analytic account specified on the employee's field analytic_account_id
        '''
        
        res = 0
        hr_ats_env = self.env['hr.analytic.timesheet'] 
        
        for inst in self:
            if inst.analytic_account_id:
                pass
            else:
                ''' use fallback analytic account '''
                inst.analytic_account_id = inst.get_fallback_analytic_account()
            dates_to_fill = inst.get_dates_to_fill()
                
            for dt in dates_to_fill:
                hr_ats_env.create({
                                    'name': "autogen",
                                    'journal_id': inst.journal_id.id,
                                    'account_id': inst.analytic_account_id.id,
                                                 'user_id': inst.user_id.id, 
                                                 'unit_amount': 0,
                                                 'date': dt,
                                                 })
                res += 1
            return res
            

