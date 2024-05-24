# Copyright 2020 ACSONE SA/NV
# Copyright 2024 Binhex - Christian Ramos
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class RealEstateOwnershipType(models.Model):

    _name = "real.estate.ownership.type"
    _description = "Real Estate Ownership Type"

    name = fields.Char(
        required=True,
        translate=True,
    )
