# -*- coding: utf-8 -*-
{
    'name': "user_limit",

    'summary': """
        限制用户数
        """,

    'description': """
        创建用户时进行检查, 当超过20时, 禁止创建
    """,

    'author': "ccdos@163.com 单雷平",
    'website': "http://www.intoodoo.cn/",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
