# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).
from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    partner_fantasy_name = fields.Char(
        related="partner_id.fantasy_name",
        string="Customer Fantasy Name",
    )
