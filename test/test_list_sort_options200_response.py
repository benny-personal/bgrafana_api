# coding: utf-8

"""
    Grafana HTTP API.

    The Grafana backend exposes an HTTP API, the same API is used by the frontend to do everything from saving dashboards, creating users and updating data sources.

    The version of the OpenAPI document: 0.0.1
    Contact: hello@grafana.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from bgrafana_api.models.list_sort_options200_response import ListSortOptions200Response  # noqa: E501

class TestListSortOptions200Response(unittest.TestCase):
    """ListSortOptions200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListSortOptions200Response:
        """Test ListSortOptions200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListSortOptions200Response`
        """
        model = ListSortOptions200Response()  # noqa: E501
        if include_optional:
            return ListSortOptions200Response(
                description = '',
                display_name = '',
                meta = '',
                name = ''
            )
        else:
            return ListSortOptions200Response(
        )
        """

    def testListSortOptions200Response(self):
        """Test ListSortOptions200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
