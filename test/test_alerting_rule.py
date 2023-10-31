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

from bgrafana_api.models.alerting_rule import AlertingRule  # noqa: E501

class TestAlertingRule(unittest.TestCase):
    """AlertingRule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AlertingRule:
        """Test AlertingRule
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AlertingRule`
        """
        model = AlertingRule()  # noqa: E501
        if include_optional:
            return AlertingRule(
                alerts = [
                    bgrafana_api.models.alert_has_info_for_an_alert/.Alert has info for an alert.(
                        active_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        annotations = {
                            'key' : ''
                            }, 
                        labels = {
                            'key' : ''
                            }, 
                        state = '', 
                        value = '', )
                    ],
                annotations = {
                    'key' : ''
                    },
                duration = 1.337,
                evaluation_time = 1.337,
                health = '',
                labels = {
                    'key' : ''
                    },
                last_error = '',
                last_evaluation = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '',
                query = '',
                state = '',
                type = ''
            )
        else:
            return AlertingRule(
                alerts = [
                    bgrafana_api.models.alert_has_info_for_an_alert/.Alert has info for an alert.(
                        active_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        annotations = {
                            'key' : ''
                            }, 
                        labels = {
                            'key' : ''
                            }, 
                        state = '', 
                        value = '', )
                    ],
                annotations = {
                    'key' : ''
                    },
                health = '',
                name = '',
                query = '',
                state = '',
                type = '',
        )
        """

    def testAlertingRule(self):
        """Test AlertingRule"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()