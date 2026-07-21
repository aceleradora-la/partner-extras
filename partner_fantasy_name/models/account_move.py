# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).
from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    partner_fantasy_name = fields.Char(
        related="partner_id.fantasy_name",
        string="Partner Fantasy Name",
    )
