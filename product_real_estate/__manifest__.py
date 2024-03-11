{
    "name": "Real estate",
    "summary": """
        Apartment management project.""",
    "author": "Binhex,Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/vertical-realestate",
    "version": "16.0.1.0.1",
    "depends": [
        "base",
        "portal",
        "website",
        "contacts",
        "website_sale",
        "product_template_tags",
        "realestate",
    ],
    "license": "AGPL-3",
    "data": [
        "security/ir.model.access.csv",
        "views/product_template_views.xml",
        "views/website_sale.xml",
        "views/menuitems.xml",
        "views/res_partner.xml",
        "views/res_country_zone.xml",
        "views/product_template_portal_templates.xml",
    ],
}
