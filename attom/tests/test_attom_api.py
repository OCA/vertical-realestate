import os

from odoo.tests import TransactionCase, tagged


@tagged("external", "-standard")
class TestAttomApi(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.env["ir.config_parameter"].set_param(
            "attom.api_key", os.environ.get("ATTOM_API_KEY", "")
        )

    def test_property_expandedprofile(self):
        data = self.env["attom.api"].property_expandedprofile(
            {
                "address": "2503 Champion Lakes Ct, Louisville KY 40245",
            }
        )
        self.assertEqual(
            data["address"]["oneLine"], "2503 CHAMPION LAKES CT, LOUISVILLE, KY 40245"
        )

    def test_property_expandedprofile_error(self):
        with self.assertLogs("odoo.addons.attom.models.attom_api", level="WARNING"):
            data = self.env["attom.api"].property_expandedprofile(
                {
                    "address": "Hello World, Beverly Hills, CA, 90212",
                }
            )
        self.assertIsNone(data)
