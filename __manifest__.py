# -*- coding: utf-8 -*-
{
    'name': "devecho_odoo_theme_v10",

    'summary': """
        Odoo10 社区版仿企业版主题 兼容手机端自适应""",

    'description': """
        Odoo10 社区版仿企业版主题 兼容手机端自适应
    """,

    'author': "n37r06u3",
    'website': "http://www.devecho.com",

    'category': 'Theme',
    'version': '0.1',

    'depends': ['web'],

    'data': [
        'views/webclient_templates.xml',
    ],
    'qweb': [
        "static/src/xml/*.xml",
    ],
    'sequence': 1,
    'application': True,
}
