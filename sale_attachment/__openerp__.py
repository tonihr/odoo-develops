# -*- coding: utf-8 -*-
{
    "name": "Attachment in sale order",
    "version": "8.0.0.1",
    "author": "An",
    "license": "AGPL-3",
    "category": 'Unknow',
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
        'views/sale_view.xml',
    ],
    #'post_init_hook': '_assign_invoice_operation_keys',
    'installable': True,
}