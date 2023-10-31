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

from bgrafana_api.models.email_config import EmailConfig  # noqa: E501

class TestEmailConfig(unittest.TestCase):
    """EmailConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EmailConfig:
        """Test EmailConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EmailConfig`
        """
        model = EmailConfig()  # noqa: E501
        if include_optional:
            return EmailConfig(
                auth_identity = '',
                auth_password = '',
                auth_password_file = '',
                auth_secret = '',
                auth_username = '',
                var_from = '',
                headers = {
                    'key' : ''
                    },
                hello = '',
                html = '',
                require_tls = True,
                send_resolved = True,
                smarthost = bgrafana_api.models.host_port_represents_a_"host:port"_network_address/.HostPort represents a "host:port" network address.(
                    host = '', 
                    port = '', ),
                text = '',
                tls_config = bgrafana_api.models.tls_config_configures_the_options_for_tls_connections/.TLSConfig configures the options for TLS connections.(
                    ca_file = '', 
                    cert_file = '', 
                    insecure_skip_verify = True, 
                    key_file = '', 
                    max_version = 56, 
                    min_version = 56, 
                    server_name = '', ),
                to = ''
            )
        else:
            return EmailConfig(
        )
        """

    def testEmailConfig(self):
        """Test EmailConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()