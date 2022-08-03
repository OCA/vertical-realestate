# Copyright 2020 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Realestate",
    "summary": """
        Manages realestate""",
    "version": "13.0.1.0.2",
    "license": "AGPL-3",
    "development_status": "Alpha",
    "author": "ACSONE SA/NV, Odoo Community Association (OCA)",
    "maintainers": ["rousseldenis"],
    "website": "https://github.com/OCA/vertical-realestate",
    "depends": ["base", "mail", "contacts"],
    "data": [
        "security/security.xml",
        "views/menus.xml",
        "views/realestate_abstract_entity.xml",
    ],
    "application": True,
}
