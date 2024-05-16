# Copyright 2022 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class RealEstateTest(models.Model):

    _name = "real.estate.test"
    _inherit = ["realestate.abstract.entity"]
    _description = "Real Estate Test"
