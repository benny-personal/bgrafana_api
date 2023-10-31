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

from bgrafana_api.models.inhibit_rule import InhibitRule  # noqa: E501

class TestInhibitRule(unittest.TestCase):
    """InhibitRule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InhibitRule:
        """Test InhibitRule
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InhibitRule`
        """
        model = InhibitRule()  # noqa: E501
        if include_optional:
            return InhibitRule(
                equal = [
                    ''
                    ],
                source_match = {
                    'key' : ''
                    },
                source_match_re = {
                    'key' : bgrafana_api.models.regexp_is_the_representation_of_a_compiled_regular_expression/.Regexp is the representation of a compiled regular expression.()
                    },
                source_matchers = [
                    bgrafana_api.models.matcher_models_the_matching_of_a_label/.Matcher models the matching of a label.(
                        name = '', 
                        type = 56, 
                        value = '', )
                    ],
                target_match = {
                    'key' : ''
                    },
                target_match_re = {
                    'key' : bgrafana_api.models.regexp_is_the_representation_of_a_compiled_regular_expression/.Regexp is the representation of a compiled regular expression.()
                    },
                target_matchers = [
                    bgrafana_api.models.matcher_models_the_matching_of_a_label/.Matcher models the matching of a label.(
                        name = '', 
                        type = 56, 
                        value = '', )
                    ]
            )
        else:
            return InhibitRule(
        )
        """

    def testInhibitRule(self):
        """Test InhibitRule"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()