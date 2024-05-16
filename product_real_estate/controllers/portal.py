# Part of Odoo. See LICENSE file for full copyright and licensing details.

from collections import OrderedDict

from odoo import _, http
from odoo.http import request

from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager


class ProductTemplateCustomerPortal(CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        if "product_count" in counters:
            values["product_count"] = (
                request.env["product.template"].search_count(
                    [
                        ("detailed_type", "=", "real_estate"),
                        ("owner_ids", "in", [request.env.user.partner_id.id]),
                    ]
                )
                if request.env["product.template"].check_access_rights(
                    "read", raise_exception=False
                )
                else 0
            )

        return values

    def _prepare_real_estate_domain(self, partner):
        return [
            ("detailed_type", "=", "real_estate"),
            ("owner_ids", "in", [partner.id]),
        ]

    def _get_product_searchbar_sortings(self):
        return OrderedDict(
            [
                ("name", {"label": _("Name"), "order": "name"}),
            ]
        )

    def _prepare_real_estate_portal_rendering_values(
        self, page=1, sortby=None, **kwargs
    ):
        ProductTemplate = request.env["product.template"]

        if not sortby:
            sortby = "name"

        partner = request.env.user.partner_id

        url = "/my/real-estate"
        domain = self._prepare_real_estate_domain(partner)

        searchbar_sortings = self._get_product_searchbar_sortings()

        sort_order = searchbar_sortings[sortby]["order"]
        values = {}
        pager_values = portal_pager(
            url=url,
            total=ProductTemplate.search_count(domain),
            page=page,
            step=self._items_per_page,
            url_args={"sortby": sortby},
        )
        products = ProductTemplate.search(
            domain,
            order=sort_order,
            limit=self._items_per_page,
            offset=pager_values["offset"],
        )

        values.update(
            {
                "products": products,
                "page_name": "real_estate",
                "pager": pager_values,
                "default_url": url,
                "searchbar_sortings": searchbar_sortings,
                "sortby": sortby,
            }
        )

        return values

    @http.route(
        ["/my/real-estate", "/my/real-estate/page/<int:page>"],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_real_estate(self, **kwargs):
        values = self._prepare_real_estate_portal_rendering_values(**kwargs)
        return request.render("real_estate.portal_my_real_estate", values)
