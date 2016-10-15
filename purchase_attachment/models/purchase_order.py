# -*- coding: utf-8 -*-

from openerp import models, fields, exceptions, api, _

class PurchaseOrder(models.Model):
    
    _inherit ='purchase.order'
    
    attachment_ids= fields.One2many('ir.attachment','partner_id', compute='_get_attachment')
    
    @api.one
    @api.depends('partner_id')
    def _get_attachment(self):
        if self.partner_id:
            attachment_obj=self.env['ir.attachment']
            attach_ids = attachment_obj.search([('partner_id','=',self.partner_id.id)])
            if attach_ids:
                self.attachment_ids= [(6,False,attach_ids.ids)]
            
