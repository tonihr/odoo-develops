# -*- coding: utf-8 -*-
{
    "name": "partner purchase lines",
    "version": "8.0.0.1",
    "author": "An",
    "license": "AGPL-3",
    "category": 'Unknow',
    'website': '',
    'depends': [
        'purchase',
    ],
    'external_dependencies': {
        #'python': ['unidecode'],
    },
    'data': [
	#'security/security.xml',
        #'security/ir.model.access.csv',
        'views/res_partner_purchase_view.xml',
    ],
    #'post_init_hook': '_assign_invoice_operation_keys',
    'installable': True,
}
