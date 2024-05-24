# Copyright 2020 ACSONE SA/NV
# Copyright 2024 Binhex - Christian Ramos
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class RealEstateOwnership(models.Model):

    _name = "real.estate.ownership"
    _description = "Real Estate Ownership"

    real_estate_id = fields.Many2one(
        comodel_name="real.estate",
        required=True,
        ondelete="cascade",
        index=True,
    )
    partner_id = fields.Many2one(
        comodel_name="res.partner",
        required=True,
    )
    ownership_type = fields.Many2one(
        comodel_name="real.estate.ownership.type",
        required=True,
    )
