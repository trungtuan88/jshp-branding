# Part of jshp-odoo. See LICENSE file for full copyright and licensing details.

from odoo import models


class MailBot(models.AbstractModel):
    _inherit = "mail.bot"

    def _get_answer(self, channel, body, values, command=False):
        answer = super()._get_answer(channel, body, values, command=command)
        # Replace after translation; str.replace also preserves Markup safety.
        if isinstance(answer, list):
            return [item.replace("OdooBot", "JSHPBot") for item in answer]
        return answer.replace("OdooBot", "JSHPBot") if answer else answer
