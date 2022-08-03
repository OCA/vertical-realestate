# Copyright 2020 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class RealEstateAbstractEntity(models.AbstractModel):
    _name = "realestate.abstract.entity"
    _description = "RealEstate Abstract Entity"
    _inherits = {"res.partner": "partner_id"}
    _inherit = ["mail.thread"]

    active = fields.Boolean(default=True,)
    partner_id = fields.Many2one(
        string="Related Partner",
        comodel_name="res.partner",
        required=True,
        ondelete="cascade",
        index=True,
    )
    type = fields.Selection(
        default=lambda s: s._name, related="partner_id.type", readonly=False,
    )

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
        """ Override this in child classes in order to add default values. """
        return vals
