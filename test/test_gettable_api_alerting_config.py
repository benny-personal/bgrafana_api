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

from bgrafana_api.models.gettable_api_alerting_config import GettableApiAlertingConfig  # noqa: E501

class TestGettableApiAlertingConfig(unittest.TestCase):
    """GettableApiAlertingConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GettableApiAlertingConfig:
        """Test GettableApiAlertingConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GettableApiAlertingConfig`
        """
        model = GettableApiAlertingConfig()  # noqa: E501
        if include_optional:
            return GettableApiAlertingConfig(
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
                mute_time_provenances = {
                    'key' : ''
                    },
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
                receivers = [
                    bgrafana_api.models.gettable_api_receiver.GettableApiReceiver(
                        discord_configs = [
                            bgrafana_api.models.discord_config_configures_notifications_via_discord/.DiscordConfig configures notifications via Discord.(
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
                                send_resolved = True, 
                                title = '', 
                                webhook_url = , )
                            ], 
                        email_configs = [
                            bgrafana_api.models.email_config_configures_notifications_via_mail/.EmailConfig configures notifications via mail.(
                                auth_identity = '', 
                                auth_password = '', 
                                auth_password_file = '', 
                                auth_secret = '', 
                                auth_username = '', 
                                from = '', 
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
                                to = '', )
                            ], 
                        grafana_managed_receiver_configs = [
                            bgrafana_api.models.gettable_grafana_receiver.GettableGrafanaReceiver(
                                disable_resolve_message = True, 
                                name = '', 
                                provenance = '', 
                                secure_fields = {
                                    'key' : True
                                    }, 
                                settings = bgrafana_api.models.raw_message.RawMessage(), 
                                type = '', 
                                uid = '', )
                            ], 
                        name = '', 
                        opsgenie_configs = [
                            bgrafana_api.models.ops_genie_config_configures_notifications_via_ops_genie/.OpsGenieConfig configures notifications via OpsGenie.(
                                actions = '', 
                                api_key = '', 
                                api_key_file = '', 
                                api_url = , 
                                description = '', 
                                details = {
                                    'key' : ''
                                    }, 
                                entity = '', 
                                message = '', 
                                note = '', 
                                priority = '', 
                                responders = [
                                    bgrafana_api.models.ops_genie_config_responder.OpsGenieConfigResponder(
                                        id = '', 
                                        name = '', 
                                        type = '', 
                                        username = '', )
                                    ], 
                                send_resolved = True, 
                                source = '', 
                                tags = '', 
                                update_alerts = True, )
                            ], 
                        pagerduty_configs = [
                            bgrafana_api.models.pagerduty_config_configures_notifications_via_pager_duty/.PagerdutyConfig configures notifications via PagerDuty.(
                                class = '', 
                                client = '', 
                                client_url = '', 
                                component = '', 
                                description = '', 
                                group = '', 
                                images = [
                                    bgrafana_api.models.pagerduty_image.PagerdutyImage(
                                        alt = '', 
                                        href = '', 
                                        src = '', )
                                    ], 
                                links = [
                                    bgrafana_api.models.pagerduty_link.PagerdutyLink(
                                        href = '', 
                                        text = '', )
                                    ], 
                                routing_key = '', 
                                routing_key_file = '', 
                                send_resolved = True, 
                                service_key = '', 
                                service_key_file = '', 
                                severity = '', 
                                source = '', 
                                url = , )
                            ], 
                        pushover_configs = [
                            bgrafana_api.models.pushover_config.PushoverConfig(
                                expire = '', 
                                html = True, 
                                message = '', 
                                priority = '', 
                                retry = '', 
                                send_resolved = True, 
                                sound = '', 
                                title = '', 
                                token = '', 
                                token_file = '', 
                                url_title = '', 
                                user_key = '', 
                                user_key_file = '', )
                            ], 
                        slack_configs = [
                            bgrafana_api.models.slack_config_configures_notifications_via_slack/.SlackConfig configures notifications via Slack.(
                                actions = [
                                    bgrafana_api.models.slack_action_configures_a_single_slack_action_that_is_sent_with_each_notification/.SlackAction configures a single Slack action that is sent with each notification.(
                                        confirm = bgrafana_api.models.slack_confirmation_field.SlackConfirmationField(
                                            dismiss_text = '', 
                                            ok_text = '', 
                                            text = '', 
                                            title = '', ), 
                                        name = '', 
                                        style = '', 
                                        text = '', 
                                        type = '', 
                                        value = '', )
                                    ], 
                                api_url_file = '', 
                                callback_id = '', 
                                channel = '', 
                                color = '', 
                                fallback = '', 
                                fields = [
                                    bgrafana_api.models.slack_field_configures_a_single_slack_field_that_is_sent_with_each_notification/.SlackField configures a single Slack field that is sent with each notification.(
                                        short = True, 
                                        title = '', 
                                        value = '', )
                                    ], 
                                footer = '', 
                                icon_emoji = '', 
                                icon_url = '', 
                                image_url = '', 
                                link_names = True, 
                                mrkdwn_in = [
                                    ''
                                    ], 
                                pretext = '', 
                                send_resolved = True, 
                                short_fields = True, 
                                text = '', 
                                thumb_url = '', 
                                title = '', 
                                title_link = '', 
                                username = '', )
                            ], 
                        sns_configs = [
                            bgrafana_api.models.sns_config.SNSConfig(
                                attributes = {
                                    'key' : ''
                                    }, 
                                message = '', 
                                phone_number = '', 
                                send_resolved = True, 
                                sigv4 = bgrafana_api.models.sig_v4_config.SigV4Config(
                                    access_key = '', 
                                    profile = '', 
                                    region = '', 
                                    role_arn = '', 
                                    secret_key = '', ), 
                                subject = '', 
                                target_arn = '', 
                                topic_arn = '', )
                            ], 
                        telegram_configs = [
                            bgrafana_api.models.telegram_config_configures_notifications_via_telegram/.TelegramConfig configures notifications via Telegram.(
                                chat = 56, 
                                disable_notifications = True, 
                                message = '', 
                                parse_mode = '', 
                                send_resolved = True, )
                            ], 
                        victorops_configs = [
                            bgrafana_api.models.victor_ops_config_configures_notifications_via_victor_ops/.VictorOpsConfig configures notifications via VictorOps.(
                                api_key_file = '', 
                                custom_fields = {
                                    'key' : ''
                                    }, 
                                entity_display_name = '', 
                                message_type = '', 
                                monitoring_tool = '', 
                                send_resolved = True, 
                                state_message = '', )
                            ], 
                        webex_configs = [
                            bgrafana_api.models.webex_config_configures_notifications_via_webex/.WebexConfig configures notifications via Webex.(
                                message = '', 
                                room_id = '', 
                                send_resolved = True, )
                            ], 
                        webhook_configs = [
                            bgrafana_api.models.webhook_config_configures_notifications_via_a_generic_webhook/.WebhookConfig configures notifications via a generic webhook.(
                                max_alerts = 56, 
                                send_resolved = True, )
                            ], 
                        wechat_configs = [
                            bgrafana_api.models.wechat_config_configures_notifications_via_wechat/.WechatConfig configures notifications via Wechat.(
                                agent_id = '', 
                                api_secret = '', 
                                corp_id = '', 
                                message = '', 
                                message_type = '', 
                                send_resolved = True, 
                                to_party = '', 
                                to_tag = '', 
                                to_user = '', )
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
            return GettableApiAlertingConfig(
        )
        """

    def testGettableApiAlertingConfig(self):
        """Test GettableApiAlertingConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
