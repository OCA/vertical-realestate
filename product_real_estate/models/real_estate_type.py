# Copyright 2020 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class RealEstateType(models.Model):
    _name = "real.estate.type"
    _description = "Real Estate Type"

    name = fields.Char(required=True, translate=True)
