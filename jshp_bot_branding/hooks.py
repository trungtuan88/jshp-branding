# Part of jshp-odoo. See LICENSE file for full copyright and licensing details.

def uninstall_hook(env):
    bot = env.ref("base.partner_root")
    if bot.name == "JSHPBot":
        bot.write({"name": "OdooBot"})
    params = env["ir.config_parameter"].sudo()
    prefix = "jshp_bot_branding."
    original = params.get_param(prefix + "original_avatar")
    applied = params.get_param(prefix + "applied_avatar")
    current = bot.image_1920.decode() if bot.image_1920 else False
    if original and current == applied:
        bot.write({"image_1920": False if original == "empty" else original})
    params.search([("key", "in", [prefix + "original_avatar", prefix + "applied_avatar"])]).unlink()
