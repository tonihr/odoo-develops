# -*- coding: utf-8 -*-

from openerp import models, fields, exceptions, api, _

class ResPartner(models.Model):
    _inherit='res.partner'
    
    sales_lines_count = fields.Integer(compute='_get_sale_lines_count')
    
    @api.one
    def _get_sale_lines_count(self):
        sale_order_line_obj=self.env['sale.order.line']
        sale_line_ids = sale_order_line_obj.search_count([('order_partner_id','=',self.id)])
        self.sales_lines_count = sale_line_ids