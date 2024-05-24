# Copyright 2020 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Real Estate",
    "summary": """
        Adds the estate management to realestate""",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "development_status": "Alpha",
    "author": "Binhex, " "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/vertical-realestate",
    "depends": ["base", "mail", "contacts"],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/menus.xml",
        "views/real_estate_type.xml",
        "views/realestate_estate.xml",
        "data/ir_sequence.xml",
    ],
}
