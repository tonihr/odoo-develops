# -*- coding: utf-8 -*-
{
    "name": "Attachment in purchase order",
    "version": "8.0.0.1",
    "author": "Antonio Hermosilla anherro285@gmail.com",
    "license": "AGPL-3",
    "category": 'Unknow',
    'website': '',
    'depends': [
        'purchase',
        'attachment_preview',
    ],
    'external_dependencies': {
        #'python': ['unidecode'],
    },
    'data': [
	    #'security/security.xml',
        #'security/ir.model.access.csv',
        'views/purchase_view.xml',
    ],
    #'post_init_hook': '_assign_invoice_operation_keys',
    'installable': True,
}
