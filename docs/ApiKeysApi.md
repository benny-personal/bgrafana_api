# bgrafana_api.ApiKeysApi

All URIs are relative to *https://grafana-dev.nftgo.dev/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_ap_ikey**](ApiKeysApi.md#add_ap_ikey) | **POST** /auth/keys | Creates an API key.
[**delete_ap_ikey**](ApiKeysApi.md#delete_ap_ikey) | **DELETE** /auth/keys/{id} | Delete API key.
[**get_ap_ikeys**](ApiKeysApi.md#get_ap_ikeys) | **GET** /auth/keys | Get auth keys.


# **add_ap_ikey**
> NewApiKeyResult add_ap_ikey(add_command)

Creates an API key.

Will return details of the created API key.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.add_command import AddCommand
from bgrafana_api.models.new_api_key_result import NewApiKeyResult
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
    api_instance = bgrafana_api.ApiKeysApi(api_client)
    add_command = bgrafana_api.AddCommand() # AddCommand | 

    try:
        # Creates an API key.
        api_response = api_instance.add_ap_ikey(add_command)
        print("The response of ApiKeysApi->add_ap_ikey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->add_ap_ikey: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_command** | [**AddCommand**](AddCommand.md)|  | 

### Return type

[**NewApiKeyResult**](NewApiKeyResult.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | BadRequestError is returned when the request is invalid and it cannot be processed. |  -  |
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**409** | ConflictError |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ap_ikey**
> SuccessResponseBody delete_ap_ikey(id)

Delete API key.

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
    api_instance = bgrafana_api.ApiKeysApi(api_client)
    id = 56 # int | 

    try:
        # Delete API key.
        api_response = api_instance.delete_ap_ikey(id)
        print("The response of ApiKeysApi->delete_ap_ikey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->delete_ap_ikey: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

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
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ap_ikeys**
> List[ApiKeyDTO] get_ap_ikeys(include_expired=include_expired)

Get auth keys.

Will return auth keys.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.api_key_dto import ApiKeyDTO
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
    api_instance = bgrafana_api.ApiKeysApi(api_client)
    include_expired = False # bool | Show expired keys (optional) (default to False)

    try:
        # Get auth keys.
        api_response = api_instance.get_ap_ikeys(include_expired=include_expired)
        print("The response of ApiKeysApi->get_ap_ikeys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->get_ap_ikeys: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_expired** | **bool**| Show expired keys | [optional] [default to False]

### Return type

[**List[ApiKeyDTO]**](ApiKeyDTO.md)

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

