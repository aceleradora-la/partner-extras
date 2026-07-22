# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).
{
    "name": "Partner Fantasy Name",
    "summary": "Add a Fantasy Name (trade name) to partners, searchable "
               "everywhere and available in sales and invoicing analysis.",
    "version": "19.0.1.2.0",
    "category": "Sales/Sales",
    "license": "LGPL-3",
    "author": "Aceleradora LA",
    "website": "https://github.com/aceleradora-la/partner-extras",
    "depends": [
        "sale",
        "account",
    ],
    "data": [
        "views/res_partner_views.xml",
        "views/sale_order_views.xml",
        "views/sale_report_views.xml",
        "views/account_move_views.xml",
        "views/account_invoice_report_views.xml",
    ],
    "installable": True,
    "application": False,
}
