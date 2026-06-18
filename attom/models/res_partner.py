from odoo import models

from odoo.addons.base.models.res_partner import ADDRESS_FIELDS

ATTOM_FIELDS = [
    field for field in ADDRESS_FIELDS if field not in ("country_id", "street2")
]


class ResPartner(models.Model):
    _inherit = "res.partner"

    def _attom_address(self):
        if self.country_id and (self.country_id != self.env.ref("base.us")):
            return
        if all([self[field] for field in ATTOM_FIELDS]):
            address = self._display_address(without_company=True)
            address = ", ".join([a for a in address.split("\n") if a.strip()])
            return address

    def _attom_property_expandedprofile(self):
        self.ensure_one()
        if address := self._attom_address():
            return self.env["attom.api"].property_expandedprofile({"address": address})
