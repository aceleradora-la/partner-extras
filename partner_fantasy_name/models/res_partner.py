# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).
from odoo import api, fields, models


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

    @api.depends("fantasy_name")
    def _compute_display_name(self):
        # Show the fantasy name next to the partner name, e.g. in the
        # dropdown of every partner many2one: "NAME (FANTASY NAME)".
        super()._compute_display_name()
        for partner in self:
            if partner.fantasy_name:
                partner.display_name = (
                    f"{partner.display_name} ({partner.fantasy_name})"
                )
