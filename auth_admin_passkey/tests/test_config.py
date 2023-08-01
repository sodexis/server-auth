# -*- coding: utf-8 -*-
# Copyright 2019 Therp BV (https://therp.nl)
# License AGPL-3 - See https://www.gnu.org/licenses/agpl-3.0.html
from odoo.tests import common


@common.post_install(True)
class TestConfig(common.TransactionCase):
    def test_set_get_config(self):
        """Test configuration methods."""
        # config_model = self.env["res.config.settings"]
        param_model = self.env["ir.config_parameter"]
        set_param = param_model.set_param
        get_param = param_model.get_param
        
        
        # Set email admin and user to False (and back again).
        set_param("auth_admin_passkey_send_to_admin", False)
        set_param("auth_admin_passkey_send_to_user", False)
        self.assertEqual(
            False,
            get_param(
                "auth_admin_passkey_send_to_admin", False
            ),
        )
        self.assertEqual(
            False,
            get_param(
                "auth_admin_passkey_send_to_user", False
            ),
        )
        set_param("auth_admin_passkey_send_to_admin", True)
        set_param("auth_admin_passkey_send_to_user", True)
        
        self.assertEqual(
            u'True',
            get_param(
                "auth_admin_passkey_send_to_admin"
            ),
        )
        self.assertEqual(
            u'True',
            get_param(
                "auth_admin_passkey_send_to_user"
            ),
        )
