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

from bgrafana_api.models.query_stat import QueryStat  # noqa: E501

class TestQueryStat(unittest.TestCase):
    """QueryStat unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QueryStat:
        """Test QueryStat
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QueryStat`
        """
        model = QueryStat()  # noqa: E501
        if include_optional:
            return QueryStat(
                color = bgrafana_api.models.color.color(),
                custom = bgrafana_api.models.custom.custom(),
                decimals = 56,
                description = '',
                display_name = '',
                display_name_from_ds = '',
                filterable = True,
                interval = 1.337,
                links = [
                    bgrafana_api.models.data_link.DataLink(
                        target_blank = True, 
                        title = '', 
                        url = '', )
                    ],
                mappings = [
                    bgrafana_api.models.value_mapping.ValueMapping()
                    ],
                max = 1.337,
                min = 1.337,
                no_value = '',
                path = '',
                thresholds = bgrafana_api.models.thresholds_config.ThresholdsConfig(
                    mode = '', 
                    steps = [
                        bgrafana_api.models.threshold.Threshold(
                            color = '', 
                            state = '', 
                            value = 1.337, )
                        ], ),
                type = bgrafana_api.models.field_type_config.FieldTypeConfig(
                    enum = bgrafana_api.models.enum_field_config.EnumFieldConfig(
                        color = [
                            ''
                            ], 
                        description = [
                            ''
                            ], 
                        icon = [
                            ''
                            ], 
                        text = [
                            ''
                            ], ), ),
                unit = '',
                value = 1.337,
                writeable = True
            )
        else:
            return QueryStat(
        )
        """

    def testQueryStat(self):
        """Test QueryStat"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
