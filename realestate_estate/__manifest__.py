# Copyright 2020 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Realestate Estate",
    "summary": """
        Adds the estate management to realestate""",
    "version": "13.0.1.0.1",
    "license": "AGPL-3",
    "development_status": "Alpha",
    "author": "ACSONE SA/NV,Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/vertical-realestate",
    "depends": ["base", "mail", "realestate"],
    "data": [
        "security/real_estate_type.xml",
        "views/real_estate_type.xml",
        "security/real_estate.xml",
        "views/real_estate.xml",
        "data/ir_sequence.xml",
        "data/real_estate_type.xml",
        "demo/real_estate.xml",
    ],
    "demo": ["demo/real_estate.xml"],
}
