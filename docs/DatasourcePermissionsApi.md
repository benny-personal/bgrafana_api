# bgrafana_api.DatasourcePermissionsApi

All URIs are relative to *https://grafana-dev.nftgo.dev/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_permission**](DatasourcePermissionsApi.md#add_permission) | **POST** /datasources/{datasourceId}/permissions | Add permissions for a data source.
[**delete_permissions**](DatasourcePermissionsApi.md#delete_permissions) | **DELETE** /datasources/{datasourceId}/permissions/{permissionId} | Remove permission for a data source.
[**disable_permissions**](DatasourcePermissionsApi.md#disable_permissions) | **POST** /datasources/{datasourceId}/disable-permissions | Disable permissions for a data source.
[**enable_permissions**](DatasourcePermissionsApi.md#enable_permissions) | **POST** /datasources/{datasourceId}/enable-permissions | Enable permissions for a data source.
[**get_all_permissions**](DatasourcePermissionsApi.md#get_all_permissions) | **GET** /datasources/{datasourceId}/permissions | Get permissions for a data source.


# **add_permission**
> AddPermission200Response add_permission(datasource_id, user_id=user_id, team_id=team_id, builtin_role=builtin_role, permission=permission)

Add permissions for a data source.

You need to have a permission with action `datasources.permissions:read` and scopes `datasources:*`, `datasources:id:*`, `datasources:id:1` (single data source).

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.add_permission200_response import AddPermission200Response
from bgrafana_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://grafana-dev.nftgo.dev/api
# See configuration.py for a list of all supported configuration parameters.
configuration = bgrafana_api.Configuration(
    host = "https://grafana-dev.nftgo.dev/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure HTTP basic authorization: basic
configuration = bgrafana_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with bgrafana_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bgrafana_api.DatasourcePermissionsApi(api_client)
    datasource_id = 'datasource_id_example' # str | 
    user_id = 56 # int |  (optional)
    team_id = 56 # int |  (optional)
    builtin_role = 'builtin_role_example' # str |  (optional)
    permission = 56 # int |  (optional)

    try:
        # Add permissions for a data source.
        api_response = api_instance.add_permission(datasource_id, user_id=user_id, team_id=team_id, builtin_role=builtin_role, permission=permission)
        print("The response of DatasourcePermissionsApi->add_permission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasourcePermissionsApi->add_permission: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource_id** | **str**|  | 
 **user_id** | **int**|  | [optional] 
 **team_id** | **int**|  | [optional] 
 **builtin_role** | **str**|  | [optional] 
 **permission** | **int**|  | [optional] 

### Return type

[**AddPermission200Response**](AddPermission200Response.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_permissions**
> SuccessResponseBody delete_permissions(datasource_id, permission_id)

Remove permission for a data source.

Removes the permission with the given permissionId for the data source with the given id.  You need to have a permission with action `datasources.permissions:delete` and scopes `datasources:*`, `datasources:id:*`, `datasources:id:1` (single data source).

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.success_response_body import SuccessResponseBody
from bgrafana_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://grafana-dev.nftgo.dev/api
# See configuration.py for a list of all supported configuration parameters.
configuration = bgrafana_api.Configuration(
    host = "https://grafana-dev.nftgo.dev/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure HTTP basic authorization: basic
configuration = bgrafana_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with bgrafana_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bgrafana_api.DatasourcePermissionsApi(api_client)
    datasource_id = 'datasource_id_example' # str | 
    permission_id = 'permission_id_example' # str | 

    try:
        # Remove permission for a data source.
        api_response = api_instance.delete_permissions(datasource_id, permission_id)
        print("The response of DatasourcePermissionsApi->delete_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasourcePermissionsApi->delete_permissions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource_id** | **str**|  | 
 **permission_id** | **str**|  | 

### Return type

[**SuccessResponseBody**](SuccessResponseBody.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An OKResponse is returned if the request was successful. |  -  |
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_permissions**
> AddDataSource200Response disable_permissions(datasource_id)

Disable permissions for a data source.

Disables permissions for the data source with the given id. All existing permissions will be removed and anyone will be able to query the data source.  You need to have a permission with action `datasources.permissions:toggle` and scopes `datasources:*`, `datasources:id:*`, `datasources:id:1` (single data source).

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.add_data_source200_response import AddDataSource200Response
from bgrafana_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://grafana-dev.nftgo.dev/api
# See configuration.py for a list of all supported configuration parameters.
configuration = bgrafana_api.Configuration(
    host = "https://grafana-dev.nftgo.dev/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure HTTP basic authorization: basic
configuration = bgrafana_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with bgrafana_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bgrafana_api.DatasourcePermissionsApi(api_client)
    datasource_id = 'datasource_id_example' # str | 

    try:
        # Disable permissions for a data source.
        api_response = api_instance.disable_permissions(datasource_id)
        print("The response of DatasourcePermissionsApi->disable_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasourcePermissionsApi->disable_permissions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource_id** | **str**|  | 

### Return type

[**AddDataSource200Response**](AddDataSource200Response.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | BadRequestError is returned when the request is invalid and it cannot be processed. |  -  |
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_permissions**
> AddDataSource200Response enable_permissions(datasource_id)

Enable permissions for a data source.

Enables permissions for the data source with the given id. No one except Org Admins will be able to query the data source until permissions have been added which permit certain users or teams to query the data source.  You need to have a permission with action `datasources.permissions:toggle` and scopes `datasources:*`, `datasources:id:*`, `datasources:id:1` (single data source).

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.add_data_source200_response import AddDataSource200Response
from bgrafana_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://grafana-dev.nftgo.dev/api
# See configuration.py for a list of all supported configuration parameters.
configuration = bgrafana_api.Configuration(
    host = "https://grafana-dev.nftgo.dev/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure HTTP basic authorization: basic
configuration = bgrafana_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with bgrafana_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bgrafana_api.DatasourcePermissionsApi(api_client)
    datasource_id = 'datasource_id_example' # str | 

    try:
        # Enable permissions for a data source.
        api_response = api_instance.enable_permissions(datasource_id)
        print("The response of DatasourcePermissionsApi->enable_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasourcePermissionsApi->enable_permissions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource_id** | **str**|  | 

### Return type

[**AddDataSource200Response**](AddDataSource200Response.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | BadRequestError is returned when the request is invalid and it cannot be processed. |  -  |
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_permissions**
> DataSourcePermissionsDTO get_all_permissions(datasource_id)

Get permissions for a data source.

Gets all existing permissions for the data source with the given id.  You need to have a permission with action `datasources.permissions:read` and scopes `datasources:*`, `datasources:id:*`, `datasources:id:1` (single data source).

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.data_source_permissions_dto import DataSourcePermissionsDTO
from bgrafana_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://grafana-dev.nftgo.dev/api
# See configuration.py for a list of all supported configuration parameters.
configuration = bgrafana_api.Configuration(
    host = "https://grafana-dev.nftgo.dev/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure HTTP basic authorization: basic
configuration = bgrafana_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with bgrafana_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bgrafana_api.DatasourcePermissionsApi(api_client)
    datasource_id = 'datasource_id_example' # str | 

    try:
        # Get permissions for a data source.
        api_response = api_instance.get_all_permissions(datasource_id)
        print("The response of DatasourcePermissionsApi->get_all_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasourcePermissionsApi->get_all_permissions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource_id** | **str**|  | 

### Return type

[**DataSourcePermissionsDTO**](DataSourcePermissionsDTO.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

