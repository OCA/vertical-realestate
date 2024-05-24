# Copyright 2020 ACSONE SA/NV
# Copyright 2024 Binhex - Christian Ramos
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class RealEstate(models.Model):
    _name = "real.estate"
    _inherit = ["mail.thread", "mail.activity.mixin", "image.mixin"]
    _description = "Real Estate"

    name = fields.Char(required=True, translate=True, index=True)
    type_id = fields.Many2one(
        comodel_name="real.estate.type",
        required=True,
        ondelete="restrict",
        index=True,
    )
    active = fields.Boolean(default=True)
    ref = fields.Char(
        default=lambda self: self.env["ir.sequence"].next_by_code("real.estate"),
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

    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char(change_default=True)
    city = fields.Char()
    state_id = fields.Many2one(
        "res.country.state",
        ondelete="restrict",
        domain="[('country_id', '=?', country_id)]",
    )
    country_id = fields.Many2one("res.country", ondelete="restrict")
    country_code = fields.Char(
        related="country_id.code",
    )
    comment = fields.Html()
    owner_ids = fields.One2many(
        comodel_name="real.estate.ownership",
        inverse_name="real_estate_id",
        string="Owners",
    )
    company_id = fields.Many2one(
        comodel_name="res.company",
        default=lambda self: self.env.company.id,
        help="The default company for this estate.",
    )
