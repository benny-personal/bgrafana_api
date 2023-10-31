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

from bgrafana_api.models.alertmanager_status import AlertmanagerStatus  # noqa: E501

class TestAlertmanagerStatus(unittest.TestCase):
    """AlertmanagerStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AlertmanagerStatus:
        """Test AlertmanagerStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AlertmanagerStatus`
        """
        model = AlertmanagerStatus()  # noqa: E501
        if include_optional:
            return AlertmanagerStatus(
                cluster = bgrafana_api.models.cluster_status.clusterStatus(
                    name = '', 
                    peers = [
                        bgrafana_api.models.peer_status.peerStatus(
                            address = '', 
                            name = '', )
                        ], 
                    status = '[ready settling disabled]', ),
                config = bgrafana_api.models.alertmanager_config.alertmanagerConfig(
                    original = '', ),
                uptime = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                version_info = bgrafana_api.models.version_info.versionInfo(
                    branch = '', 
                    build_date = '', 
                    build_user = '', 
                    go_version = '', 
                    revision = '', 
                    version = '', )
            )
        else:
            return AlertmanagerStatus(
                cluster = bgrafana_api.models.cluster_status.clusterStatus(
                    name = '', 
                    peers = [
                        bgrafana_api.models.peer_status.peerStatus(
                            address = '', 
                            name = '', )
                        ], 
                    status = '[ready settling disabled]', ),
                config = bgrafana_api.models.alertmanager_config.alertmanagerConfig(
                    original = '', ),
                uptime = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                version_info = bgrafana_api.models.version_info.versionInfo(
                    branch = '', 
                    build_date = '', 
                    build_user = '', 
                    go_version = '', 
                    revision = '', 
                    version = '', ),
        )
        """

    def testAlertmanagerStatus(self):
        """Test AlertmanagerStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
