# -*- coding: utf-8 -*-
{
    "name": "partner sale lines",
    "version": "1.0",
    "author": "An",
    "license": "AGPL-3",
    "category": 'Sale',
    'website': '',
    'depends': [
        'sale',
    ],
    'external_dependencies': {
        #'python': ['unidecode'],
    },
    'data': [
	#'security/security.xml',
        #'security/ir.model.access.csv',
        'views/res_partner_sale_view.xml',
    ],
    #'post_init_hook': '_assign_invoice_operation_keys',
    'installable': True,
}
