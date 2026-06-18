import json
from unittest.mock import Mock, patch

from odoo.tests import TransactionCase
from odoo.tools import file_open


class TestPartner(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.env["ir.config_parameter"].set_param("attom.api_key", "bogus")
        cls.partner = cls.env["res.partner"].create(
            {
                "name": "Test",
                "street": "13204 Cain Ln",
                "city": "Louisville",
                "state_id": cls.env.ref("base.state_us_18").id,  # KY
                "zip": "40245",
            }
        )

    def test_attom_format_address(self):
        self.assertEqual(
            self.partner._attom_address(), "13204 Cain Ln, Louisville KY 40245"
        )

    def test_attom_property_expandedprofile(self):
        def mock_get(url, **kwargs):
            self.assertEqual(
                url,
                "https://api.gateway.attomdata.com/propertyapi/v1.0.0/property/expandedprofile",
            )
            self.assertEqual(
                kwargs["params"], {"address": "13204 Cain Ln, Louisville KY 40245"}
            )
            self.assertEqual(kwargs["timeout"], 10)
            mock_response = Mock()
            mock_response.raise_for_status = Mock()
            with file_open("attom/tests/data/property_expandedprofile.json") as file:
                mock_response.json.return_value = json.load(file)
            return mock_response

        with patch("requests.get", mock_get):
            data = self.partner._attom_property_expandedprofile()
        self.assertEqual(
            data["address"]["oneLine"], "13204 CAIN LN, LOUISVILLE, KY 40245"
        )
