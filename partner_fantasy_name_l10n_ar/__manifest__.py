# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).
{
    "name": "Partner Fantasy Name - Argentina",
    "summary": "Print the partner's fantasy name and the delivery address "
               "on Argentinean invoices (configurable per company).",
    "version": "18.0.1.0.0",
    "category": "Accounting/Localizations",
    "license": "LGPL-3",
    "author": "Aceleradora LA",
    "website": "https://github.com/aceleradora-la/partner-extras",
    "depends": [
        "partner_fantasy_name",
        "l10n_ar",
    ],
    "auto_install": True,
    "data": [
        "views/res_config_settings_views.xml",
        "report/report_invoice.xml",
    ],
    "installable": True,
    "application": False,
}
