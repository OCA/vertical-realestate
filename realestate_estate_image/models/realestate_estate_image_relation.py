# Copyright 2020 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class RealestateEstateImageRelation(models.Model):

    _name = "realestate.estate.image.relation"
    _inherit = "image.relation.abstract"
    _description = "Realestate Estate Image Relation"

    sequence = fields.Integer()
    image_id = fields.Many2one(
        "storage.image", required=True, ondelete="cascade", index=True,
    )
    estate_id = fields.Many2one(
        "real.estate", required=True, ondelete="cascade", index=True,
    )
    # for kanban view
    image_name = fields.Char(related="image_id.name")
    # for kanban view
    image_url = fields.Char(related="image_id.image_medium_url")

    tag_id = fields.Many2one("image.tag", domain=[("apply_on", "=", "real.estate")])
