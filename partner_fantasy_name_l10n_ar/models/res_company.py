# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).
from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    l10n_ar_print_fantasy_name = fields.Boolean(
        string="Print Fantasy Name on AR Invoices",
        default=True,
        help="Print the customer's fantasy name below their legal name "
             "on Argentinean invoices.",
    )
    l10n_ar_print_delivery_address = fields.Boolean(
        string="Print Delivery Address on AR Invoices",
        default=False,
        help="Print the delivery address at the end of the customer data "
             "block on Argentinean customer invoices, when it differs from "
             "the invoice address.",
    )
