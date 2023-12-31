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

from typing import Optional

from bgrafana_api.models.add_data_source200_response import AddDataSource200Response
from bgrafana_api.models.add_permission200_response import AddPermission200Response
from bgrafana_api.models.data_source_permissions_dto import DataSourcePermissionsDTO
from bgrafana_api.models.success_response_body import SuccessResponseBody

from bgrafana_api.api_client import ApiClient
from bgrafana_api.api_response import ApiResponse
from bgrafana_api.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class DatasourcePermissionsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def add_permission(self, datasource_id : StrictStr, user_id : Optional[StrictInt] = None, team_id : Optional[StrictInt] = None, builtin_role : Optional[StrictStr] = None, permission : Optional[StrictInt] = None, **kwargs) -> AddPermission200Response:  # noqa: E501
        """Add permissions for a data source.  # noqa: E501

        You need to have a permission with action `datasources.permissions:read` and scopes `datasources:*`, `datasources:id:*`, `datasources:id:1` (single data source).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_permission(datasource_id, user_id, team_id, builtin_role, permission, async_req=True)
        >>> result = thread.get()

        :param datasource_id: (required)
        :type datasource_id: str
        :param user_id:
        :type user_id: int
        :param team_id:
        :type team_id: int
        :param builtin_role:
        :type builtin_role: str
        :param permission:
        :type permission: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AddPermission200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the add_permission_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.add_permission_with_http_info(datasource_id, user_id, team_id, builtin_role, permission, **kwargs)  # noqa: E501

    @validate_arguments
    def add_permission_with_http_info(self, datasource_id : StrictStr, user_id : Optional[StrictInt] = None, team_id : Optional[StrictInt] = None, builtin_role : Optional[StrictStr] = None, permission : Optional[StrictInt] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Add permissions for a data source.  # noqa: E501

        You need to have a permission with action `datasources.permissions:read` and scopes `datasources:*`, `datasources:id:*`, `datasources:id:1` (single data source).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_permission_with_http_info(datasource_id, user_id, team_id, builtin_role, permission, async_req=True)
        >>> result = thread.get()

        :param datasource_id: (required)
        :type datasource_id: str
        :param user_id:
        :type user_id: int
        :param team_id:
        :type team_id: int
        :param builtin_role:
        :type builtin_role: str
        :param permission:
        :type permission: int
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
        :rtype: tuple(AddPermission200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'datasource_id',
            'user_id',
            'team_id',
            'builtin_role',
            'permission'
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
                    " to method add_permission" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['datasource_id']:
            _path_params['datasourceId'] = _params['datasource_id']


        # process the query parameters
        _query_params = []
        if _params.get('user_id') is not None:  # noqa: E501
            _query_params.append(('userId', _params['user_id']))

        if _params.get('team_id') is not None:  # noqa: E501
            _query_params.append(('teamId', _params['team_id']))

        if _params.get('builtin_role') is not None:  # noqa: E501
            _query_params.append(('builtinRole', _params['builtin_role']))

        if _params.get('permission') is not None:  # noqa: E501
            _query_params.append(('permission', _params['permission']))

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
            '200': "AddPermission200Response",
            '401': "ErrorResponseBody",
            '403': "ErrorResponseBody",
            '404': "ErrorResponseBody",
            '500': "ErrorResponseBody",
        }

        return self.api_client.call_api(
            '/datasources/{datasourceId}/permissions', 'POST',
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
    def delete_permissions(self, datasource_id : StrictStr, permission_id : StrictStr, **kwargs) -> SuccessResponseBody:  # noqa: E501
        """Remove permission for a data source.  # noqa: E501

        Removes the permission with the given permissionId for the data source with the given id.  You need to have a permission with action `datasources.permissions:delete` and scopes `datasources:*`, `datasources:id:*`, `datasources:id:1` (single data source).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_permissions(datasource_id, permission_id, async_req=True)
        >>> result = thread.get()

        :param datasource_id: (required)
        :type datasource_id: str
        :param permission_id: (required)
        :type permission_id: str
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
            message = "Error! Please call the delete_permissions_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.delete_permissions_with_http_info(datasource_id, permission_id, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_permissions_with_http_info(self, datasource_id : StrictStr, permission_id : StrictStr, **kwargs) -> ApiResponse:  # noqa: E501
        """Remove permission for a data source.  # noqa: E501

        Removes the permission with the given permissionId for the data source with the given id.  You need to have a permission with action `datasources.permissions:delete` and scopes `datasources:*`, `datasources:id:*`, `datasources:id:1` (single data source).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_permissions_with_http_info(datasource_id, permission_id, async_req=True)
        >>> result = thread.get()

        :param datasource_id: (required)
        :type datasource_id: str
        :param permission_id: (required)
        :type permission_id: str
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
            'datasource_id',
            'permission_id'
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
                    " to method delete_permissions" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['datasource_id']:
            _path_params['datasourceId'] = _params['datasource_id']

        if _params['permission_id']:
            _path_params['permissionId'] = _params['permission_id']


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
            '401': "ErrorResponseBody",
            '403': "ErrorResponseBody",
            '404': "ErrorResponseBody",
        }

        return self.api_client.call_api(
            '/datasources/{datasourceId}/permissions/{permissionId}', 'DELETE',
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
    def disable_permissions(self, datasource_id : StrictStr, **kwargs) -> AddDataSource200Response:  # noqa: E501
        """Disable permissions for a data source.  # noqa: E501

        Disables permissions for the data source with the given id. All existing permissions will be removed and anyone will be able to query the data source.  You need to have a permission with action `datasources.permissions:toggle` and scopes `datasources:*`, `datasources:id:*`, `datasources:id:1` (single data source).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.disable_permissions(datasource_id, async_req=True)
        >>> result = thread.get()

        :param datasource_id: (required)
        :type datasource_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AddDataSource200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the disable_permissions_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.disable_permissions_with_http_info(datasource_id, **kwargs)  # noqa: E501

    @validate_arguments
    def disable_permissions_with_http_info(self, datasource_id : StrictStr, **kwargs) -> ApiResponse:  # noqa: E501
        """Disable permissions for a data source.  # noqa: E501

        Disables permissions for the data source with the given id. All existing permissions will be removed and anyone will be able to query the data source.  You need to have a permission with action `datasources.permissions:toggle` and scopes `datasources:*`, `datasources:id:*`, `datasources:id:1` (single data source).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.disable_permissions_with_http_info(datasource_id, async_req=True)
        >>> result = thread.get()

        :param datasource_id: (required)
        :type datasource_id: str
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
        :rtype: tuple(AddDataSource200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'datasource_id'
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
                    " to method disable_permissions" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['datasource_id']:
            _path_params['datasourceId'] = _params['datasource_id']


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
            '200': "AddDataSource200Response",
            '400': "ErrorResponseBody",
            '401': "ErrorResponseBody",
            '403': "ErrorResponseBody",
            '404': "ErrorResponseBody",
            '500': "ErrorResponseBody",
        }

        return self.api_client.call_api(
            '/datasources/{datasourceId}/disable-permissions', 'POST',
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
    def enable_permissions(self, datasource_id : StrictStr, **kwargs) -> AddDataSource200Response:  # noqa: E501
        """Enable permissions for a data source.  # noqa: E501

        Enables permissions for the data source with the given id. No one except Org Admins will be able to query the data source until permissions have been added which permit certain users or teams to query the data source.  You need to have a permission with action `datasources.permissions:toggle` and scopes `datasources:*`, `datasources:id:*`, `datasources:id:1` (single data source).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.enable_permissions(datasource_id, async_req=True)
        >>> result = thread.get()

        :param datasource_id: (required)
        :type datasource_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AddDataSource200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the enable_permissions_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.enable_permissions_with_http_info(datasource_id, **kwargs)  # noqa: E501

    @validate_arguments
    def enable_permissions_with_http_info(self, datasource_id : StrictStr, **kwargs) -> ApiResponse:  # noqa: E501
        """Enable permissions for a data source.  # noqa: E501

        Enables permissions for the data source with the given id. No one except Org Admins will be able to query the data source until permissions have been added which permit certain users or teams to query the data source.  You need to have a permission with action `datasources.permissions:toggle` and scopes `datasources:*`, `datasources:id:*`, `datasources:id:1` (single data source).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.enable_permissions_with_http_info(datasource_id, async_req=True)
        >>> result = thread.get()

        :param datasource_id: (required)
        :type datasource_id: str
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
        :rtype: tuple(AddDataSource200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'datasource_id'
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
                    " to method enable_permissions" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['datasource_id']:
            _path_params['datasourceId'] = _params['datasource_id']


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
            '200': "AddDataSource200Response",
            '400': "ErrorResponseBody",
            '401': "ErrorResponseBody",
            '403': "ErrorResponseBody",
            '404': "ErrorResponseBody",
            '500': "ErrorResponseBody",
        }

        return self.api_client.call_api(
            '/datasources/{datasourceId}/enable-permissions', 'POST',
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
    def get_all_permissions(self, datasource_id : StrictStr, **kwargs) -> DataSourcePermissionsDTO:  # noqa: E501
        """Get permissions for a data source.  # noqa: E501

        Gets all existing permissions for the data source with the given id.  You need to have a permission with action `datasources.permissions:read` and scopes `datasources:*`, `datasources:id:*`, `datasources:id:1` (single data source).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_all_permissions(datasource_id, async_req=True)
        >>> result = thread.get()

        :param datasource_id: (required)
        :type datasource_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DataSourcePermissionsDTO
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_all_permissions_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_all_permissions_with_http_info(datasource_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_all_permissions_with_http_info(self, datasource_id : StrictStr, **kwargs) -> ApiResponse:  # noqa: E501
        """Get permissions for a data source.  # noqa: E501

        Gets all existing permissions for the data source with the given id.  You need to have a permission with action `datasources.permissions:read` and scopes `datasources:*`, `datasources:id:*`, `datasources:id:1` (single data source).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_all_permissions_with_http_info(datasource_id, async_req=True)
        >>> result = thread.get()

        :param datasource_id: (required)
        :type datasource_id: str
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
        :rtype: tuple(DataSourcePermissionsDTO, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'datasource_id'
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
                    " to method get_all_permissions" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['datasource_id']:
            _path_params['datasourceId'] = _params['datasource_id']


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
            '200': "DataSourcePermissionsDTO",
            '401': "ErrorResponseBody",
            '403': "ErrorResponseBody",
            '404': "ErrorResponseBody",
            '500': "ErrorResponseBody",
        }

        return self.api_client.call_api(
            '/datasources/{datasourceId}/permissions', 'GET',
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
