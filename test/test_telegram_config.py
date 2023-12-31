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

from bgrafana_api.models.telegram_config import TelegramConfig  # noqa: E501

class TestTelegramConfig(unittest.TestCase):
    """TelegramConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TelegramConfig:
        """Test TelegramConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TelegramConfig`
        """
        model = TelegramConfig()  # noqa: E501
        if include_optional:
            return TelegramConfig(
                api_url = bgrafana_api.models.a_url_represents_a_parsed_url_(technically,_a_uri_reference)/.A URL represents a parsed URL (technically, a URI reference).(
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
                chat = 56,
                disable_notifications = True,
                http_config = bgrafana_api.models.http_client_config_configures_an_http_client/.HTTPClientConfig configures an HTTP client.(
                    authorization = bgrafana_api.models.authorization_contains_http_authorization_credentials/.Authorization contains HTTP authorization credentials.(
                        credentials = '', 
                        credentials_file = '', 
                        type = '', ), 
                    basic_auth = bgrafana_api.models.basic_auth_contains_basic_http_authentication_credentials/.BasicAuth contains basic HTTP authentication credentials.(
                        password = '', 
                        password_file = '', 
                        username = '', ), 
                    bearer_token = '', 
                    bearer_token_file = '', 
                    enable_http2 = True, 
                    follow_redirects = True, 
                    oauth2 = bgrafana_api.models.o_auth2_is_the_oauth2_client_configuration/.OAuth2 is the oauth2 client configuration.(
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
                        token_url = '', ), 
                    proxy_connect_header = {
                        'key' : [
                            ''
                            ]
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
                        scheme = '', ), 
                    tls_config = bgrafana_api.models.tls_config_configures_the_options_for_tls_connections/.TLSConfig configures the options for TLS connections.(
                        ca_file = '', 
                        cert_file = '', 
                        insecure_skip_verify = True, 
                        key_file = '', 
                        server_name = '', ), ),
                message = '',
                parse_mode = '',
                send_resolved = True,
                token = ''
            )
        else:
            return TelegramConfig(
        )
        """

    def testTelegramConfig(self):
        """Test TelegramConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
