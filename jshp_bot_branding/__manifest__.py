# Part of jshp-odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "JSHP Bot Branding",
    "version": "1.1.1",
    "summary": "JSHPBot identity and favicon; company-managed login logo",
    "author": "NTT",
    "website": "https://jshp.com.vn",
    "license": "LGPL-3",
    "depends": ["mail_bot"],
    "data": ["data/bot_name.xml", "views/branding_templates.xml"],
    "uninstall_hook": "uninstall_hook",
    "installable": True,
}
