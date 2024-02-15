from odoo import Command

from .test_real_estate_type import TestRealEstateType
from .test_res_country_zone import TestResCountryZone


class TestProductTemplate(TestResCountryZone, TestRealEstateType):
    def setUp(self):
        super().setUp()
        owner_partner = self.env["res.partner"].search([], limit=2)
        self.product_template_id = self.env["product.template"].create(
            {
                "name": "Flat",
                "sale_ok": True,
                "detailed_type": "real_estate",
                "zone_id": self.zone_id.id,
                "sale_type": "sale",
                "real_estate_type_id": self.real_estate_type_id.id,
                "stove": "gas",
                "thermo": "gas",
                "owner_ids": [Command.set(owner_partner.ids)],
            }
        )

    def test_name_get(self):
        res = self.product_template_id.name_get()
        self.assertEqual(res[0][0], self.product_template_id.id)
        self.assertEqual(self.product_template_id.name, "Flat")

    def test_owner_values(self):
        self.assertLessEqual(len(self.product_template_id.owner_ids), 2)

    def test_owner_ids(self):
        owners = self.env["res.partner"].search([("property_ids", "!=", False)])
        self.assertTrue(len(owners) > 0)
