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

from bgrafana_api.models.time_interval import TimeInterval  # noqa: E501

class TestTimeInterval(unittest.TestCase):
    """TimeInterval unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimeInterval:
        """Test TimeInterval
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimeInterval`
        """
        model = TimeInterval()  # noqa: E501
        if include_optional:
            return TimeInterval(
                days_of_month = [
                    ''
                    ],
                location = '',
                months = [
                    ''
                    ],
                times = [
                    bgrafana_api.models.time_range_represents_a_range_of_minutes_within_a_1440_minute_day,_exclusive_of_the_end_minute/_a_day_consists_of_1440_minutes/.TimeRange represents a range of minutes within a 1440 minute day, exclusive of the End minute. A day consists of 1440 minutes.(
                        end_minute = 56, 
                        start_minute = 56, )
                    ],
                weekdays = [
                    ''
                    ],
                years = [
                    ''
                    ]
            )
        else:
            return TimeInterval(
        )
        """

    def testTimeInterval(self):
        """Test TimeInterval"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()