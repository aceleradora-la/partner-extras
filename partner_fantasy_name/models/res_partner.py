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
        # Show "NAME (FANTASY NAME)" only where a customer/vendor is being
        # picked (sale orders, invoices, ...): those many2one fields carry
        # res_partner_search_mode in their context. Generic partner displays
        # (report pivots, contact lists, chatter) keep the plain name.
        # Set show_fantasy_name in the context to force it either way.
        super()._compute_display_name()
        show = self.env.context.get("show_fantasy_name")
        if show is None:
            show = bool(self.env.context.get("res_partner_search_mode"))
        if not show:
            return
        for partner in self:
            if partner.fantasy_name:
                partner.display_name = (
                    f"{partner.display_name} ({partner.fantasy_name})"
                )
