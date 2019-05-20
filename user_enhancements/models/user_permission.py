# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see the __manifest__.py file in root directory
##############################################################################

from openerp import models, fields, api


class UserPermission(models.Model):
    """
    Readonly view to show which models the user has permission to view, create, update and delete
    """

    _name = 'user.permission'
    _auto = False

    login = fields.Char("Login", readonly=True)
    group = fields.Char("Group", readonly=True)
    model = fields.Char("Model", readonly=True)
    perm_read = fields.Char('Read', readonly=True)
    perm_create = fields.Char('Create', readonly=True)
    perm_write = fields.Char('Write', readonly=True)
    perm_unlink = fields.Char('Delete', readonly=True)

    @api.model_cr
    def init(self):
        self._cr.execute("""
            CREATE OR REPLACE VIEW user_permission AS (
            SELECT m.id, u.login, concat(group_category.name, ' - ', g.name) AS group, m.model, MAX(CASE WHEN perm_read THEN 1 ELSE 0 END) AS perm_read, MAX(CASE WHEN perm_create THEN 1 ELSE 0 END) AS perm_create, MAX(CASE WHEN perm_write THEN 1 ELSE 0 END) AS perm_write, MAX(CASE WHEN perm_unlink THEN 1 ELSE 0 END) AS perm_unlink
            FROM ir_model_access a
            JOIN ir_model m ON m.id = a.model_id
            JOIN res_groups_users_rel gu ON gu.gid = a.group_id
            JOIN res_users u ON u.id = gu.uid
            LEFT JOIN res_groups g ON g.id = a.group_id
            LEFT JOIN ir_module_category AS group_category ON group_category.id = g.category_id
            WHERE a.active = TRUE
            GROUP BY m.id, u.login, group_category.name, g.name, m.model
            )
        """
        )
