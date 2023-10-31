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

from bgrafana_api.models.quota_dto import QuotaDTO  # noqa: E501

class TestQuotaDTO(unittest.TestCase):
    """QuotaDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QuotaDTO:
        """Test QuotaDTO
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QuotaDTO`
        """
        model = QuotaDTO()  # noqa: E501
        if include_optional:
            return QuotaDTO(
                limit = 56,
                org_id = 56,
                target = '',
                used = 56,
                user_id = 56
            )
        else:
            return QuotaDTO(
        )
        """

    def testQuotaDTO(self):
        """Test QuotaDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()