# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"
    # Extend the fields used by name_search / display_name searches so that
    # partners can be found by their fantasy name anywhere a partner is
    # looked up (sale order customer, invoices, contact search views, ...).
    _rec_names_search = [
        "complete_name",
        "email",
        "ref",
        "vat",
        "company_registry",
        "fantasy_name",
    ]

    fantasy_name = fields.Char(
        string="Fantasy Name",
        index="trigram",
        help="Commercial or trade name by which the partner is publicly known.",
    )
