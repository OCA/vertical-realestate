# Copyright 2022 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class RealEstateTest(models.Model):

    _name = "real.estate.test"
    _inherit = ["realestate.abstract.entity"]
    _description = "Real Estate Test"


class ResPartner(models.Model):

    _inherit = "res.partner"

    type = fields.Selection(
        selection_add=[("real.estate.test", "Estate Test")], readonly=False
    )
