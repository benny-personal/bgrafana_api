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

from bgrafana_api.models.custom_permissions_record_dto import CustomPermissionsRecordDTO  # noqa: E501

class TestCustomPermissionsRecordDTO(unittest.TestCase):
    """CustomPermissionsRecordDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomPermissionsRecordDTO:
        """Test CustomPermissionsRecordDTO
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomPermissionsRecordDTO`
        """
        model = CustomPermissionsRecordDTO()  # noqa: E501
        if include_optional:
            return CustomPermissionsRecordDTO(
                custom_permissions = '',
                grantee_name = '',
                grantee_type = '',
                grantee_url = '',
                id = 56,
                is_folder = True,
                org_id = 56,
                org_role = '',
                slug = '',
                title = '',
                uid = '',
                url = '',
                users_count = 56
            )
        else:
            return CustomPermissionsRecordDTO(
        )
        """

    def testCustomPermissionsRecordDTO(self):
        """Test CustomPermissionsRecordDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
