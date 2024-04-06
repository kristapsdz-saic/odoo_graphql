from odoo import http
from odoo.http import request, content_disposition
from odoo.exceptions import ValidationError
import werkzeug
import json

import logging

_logger = logging.getLogger(__name__)


class TestApollo(http.Controller):
    @http.route(
        "/graphql/test-modules/apollo", auth="public", type="http", website=True, sitemap=False, csrf=False,
    )
    def test_appolo(self):
        # https://spec.graphql.org/June2018/#sec-Response-Format
        query = request.httprequest.data.decode()  # request.graphqlrequest
        response = request.env["graphql.handler"].handle_query(query)
        payload = json.dumps(response, indent=4)
        return payload

    @http.route(
        "/graphql/test-modules/apollo", type="http", website=True, sitemap=False
    )
    def test_apollo(self):
        return request.render("odoo_graphql_test.test-graphql")