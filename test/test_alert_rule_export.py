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

from bgrafana_api.models.alert_rule_export import AlertRuleExport  # noqa: E501

class TestAlertRuleExport(unittest.TestCase):
    """AlertRuleExport unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AlertRuleExport:
        """Test AlertRuleExport
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AlertRuleExport`
        """
        model = AlertRuleExport()  # noqa: E501
        if include_optional:
            return AlertRuleExport(
                annotations = {
                    'key' : ''
                    },
                condition = '',
                dasboard_uid = '',
                data = [
                    bgrafana_api.models.alert_query_export_is_the_provisioned_export_of_models/alert_query/.AlertQueryExport is the provisioned export of models.AlertQuery.(
                        datasource_uid = '', 
                        model = bgrafana_api.models.model.model(), 
                        query_type = '', 
                        ref_id = '', 
                        relative_time_range = bgrafana_api.models.relative_time_range.RelativeTimeRange(
                            from = 56, 
                            to = 56, ), )
                    ],
                exec_err_state = 'Alerting',
                var_for = 56,
                is_paused = True,
                labels = {
                    'key' : ''
                    },
                no_data_state = 'Alerting',
                panel_id = 56,
                title = '',
                uid = ''
            )
        else:
            return AlertRuleExport(
        )
        """

    def testAlertRuleExport(self):
        """Test AlertRuleExport"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()