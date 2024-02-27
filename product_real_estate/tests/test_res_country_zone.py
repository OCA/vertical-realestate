from odoo.tests.common import TransactionCase


class TestResCountryZone(TransactionCase):
    def setUp(self):
        super().setUp()
        self.country_id = self.env.ref("base.es")
        self.state_id = self.env["res.country.state"].create(
            {"country_id": self.country_id.id, "name": "Madrid", "code": "MAD"}
        )
        self.zone_id = self.env["res.country.zone"].create(
            {
                "state_id": self.state_id.id,
                "name": "Madrid",
            }
        )

    def test_name_get(self):
        res = self.zone_id.name_get()
        self.assertEqual(res[0][0], self.zone_id.id)
