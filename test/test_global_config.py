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

from bgrafana_api.models.global_config import GlobalConfig  # noqa: E501

class TestGlobalConfig(unittest.TestCase):
    """GlobalConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GlobalConfig:
        """Test GlobalConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GlobalConfig`
        """
        model = GlobalConfig()  # noqa: E501
        if include_optional:
            return GlobalConfig(
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
                opsgenie_api_key = '',
                opsgenie_api_key_file = '',
                opsgenie_api_url = bgrafana_api.models.a_url_represents_a_parsed_url_(technically,_a_uri_reference)/.A URL represents a parsed URL (technically, a URI reference).(
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
                pagerduty_url = bgrafana_api.models.a_url_represents_a_parsed_url_(technically,_a_uri_reference)/.A URL represents a parsed URL (technically, a URI reference).(
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
                resolve_timeout = 56,
                slack_api_url = bgrafana_api.models.a_url_represents_a_parsed_url_(technically,_a_uri_reference)/.A URL represents a parsed URL (technically, a URI reference).(
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
                slack_api_url_file = '',
                smtp_auth_identity = '',
                smtp_auth_password = '',
                smtp_auth_password_file = '',
                smtp_auth_secret = '',
                smtp_auth_username = '',
                smtp_from = '',
                smtp_hello = '',
                smtp_require_tls = True,
                smtp_smarthost = bgrafana_api.models.host_port_represents_a_"host:port"_network_address/.HostPort represents a "host:port" network address.(
                    host = '', 
                    port = '', ),
                telegram_api_url = bgrafana_api.models.a_url_represents_a_parsed_url_(technically,_a_uri_reference)/.A URL represents a parsed URL (technically, a URI reference).(
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
                victorops_api_key = '',
                victorops_api_key_file = '',
                victorops_api_url = bgrafana_api.models.a_url_represents_a_parsed_url_(technically,_a_uri_reference)/.A URL represents a parsed URL (technically, a URI reference).(
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
                webex_api_url = bgrafana_api.models.a_url_represents_a_parsed_url_(technically,_a_uri_reference)/.A URL represents a parsed URL (technically, a URI reference).(
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
                wechat_api_corp_id = '',
                wechat_api_secret = '',
                wechat_api_url = bgrafana_api.models.a_url_represents_a_parsed_url_(technically,_a_uri_reference)/.A URL represents a parsed URL (technically, a URI reference).(
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
                    user = bgrafana_api.models.userinfo.Userinfo(), )
            )
        else:
            return GlobalConfig(
        )
        """

    def testGlobalConfig(self):
        """Test GlobalConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
