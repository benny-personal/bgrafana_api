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

from bgrafana_api.models.hit import Hit  # noqa: E501

class TestHit(unittest.TestCase):
    """Hit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Hit:
        """Test Hit
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Hit`
        """
        model = Hit()  # noqa: E501
        if include_optional:
            return Hit(
                folder_id = 56,
                folder_title = '',
                folder_uid = '',
                folder_url = '',
                id = 56,
                is_starred = True,
                slug = '',
                sort_meta = 56,
                sort_meta_name = '',
                tags = [
                    ''
                    ],
                title = '',
                type = '',
                uid = '',
                uri = '',
                url = ''
            )
        else:
            return Hit(
        )
        """

    def testHit(self):
        """Test Hit"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()