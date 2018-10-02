# -*- coding: utf-8 -*-
from openerp import api, fields, tools, models, _
import openerp.addons.decimal_precision as dp
from datetime import datetime
import math
import logging


_logger = logging.getLogger(__name__)

class hr_employee(models.Model):
    _inherit = 'hr.employee'

    do_not_round = fields.Boolean("Do not round")
    
    rounding_method = fields.Selection([('up', "UP"),
                                        ('down', "Down"),
                                        ('round', "5/4")],
                                       string="Rounding Method",
                                       default='round')
    
    rounding = fields.Integer(string='Rounding', default=2)
    
    hr_payslip_line = fields.One2many('hr.payslip.line',
                                      'name',
                                      copy=True)
    compute_per_day = fields.Boolean('Compute Per Day')
    
    @api.multi
    def ts_autogen(self):
        #########################
        for inst in self:
                if inst.do_not_round:
                    return total_val
                
                res = total_val
                r_m = inst.rounding_method
                r = inst.rounding
    
                if r_m == 'up':
                    res = math.ceil(10.0**r*tot_val)
                    res = res / 10.0 ** r
    
                if r_m== 'down':
                    res = math.floor(10.0 ** r * res)
                    res = res / 10.0 ** r
    
                if r_m == 'round':
                    res = round(res, r)
                return res    

