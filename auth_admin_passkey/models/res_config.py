# -*- coding: utf-8 -*-
# Copyright (C) 2013-2014 GRAP (http://www.grap.coop)
# @author Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    # Getter / Setter Section
    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        sudo = self.env['ir.config_parameter'].sudo()
        res.update(auth_admin_passkey_send_to_admin=sudo.get_param("auth_admin_passkey.auth_admin_passkey_send_to_admin"),
                auth_admin_passkey_send_to_user=sudo.get_param("auth_admin_passkey.auth_admin_passkey_send_to_user"))
        return res


    @api.multi
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        for config in self:
            config.env['ir.config_parameter'].sudo().set_param("auth_admin_passkey.auth_admin_passkey_send_to_admin", config.auth_admin_passkey_send_to_admin)
            config.env['ir.config_parameter'].sudo().set_param("auth_admin_passkey.auth_admin_passkey_send_to_user", config.auth_admin_passkey_send_to_user)


    auth_admin_passkey_send_to_admin = fields.Boolean(
        string='Send email to admin user.',
        help='When the administrator use his password to login in '
             'with a different account, Odoo will send an email '
             'to the admin user.')

    auth_admin_passkey_send_to_user = fields.Boolean(
        string='Send email to user.',
        help='When the administrator use his password to login in '
             'with a different account, Odoo will send an email '
             'to the account user.')
