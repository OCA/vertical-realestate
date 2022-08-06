# Copyright 2020 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class RealEstate(models.Model):

    _name = "real.estate"
    _inherit = ["real.estate", "storage.main.image.mixin"]
    _field_image_ids = "image_ids"

    # small and medium image are here to replace
    # native image field on form and kanban
    image_small_url = fields.Char(
        related="image_ids.image_id.image_small_url", store=True
    )
    image_medium_url = fields.Char(
        related="image_ids.image_id.image_medium_url", store=True
    )
    image_ids = fields.One2many(
        "realestate.estate.image.relation", inverse_name="estate_id", string="Images"
    )
