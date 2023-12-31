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

from bgrafana_api.models.test_receivers_result import TestReceiversResult  # noqa: E501

class TestTestReceiversResult(unittest.TestCase):
    """TestReceiversResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TestReceiversResult:
        """Test TestReceiversResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TestReceiversResult`
        """
        model = TestReceiversResult()  # noqa: E501
        if include_optional:
            return TestReceiversResult(
                alert = bgrafana_api.models.test_receivers_config_alert_params.TestReceiversConfigAlertParams(
                    annotations = {
                        'key' : ''
                        }, 
                    labels = {
                        'key' : ''
                        }, ),
                notified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                receivers = [
                    bgrafana_api.models.test_receiver_result.TestReceiverResult(
                        grafana_managed_receiver_configs = [
                            bgrafana_api.models.test_receiver_config_result.TestReceiverConfigResult(
                                error = '', 
                                name = '', 
                                status = '', 
                                uid = '', )
                            ], 
                        name = '', )
                    ]
            )
        else:
            return TestReceiversResult(
        )
        """

    def testTestReceiversResult(self):
        """Test TestReceiversResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
