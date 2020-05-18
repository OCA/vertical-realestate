# Copyright 2020 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ImageTag(models.Model):

    _name = "image.tag"
    _description = "Image Tag"

    @api.model
    def _get_default_apply_on(self):
        active_model = self.env.context.get("active_model")
        return (
            "real.estate"
            if active_model == "realestate.estate.image.relation"
            else False
        )

    name = fields.Char()
    apply_on = fields.Selection(
        selection=[("real.estate", "Real Estate")],
        default=lambda self: self._get_default_apply_on(),
    )
