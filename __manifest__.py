# -*- coding: utf-8 -*-
{
    'name': "user_limit",

    'summary': """
        限制用户数
        """,

    'description': """
        1 创建用户时进行检查, 当超过限制时, 禁止创建
        2 用户管理页面不出现 系统管理 设置, 避免超额授权
        3 apps 菜单隐藏
    """,

    'author': "ccdos@163.com 单雷平",
    'website': "http://www.intoodoo.cn/",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/group.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
