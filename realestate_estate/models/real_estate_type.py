# Copyright 2020 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class RealEstateType(models.Model):

    _name = "real.estate.type"
    _description = "Real Estate Type"

    name = fields.Char(required=True, translate=True)
    code = fields.Char(required=True, index=True,)

    _sql_constraints = [
        ("code_uniq", "unique (code)", "The code has to be unique!"),
    ]
