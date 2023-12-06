# -*- coding: utf-8 -*-

from odoo.exceptions import ValidationError
from odoo import api, fields, models, _
import ast

class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def create(self, vals):
        # 从ir.config_parameter 读取用户数量限制
        users_counts_limit = self.env["ir.config_parameter"].sudo().get_param('users_counts_limit', '20')
        # 尝试转为整数
        try:
            users_counts_limit = ast.literal_eval(users_counts_limit)
        except Exception:
            users_counts_limit = 20
        # 判断是否是整数
        if not isinstance(users_counts_limit, int):

            users_counts_limit = 20

        existing_users_count = self.env['res.users'].search_count([('share', '=', False)])
        if existing_users_count >= users_counts_limit:
            raise ValidationError(_('User creation is not allowed due to user limit.'))
        return super(ResUsers, self).create(vals)


class GroupsView(models.Model):
    _inherit = 'res.groups'

    @api.model
    def get_application_groups(self, domain):
        # 重载, 隐藏 系统管理 base.group_erp_manager 和系统设置用户组base.group_system, 使得用户页面不能出现无法授权
        group_erp_manager = self.env.ref('base.group_erp_manager', raise_if_not_found=False)
        if (group_erp_manager and
                group_erp_manager.category_id.xml_id == 'base.module_category_administration_administration'):
            domain += [('id', '!=', group_erp_manager.id)]
        group_system = self.env.ref('base.group_system', raise_if_not_found=False)
        if group_system and group_system.category_id.xml_id == 'base.module_category_administration_administration':
            domain += [('id', '!=', group_system.id)]
        return super().get_application_groups(domain)



#  todo: 如果启用了auth_signup模块, 则需要重载res_partner.py
class ResPartner(models.Model):
    _inherit = 'res.partner'

    signup_token = fields.Char(copy=False, groups="base.group_erp_manager,user_limit.groups_super_user")
    signup_type = fields.Char(string='Signup Token Type', copy=False, groups="base.group_erp_manager,user_limit.groups_super_user")
    signup_expiration = fields.Datetime(copy=False, groups="base.group_erp_manager,user_limit.groups_super_user")

