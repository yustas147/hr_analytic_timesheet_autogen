# -*- coding: utf-8 -*-
from openerp import api, fields, tools, models, _
import logging


_logger = logging.getLogger(__name__)

class fortnet_backend(models.Model):
    _inherit = 'fortnet.backend'

    @api.multi
    def ts_autogen(self):
        emp_env = self.env['hr.employee']
        for inst in self:
            employees = emp_env.search([('fortnet_id','>',0)])
            for emp in employees:
                res = emp.ts_autogen()
                _logger.info('Done for %s: result is %s records' % (unicode(emp.name), unicode(res)))
                
        return True