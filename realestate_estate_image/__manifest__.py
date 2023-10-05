# Copyright 2020 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Realestate Estate Image",
    "summary": """
        Adds multi image real estate management""",
    "version": "13.0.1.0.0",
    "license": "AGPL-3",
    "development_status": "Alpha",
    "author": "ACSONE SA/NV,Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/vertical-realestate",
    "depends": ["realestate_estate", "storage_image", "storage_image_main"],
    "data": [
        "security/realestate_estate_image_relation.xml",
        "views/realestate_estate_image_relation.xml",
        "views/real_estate.xml",
    ],
}
