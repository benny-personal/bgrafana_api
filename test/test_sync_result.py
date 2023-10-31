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

from bgrafana_api.models.sync_result import SyncResult  # noqa: E501

class TestSyncResult(unittest.TestCase):
    """SyncResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SyncResult:
        """Test SyncResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SyncResult`
        """
        model = SyncResult()  # noqa: E501
        if include_optional:
            return SyncResult(
                elapsed = 56,
                failed_users = [
                    bgrafana_api.models.failed_user.FailedUser(
                        error = '', 
                        login = '', )
                    ],
                missing_user_ids = [
                    56
                    ],
                started = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_user_ids = [
                    56
                    ]
            )
        else:
            return SyncResult(
        )
        """

    def testSyncResult(self):
        """Test SyncResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
