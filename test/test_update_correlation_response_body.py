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

from bgrafana_api.models.update_correlation_response_body import UpdateCorrelationResponseBody  # noqa: E501

class TestUpdateCorrelationResponseBody(unittest.TestCase):
    """UpdateCorrelationResponseBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateCorrelationResponseBody:
        """Test UpdateCorrelationResponseBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateCorrelationResponseBody`
        """
        model = UpdateCorrelationResponseBody()  # noqa: E501
        if include_optional:
            return UpdateCorrelationResponseBody(
                message = 'Correlation updated',
                result = bgrafana_api.models.correlation.Correlation(
                    config = bgrafana_api.models.correlation_config.CorrelationConfig(
                        field = 'message', 
                        target = {"expr":"job=app"}, 
                        transformations = [
                            bgrafana_api.models.transformation.Transformation(
                                expression = '', 
                                field = '', 
                                map_value = '', 
                                type = 'regex', )
                            ], 
                        type = '', ), 
                    description = 'Logs to Traces', 
                    label = 'My Label', 
                    source_uid = 'd0oxYRg4z', 
                    target_uid = 'PE1C5CBDA0504A6A3', 
                    uid = '50xhMlg9k', )
            )
        else:
            return UpdateCorrelationResponseBody(
        )
        """

    def testUpdateCorrelationResponseBody(self):
        """Test UpdateCorrelationResponseBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()