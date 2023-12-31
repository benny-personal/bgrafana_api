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

from bgrafana_api.models.library_element_dto_meta import LibraryElementDTOMeta  # noqa: E501

class TestLibraryElementDTOMeta(unittest.TestCase):
    """LibraryElementDTOMeta unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LibraryElementDTOMeta:
        """Test LibraryElementDTOMeta
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LibraryElementDTOMeta`
        """
        model = LibraryElementDTOMeta()  # noqa: E501
        if include_optional:
            return LibraryElementDTOMeta(
                connected_dashboards = 56,
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_by = bgrafana_api.models.library_element_dto_meta_user_defines_model_for_library_element_dto_meta_user/.LibraryElementDTOMetaUser defines model for LibraryElementDTOMetaUser.(
                    avatar_url = '', 
                    id = 56, 
                    name = '', ),
                folder_name = '',
                folder_uid = '',
                updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_by = bgrafana_api.models.library_element_dto_meta_user_defines_model_for_library_element_dto_meta_user/.LibraryElementDTOMetaUser defines model for LibraryElementDTOMetaUser.(
                    avatar_url = '', 
                    id = 56, 
                    name = '', )
            )
        else:
            return LibraryElementDTOMeta(
        )
        """

    def testLibraryElementDTOMeta(self):
        """Test LibraryElementDTOMeta"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
