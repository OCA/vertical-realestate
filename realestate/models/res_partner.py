# Copyright 2020 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def create(self, vals):
        """ It overrides create to bind appropriate realestate entity. """
        if all(
            (
                vals.get("type", "").startswith("real.estate"),
                not self.env.context.get("real_entity_no_create"),
            )
        ):
            model = self.env[vals["type"]].with_context(real_entity_no_create=True,)
            real_entity = model.create(vals)
            return real_entity.partner_id
        return super(ResPartner, self).create(vals)
