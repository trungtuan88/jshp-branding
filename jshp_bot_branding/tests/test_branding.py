# Part of jshp-odoo. See LICENSE file for full copyright and licensing details.

from odoo.tests.common import TransactionCase


class TestBotBranding(TransactionCase):
    def test_system_identity(self):
        self.assertEqual(self.env.ref("base.partner_root").name, "JSHPBot")
        self.assertEqual(self.env.ref("base.user_root").name, "JSHPBot")

    def test_status_label(self):
        info = self.env["res.users"].with_context(lang="en_US").fields_get(["odoobot_state"])
        self.assertEqual(info["odoobot_state"]["string"], "JSHPBot Status")

    def test_mention_instructions(self):
        user = self.env.user
        channel = self.env["discuss.channel"]._get_or_create_chat(
            [self.env.ref("base.partner_root").id, user.partner_id.id]
        )
        bot = self.env["mail.bot"].with_context(lang="en_US")
        user.odoobot_state = "onboarding_command"
        answer = bot._get_answer(channel, "", {}, command="help")
        self.assertIn("@JSHPBot", answer)
        self.assertNotIn("OdooBot", answer)
        self.assertEqual(user.odoobot_state, "onboarding_ping")
        answer = bot._get_answer(channel, "hello", {})
        self.assertIn("@JSHPBot", answer)
        answer = bot._get_answer(channel, "", {"partner_ids": [self.env.ref("base.partner_root").id]})
        self.assertEqual(user.odoobot_state, "onboarding_attachement")

    def test_logo_and_upgrade_backup(self):
        params = self.env["ir.config_parameter"].sudo()
        original = params.get_param("jshp_bot_branding.original_avatar")
        self.assertTrue(original)
        self.env["res.users"]._apply_jshp_bot_logo()
        self.assertEqual(params.get_param("jshp_bot_branding.original_avatar"), original)
        self.assertEqual(
            self.env.ref("base.partner_root").image_1920.decode(),
            params.get_param("jshp_bot_branding.applied_avatar"),
        )

    def test_branding_templates(self):
        logo = "/jshp_bot_branding/static/img/jshp_logo.png"
        login = self.env.ref("web.login_layout")._get_combined_arch()
        self.assertEqual(
            login.xpath("//img/@t-attf-src"),
            ["/web/binary/company_logo{{ '?dbname='+db if db else '' }}"],
        )
        self.assertNotIn(logo, login.xpath("//img/@src"))
        layout = self.env.ref("web.layout")._get_combined_arch()
        icon = layout.xpath("//link[@rel='shortcut icon']")[0]
        self.assertEqual(icon.get("href"), logo)
        self.assertEqual(icon.get("type"), "image/png")
        self.assertNotIn("t-att-href", icon.attrib)
