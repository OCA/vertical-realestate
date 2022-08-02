# Copyright 2022 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo_test_helper import FakeModelLoader

from odoo.tests import SavepointCase


class TestRealEstate(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.loader = FakeModelLoader(cls.env, cls.__module__)
        cls.loader.backup_registry()

        # The fake class is imported here !! After the backup_registry
        from .test_model import RealEstateTest, ResPartner

        cls.loader.update_registry((ResPartner,))
        cls.loader.update_registry((RealEstateTest,))

    @classmethod
    def tearDownClass(cls):
        cls.loader.restore_registry()
        super().tearDownClass()

    def test_create(self):
        self.record = self.env["res.partner"].create({"type": "real.estate.test"})

        estate = self.env["real.estate.test"].search(
            [("partner_id", "=", self.record.id)]
        )

        self.assertTrue(estate)
