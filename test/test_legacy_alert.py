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

from bgrafana_api.models.legacy_alert import LegacyAlert  # noqa: E501

class TestLegacyAlert(unittest.TestCase):
    """LegacyAlert unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LegacyAlert:
        """Test LegacyAlert
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LegacyAlert`
        """
        model = LegacyAlert()  # noqa: E501
        if include_optional:
            return LegacyAlert(
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                dashboard_id = 56,
                eval_data = None,
                execution_error = '',
                var_for = 56,
                frequency = 56,
                handler = 56,
                id = 56,
                message = '',
                name = '',
                new_state_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                org_id = 56,
                panel_id = 56,
                settings = None,
                severity = '',
                silenced = True,
                state = '',
                state_changes = 56,
                updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                version = 56
            )
        else:
            return LegacyAlert(
        )
        """

    def testLegacyAlert(self):
        """Test LegacyAlert"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()