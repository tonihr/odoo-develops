# -*- coding: utf-8 -*-

from openerp import models, fields, exceptions, api, _

class ResPartner(models.Model):
    _inherit='res.partner'
    
    purchase_lines_count = fields.Integer(compute='_get_purchase_lines_count')
    
    @api.one
    def _get_purchase_lines_count(self):
        purchase_order_line_obj=self.env['purchase.order.line']
        purchase_line_ids = purchase_order_line_obj.search_count([('partner_id','=',self.id)])
        self.purchase_lines_count = purchase_line_ids