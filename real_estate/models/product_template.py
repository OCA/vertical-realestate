from odoo import _, api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    real_estate_type_id = fields.Many2one("real.estate.type")
    detailed_type = fields.Selection(
        selection_add=[("real_estate", "Real Estate")],
        tracking=True,
        ondelete={"real_estate": "set default"},
    )
    type = fields.Selection(
        selection_add=[("real_estate", "Real Estate")],
        tracking=True,
    )
    price_type = fields.Selection([("fixed", "Fixed"), ("monthly", "Monthly")])
    sale_type = fields.Selection([("sale", "Sale"), ("rent", "Rent")])
    flat_condition = fields.Selection(
        [
            ("new", _("New")),
            ("good", _("Good")),
            ("bad", _("Bad")),
            ("deteriorated", _("Deteriorated")),
        ]
    )

    # Technical data
    furnished = fields.Boolean()
    elevator = fields.Boolean()
    restrooms = fields.Integer()
    bedrooms = fields.Integer()
    garage = fields.Boolean()
    surface = fields.Float(default=0.0)
    existent_pool = fields.Boolean()
    terrace = fields.Boolean()
    parking = fields.Boolean()

    # Facilities
    shopping_center = fields.Boolean()
    medical_center = fields.Boolean()
    train_station = fields.Integer()
    tram_station = fields.Integer()
    beach = fields.Integer()

    # Location
    description = fields.Text()
    street = fields.Char()
    street2 = fields.Char()
    zip_code = fields.Char(change_default=True)
    city = fields.Char()
    state_id = fields.Many2one(
        "res.country.state",
        ondelete="restrict",
        domain="[('country_id', '=?', country_id)]",
    )
    country_id = fields.Many2one("res.country", ondelete="restrict")
    zone_id = fields.Many2one(
        "res.country.zone",
        ondelete="restrict",
        domain="[('state_id', '=?', state_id)]",
    )

    # Owners/Tenants
    tenant_ids = fields.Many2many("res.partner", "real_estate_tenant_rel")
    owner_ids = fields.Many2many("res.partner", "real_estate_owner_rel")
    google_maps_url = fields.Text()
    energy_consumption = fields.Float()
    emissions = fields.Float()
    stove = fields.Selection([("gas", _("Gas")), ("electric", _("Electric"))])
    thermo = fields.Selection([("gas", _("Gas")), ("electric", _("Electric"))])
    antiquity = fields.Selection(
        [
            ("110", _("1 - 10 years")),
            ("1030", _("10 - 30 years ")),
            ("3050", _("30 - 50 years")),
            ("50+", _("+ 50 years")),
        ],
    )
    floor = fields.Integer()

    # Price depending on the sale type
    @api.onchange("sale_type")
    def _onchange_sale_type(self):
        if self.sale_type:
            if self.sale_type == "sale":
                self.price_type = "fixed"
            elif self.sale_type == "rent":
                self.price_type = "monthly"

    @api.constrains("list_price")
    def _constrains_valid_price(self):
        if self.list_price < 0:
            return {
                "warning": {
                    "title": _("Warning"),
                    "message": _("The price can not be negative"),
                },
            }
