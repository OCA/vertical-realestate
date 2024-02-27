from odoo import fields, models


class CountryZone(models.Model):
    _description = "Country Zone"
    _name = "res.country.zone"
    _order = "name"

    state_id = fields.Many2one("res.country.state", required=True)
    name = fields.Char(required=True)
