# coding: utf-8

"""
    Grafana HTTP API.

    The Grafana backend exposes an HTTP API, the same API is used by the frontend to do everything from saving dashboards, creating users and updating data sources.

    The version of the OpenAPI document: 0.0.1
    Contact: hello@grafana.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from pydantic import StrictInt, StrictStr

from typing import List

from bgrafana_api.models.success_response_body import SuccessResponseBody
from bgrafana_api.models.team_group_dto import TeamGroupDTO
from bgrafana_api.models.team_group_mapping import TeamGroupMapping

from bgrafana_api.api_client import ApiClient
from bgrafana_api.api_response import ApiResponse
from bgrafana_api.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class SyncTeamGroupsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def add_team_group_api(self, team_id : StrictInt, team_group_mapping : TeamGroupMapping, **kwargs) -> SuccessResponseBody:  # noqa: E501
        """Add External Group.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_team_group_api(team_id, team_group_mapping, async_req=True)
        >>> result = thread.get()

        :param team_id: (required)
        :type team_id: int
        :param team_group_mapping: (required)
        :type team_group_mapping: TeamGroupMapping
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: SuccessResponseBody
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the add_team_group_api_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.add_team_group_api_with_http_info(team_id, team_group_mapping, **kwargs)  # noqa: E501

    @validate_arguments
    def add_team_group_api_with_http_info(self, team_id : StrictInt, team_group_mapping : TeamGroupMapping, **kwargs) -> ApiResponse:  # noqa: E501
        """Add External Group.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_team_group_api_with_http_info(team_id, team_group_mapping, async_req=True)
        >>> result = thread.get()

        :param team_id: (required)
        :type team_id: int
        :param team_group_mapping: (required)
        :type team_group_mapping: TeamGroupMapping
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(SuccessResponseBody, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'team_id',
            'team_group_mapping'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_team_group_api" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['team_id']:
            _path_params['teamId'] = _params['team_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['team_group_mapping'] is not None:
            _body_params = _params['team_group_mapping']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['api_key', 'basic']  # noqa: E501

        _response_types_map = {
            '200': "SuccessResponseBody",
            '400': "ErrorResponseBody",
            '401': "ErrorResponseBody",
            '403': "ErrorResponseBody",
            '404': "ErrorResponseBody",
            '500': "ErrorResponseBody",
        }

        return self.api_client.call_api(
            '/teams/{teamId}/groups', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_team_groups_api(self, team_id : StrictInt, **kwargs) -> List[TeamGroupDTO]:  # noqa: E501
        """Get External Groups.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_team_groups_api(team_id, async_req=True)
        >>> result = thread.get()

        :param team_id: (required)
        :type team_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[TeamGroupDTO]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_team_groups_api_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_team_groups_api_with_http_info(team_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_team_groups_api_with_http_info(self, team_id : StrictInt, **kwargs) -> ApiResponse:  # noqa: E501
        """Get External Groups.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_team_groups_api_with_http_info(team_id, async_req=True)
        >>> result = thread.get()

        :param team_id: (required)
        :type team_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(List[TeamGroupDTO], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'team_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_team_groups_api" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['team_id']:
            _path_params['teamId'] = _params['team_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['api_key', 'basic']  # noqa: E501

        _response_types_map = {
            '200': "List[TeamGroupDTO]",
            '400': "ErrorResponseBody",
            '401': "ErrorResponseBody",
            '403': "ErrorResponseBody",
            '404': "ErrorResponseBody",
            '500': "ErrorResponseBody",
        }

        return self.api_client.call_api(
            '/teams/{teamId}/groups', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def remove_team_group_api(self, group_id : StrictStr, team_id : StrictInt, **kwargs) -> SuccessResponseBody:  # noqa: E501
        """Remove External Group.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.remove_team_group_api(group_id, team_id, async_req=True)
        >>> result = thread.get()

        :param group_id: (required)
        :type group_id: str
        :param team_id: (required)
        :type team_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: SuccessResponseBody
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the remove_team_group_api_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.remove_team_group_api_with_http_info(group_id, team_id, **kwargs)  # noqa: E501

    @validate_arguments
    def remove_team_group_api_with_http_info(self, group_id : StrictStr, team_id : StrictInt, **kwargs) -> ApiResponse:  # noqa: E501
        """Remove External Group.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.remove_team_group_api_with_http_info(group_id, team_id, async_req=True)
        >>> result = thread.get()

        :param group_id: (required)
        :type group_id: str
        :param team_id: (required)
        :type team_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(SuccessResponseBody, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'group_id',
            'team_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_team_group_api" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['group_id']:
            _path_params['groupId'] = _params['group_id']

        if _params['team_id']:
            _path_params['teamId'] = _params['team_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['api_key', 'basic']  # noqa: E501

        _response_types_map = {
            '200': "SuccessResponseBody",
            '400': "ErrorResponseBody",
            '401': "ErrorResponseBody",
            '403': "ErrorResponseBody",
            '404': "ErrorResponseBody",
            '500': "ErrorResponseBody",
        }

        return self.api_client.call_api(
            '/teams/{teamId}/groups/{groupId}', 'DELETE',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
