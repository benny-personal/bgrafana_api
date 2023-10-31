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

from bgrafana_api.models.folder import Folder  # noqa: E501

class TestFolder(unittest.TestCase):
    """Folder unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Folder:
        """Test Folder
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Folder`
        """
        model = Folder()  # noqa: E501
        if include_optional:
            return Folder(
                access_control = {
                    'key' : True
                    },
                can_admin = True,
                can_delete = True,
                can_edit = True,
                can_save = True,
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_by = '',
                has_acl = True,
                id = 56,
                parent_uid = '',
                title = '',
                uid = '',
                updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_by = '',
                url = '',
                version = 56
            )
        else:
            return Folder(
        )
        """

    def testFolder(self):
        """Test Folder"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
