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

from bgrafana_api.models.config import Config  # noqa: E501

class TestConfig(unittest.TestCase):
    """Config unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Config:
        """Test Config
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Config`
        """
        model = Config()  # noqa: E501
        if include_optional:
            return Config(
                var_global = bgrafana_api.models.global_config.GlobalConfig(
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
                    opsgenie_api_url = , 
                    pagerduty_url = , 
                    resolve_timeout = 56, 
                    slack_api_url = , 
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
                    telegram_api_url = , 
                    victorops_api_key = '', 
                    victorops_api_key_file = '', 
                    victorops_api_url = , 
                    webex_api_url = , 
                    wechat_api_corp_id = '', 
                    wechat_api_secret = '', 
                    wechat_api_url = , ),
                inhibit_rules = [
                    bgrafana_api.models.inhibit_rule.InhibitRule(
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
                                value = '', )
                            ], )
                    ],
                mute_time_intervals = [
                    bgrafana_api.models.mute_time_interval_represents_a_named_set_of_time_intervals_for_which_a_route_should_be_muted/.MuteTimeInterval represents a named set of time intervals for which a route should be muted.(
                        name = '', 
                        time_intervals = [
                            bgrafana_api.models.time_interval.TimeInterval(
                                days_of_month = [
                                    ''
                                    ], 
                                location = '', 
                                months = [
                                    ''
                                    ], 
                                times = [
                                    bgrafana_api.models.time_range_represents_a_range_of_minutes_within_a_1440_minute_day,_exclusive_of_the_end_minute/_a_day_consists_of_1440_minutes/.TimeRange represents a range of minutes within a 1440 minute day, exclusive of the End minute. A day consists of 1440 minutes.(
                                        end_minute = 56, 
                                        start_minute = 56, )
                                    ], 
                                weekdays = [
                                    ''
                                    ], 
                                years = [
                                    ''
                                    ], )
                            ], )
                    ],
                route = bgrafana_api.models.route.Route(
                    continue = True, 
                    group_by = [
                        ''
                        ], 
                    group_interval = '', 
                    group_wait = '', 
                    match = {
                        'key' : ''
                        }, 
                    match_re = {
                        'key' : bgrafana_api.models.regexp_is_the_representation_of_a_compiled_regular_expression/.Regexp is the representation of a compiled regular expression.()
                        }, 
                    matchers = [
                        bgrafana_api.models.matcher_models_the_matching_of_a_label/.Matcher models the matching of a label.(
                            name = '', 
                            type = 56, 
                            value = '', )
                        ], 
                    mute_time_intervals = [
                        ''
                        ], 
                    object_matchers = [
                        bgrafana_api.models.matcher_models_the_matching_of_a_label/.Matcher models the matching of a label.(
                            name = '', 
                            value = '', )
                        ], 
                    provenance = '', 
                    receiver = '', 
                    repeat_interval = '', 
                    routes = [
                        bgrafana_api.models.route.Route(
                            continue = True, 
                            group_interval = '', 
                            group_wait = '', 
                            receiver = '', 
                            repeat_interval = '', )
                        ], ),
                templates = [
                    ''
                    ]
            )
        else:
            return Config(
        )
        """

    def testConfig(self):
        """Test Config"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
