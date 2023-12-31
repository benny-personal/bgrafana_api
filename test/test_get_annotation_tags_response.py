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

from bgrafana_api.models.get_annotation_tags_response import GetAnnotationTagsResponse  # noqa: E501

class TestGetAnnotationTagsResponse(unittest.TestCase):
    """GetAnnotationTagsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAnnotationTagsResponse:
        """Test GetAnnotationTagsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAnnotationTagsResponse`
        """
        model = GetAnnotationTagsResponse()  # noqa: E501
        if include_optional:
            return GetAnnotationTagsResponse(
                result = bgrafana_api.models.find_tags_result_is_the_result_of_a_tags_search/.FindTagsResult is the result of a tags search.(
                    tags = [
                        bgrafana_api.models.tags_dto_is_the_frontend_dto_for_tag/.TagsDTO is the frontend DTO for Tag.(
                            count = 56, 
                            tag = '', )
                        ], )
            )
        else:
            return GetAnnotationTagsResponse(
        )
        """

    def testGetAnnotationTagsResponse(self):
        """Test GetAnnotationTagsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
