# Copyright 2020 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class RealEstate(models.Model):
    _name = "real.estate"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Real Estate"

    name = fields.Char(required=True, translate=True, index=True)
    type_id = fields.Many2one(
        comodel_name="real.estate.type",
        required=True,
        ondelete="restrict",
        index=True,
    )
    active = fields.Boolean(default=True)
    image = fields.Image(
        max_width=256,
        max_height=256,
        help="This field holds the image used for the real estate",
    )
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
    real_estate_latitude = fields.Float(digits=(10, 7))
    real_estate_longitude = fields.Float(digits=(10, 7))
    comment = fields.Html()
    owner_ids = fields.Many2many(
        "res.partner",
    )
    company_id = fields.Many2one(
        comodel_name="res.company",
        default=lambda self: self.env.company.id,
        help="The default company for this user.",
    )
