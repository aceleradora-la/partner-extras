# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).
from odoo import fields, models


class SaleReport(models.Model):
    _inherit = "sale.report"
    _depends = {"res.partner": ["fantasy_name"]}

    partner_fantasy_name = fields.Char(string="Customer Fantasy Name", readonly=True)

    def _select_additional_fields(self):
        fields_ = super()._select_additional_fields()
        # "partner" is the alias of the sale order customer (s.partner_id)
        # in the report query, see sale.report _from_sale().
        fields_["partner_fantasy_name"] = "partner.fantasy_name"
        return fields_

    def _group_by_sale(self):
        return (
            super()._group_by_sale()
            + """,
            partner.fantasy_name"""
        )
