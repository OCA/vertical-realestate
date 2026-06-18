import logging
import os

import requests

from odoo import api, models

_logger = logging.getLogger(__name__)


# https://api.developer.attomdata.com/docs
class AttomApi(models.AbstractModel):
    _name = "attom.api"
    _description = "ATTOM API"

    @api.model
    def property_expandedprofile(self, params):
        if not self.has_access("read"):
            return

        get_param = self.env["ir.config_parameter"].sudo().get_param
        timeout = int(get_param("attom.api_timeout", 10))
        url = get_param("attom.api_url")
        if not url:
            _logger.debug("attom.api_url not configured")
            return

        headers = {
            "accept": "application/json",
            "apikey": get_param("attom.api_key", os.environ.get("ATTOM_API_KEY", "")),
        }
        if not headers["apikey"]:
            _logger.debug("attom.api_key not configured")
            return

        try:
            response = requests.get(
                f"{url}/property/expandedprofile",
                headers=headers,
                params=params,
                timeout=timeout,
            )
            response.raise_for_status()
            try:
                body = response.json()
                return body["property"][0]  # TODO Handle multiple responses
            except (LookupError, TypeError, ValueError):
                _logger.warning("ATTOM API malformed response %s", response.text)
        except requests.RequestException:
            _logger.warning("ATTOM API failed request %s", params)
