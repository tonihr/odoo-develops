# -*- coding: utf-8 -*-

from openerp import fields, models, exceptions, api, _

class AccountFollowUp(models.Model):
    _inherit='res.partner'
    
    unreconciled_aml_ids = fields.One2many('account.move.line', 'partner_id',domain=['&', ('reconcile_id', '=', False), '&', 
                            ('account_id.active','=', True), '&', ('account_id.type', 'in', ['receivable','payable']), ('state', '!=', 'draft')] )