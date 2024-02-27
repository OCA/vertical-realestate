from odoo.tests.common import TransactionCase


class TestRealEstateType(TransactionCase):
    def setUp(self):
        super().setUp()
        self.real_estate_type_id = self.env["real.estate.type"].create(
            {
                "name": "Flat",
            }
        )

    def test_name_get(self):
        res = self.real_estate_type_id.name_get()
        self.assertEqual(res[0][0], self.real_estate_type_id.id)
