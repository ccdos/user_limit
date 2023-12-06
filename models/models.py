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
