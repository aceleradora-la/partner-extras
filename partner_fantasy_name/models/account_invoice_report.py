# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).
from odoo import api, fields, models
from odoo.tools import SQL


class AccountInvoiceReport(models.Model):
    _inherit = "account.invoice.report"
    _depends = {"res.partner": ["fantasy_name"]}

    partner_fantasy_name = fields.Char(string="Partner Fantasy Name", readonly=True)

    @api.model
    def _select(self) -> SQL:
        return SQL(
            "%s, move_partner.fantasy_name AS partner_fantasy_name",
            super()._select(),
        )

    @api.model
    def _from(self) -> SQL:
        # Dedicated join on the invoice partner (move.partner_id): the
        # existing "partner" alias points to the line partner (commercial
        # partner), not to the partner displayed on the invoice.
        return SQL(
            "%s LEFT JOIN res_partner move_partner ON move_partner.id = move.partner_id",
            super()._from(),
        )
