# Part of jshp-odoo. See LICENSE file for full copyright and licensing details.

import base64

from odoo import api, fields, models
from odoo.tools import file_open


class ResUsers(models.Model):
    _inherit = "res.users"

    odoobot_state = fields.Selection(string="JSHPBot Status")

    @api.model
    def _apply_jshp_bot_logo(self):
        bot = self.env.ref("base.partner_root")
        params = self.env["ir.config_parameter"].sudo()
        prefix = "jshp_bot_branding."
        # Keep the original across upgrades, including an originally empty image.
        if params.get_param(prefix + "original_avatar") is False:
            original = bot.image_1920
            params.set_param(prefix + "original_avatar", original.decode() if original else "empty")
        with file_open("jshp_bot_branding/static/img/jshp_logo.png", "rb") as logo:
            bot.write({"image_1920": base64.b64encode(logo.read())})
        params.set_param(prefix + "applied_avatar", bot.image_1920.decode())
