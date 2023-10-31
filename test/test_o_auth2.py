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

from bgrafana_api.models.o_auth2 import OAuth2  # noqa: E501

class TestOAuth2(unittest.TestCase):
    """OAuth2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OAuth2:
        """Test OAuth2
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OAuth2`
        """
        model = OAuth2()  # noqa: E501
        if include_optional:
            return OAuth2(
                tls_config = bgrafana_api.models.tls_config_configures_the_options_for_tls_connections/.TLSConfig configures the options for TLS connections.(
                    ca_file = '', 
                    cert_file = '', 
                    insecure_skip_verify = True, 
                    key_file = '', 
                    max_version = 56, 
                    min_version = 56, 
                    server_name = '', ),
                client_id = '',
                client_secret = '',
                client_secret_file = '',
                endpoint_params = {
                    'key' : ''
                    },
                proxy_url = bgrafana_api.models.a_url_represents_a_parsed_url_(technically,_a_uri_reference)/.A URL represents a parsed URL (technically, a URI reference).(
                    force_query = True, 
                    fragment = '', 
                    host = '', 
                    omit_host = True, 
                    opaque = '', 
                    path = '', 
                    raw_fragment = '', 
                    raw_path = '', 
                    raw_query = '', 
                    scheme = '', 
                    user = bgrafana_api.models.userinfo.Userinfo(), ),
                scopes = [
                    ''
                    ],
                token_url = ''
            )
        else:
            return OAuth2(
        )
        """

    def testOAuth2(self):
        """Test OAuth2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()