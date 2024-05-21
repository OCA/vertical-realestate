# Copyright 2020 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class RealEstate(models.Model):
    _name = "real.estate"
    _inherits = {"res.partner": "partner_id"}
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Real Estate"

    partner_id = fields.Many2one(
        string="Related Partner",
        comodel_name="res.partner",
        required=True,
        auto_join=True,
        ondelete="cascade",
        index=True,
    )
    type = fields.Selection(
        default=lambda s: s._name,
        related="partner_id.type",
        readonly=False,
    )
    type_id = fields.Many2one(
        comodel_name="real.estate.type",
        required=True,
        ondelete="restrict",
        index=True,
    )
    ref = fields.Char(
        default=lambda self: self.env["ir.sequence"].next_by_code("real.estate"),
        string="Reference",
        index=True,
        copy=False,
        readonly=True,
    )
    short_description = fields.Char(
        translate=True,
        size=50,
    )
    description = fields.Text(
        translate=True,
    )
    surface = fields.Float(default=0.0)
    google_maps_url = fields.Text()

    def open_parent(self):
        return self.partner_id.open_parent()

    @api.model
    @api.returns("self", lambda value: value.id)
    def create(self, vals):
        vals = self._create_vals(vals)
        self_context = self
        if "type" in vals:
            self_context = self.with_context(default_type=vals.get("type"))
        return super(RealEstate, self_context).create(vals)

    @api.model
    def _create_vals(self, vals):
        """Override this in child classes in order to add default values."""
        return vals
