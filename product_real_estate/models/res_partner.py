from odoo import fields, models


class RealEstateClient(models.Model):
    _inherit = "res.partner"

    property_ids = fields.Many2many("product.template", "real_estate_owner_rel")
    rented_property_ids = fields.Many2many("product.template", "real_estate_tenant_rel")
