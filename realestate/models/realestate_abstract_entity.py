# Copyright 2020 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class RealEstateAbstractEntity(models.Model):
    _name = "realestate.abstract.entity"
    _description = "RealEstate Abstract Entity"
    _inherits = {"res.partner": "partner_id"}
    _inherit = ["mail.thread"]

    active = fields.Boolean(default=True)

    def open_parent(self):
        """Utility method used to add an "Open Parent" button in partner views"""
        self.ensure_one()
        address_form_id = self.env.ref("base.view_partner_address_form").id
        return {
            "type": "ir.actions.act_window",
            "res_model": "res.partner",
            "view_mode": "form",
            "views": [(address_form_id, "form")],
            "res_id": self.parent_id.id,
            "target": "new",
        }

    @api.model
    @api.returns("self", lambda value: value.id)
    def create(self, vals):
        vals = self._create_vals(vals)
        self_context = self
        if "type" in vals:
            self_context = self.with_context(default_type=vals.get("type"))
        return super(RealEstateAbstractEntity, self_context).create(vals)

    @api.model
    def _create_vals(self, vals):
        """Override this in child classes in order to add default values."""
        return vals
