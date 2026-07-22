# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    l10n_ar_print_fantasy_name = fields.Boolean(
        related="company_id.l10n_ar_print_fantasy_name",
        readonly=False,
    )
    l10n_ar_print_delivery_address = fields.Boolean(
        related="company_id.l10n_ar_print_delivery_address",
        readonly=False,
    )
