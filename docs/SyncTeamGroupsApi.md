# bgrafana_api.SyncTeamGroupsApi

All URIs are relative to *https://grafana-dev.nftgo.dev/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_team_group_api**](SyncTeamGroupsApi.md#add_team_group_api) | **POST** /teams/{teamId}/groups | Add External Group.
[**get_team_groups_api**](SyncTeamGroupsApi.md#get_team_groups_api) | **GET** /teams/{teamId}/groups | Get External Groups.
[**remove_team_group_api**](SyncTeamGroupsApi.md#remove_team_group_api) | **DELETE** /teams/{teamId}/groups/{groupId} | Remove External Group.


# **add_team_group_api**
> SuccessResponseBody add_team_group_api(team_id, team_group_mapping)

Add External Group.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.success_response_body import SuccessResponseBody
from bgrafana_api.models.team_group_mapping import TeamGroupMapping
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
    api_instance = bgrafana_api.SyncTeamGroupsApi(api_client)
    team_id = 56 # int | 
    team_group_mapping = bgrafana_api.TeamGroupMapping() # TeamGroupMapping | 

    try:
        # Add External Group.
        api_response = api_instance.add_team_group_api(team_id, team_group_mapping)
        print("The response of SyncTeamGroupsApi->add_team_group_api:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyncTeamGroupsApi->add_team_group_api: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**|  | 
 **team_group_mapping** | [**TeamGroupMapping**](TeamGroupMapping.md)|  | 

### Return type

[**SuccessResponseBody**](SuccessResponseBody.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An OKResponse is returned if the request was successful. |  -  |
**400** | BadRequestError is returned when the request is invalid and it cannot be processed. |  -  |
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_groups_api**
> List[TeamGroupDTO] get_team_groups_api(team_id)

Get External Groups.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.team_group_dto import TeamGroupDTO
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
    api_instance = bgrafana_api.SyncTeamGroupsApi(api_client)
    team_id = 56 # int | 

    try:
        # Get External Groups.
        api_response = api_instance.get_team_groups_api(team_id)
        print("The response of SyncTeamGroupsApi->get_team_groups_api:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyncTeamGroupsApi->get_team_groups_api: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**|  | 

### Return type

[**List[TeamGroupDTO]**](TeamGroupDTO.md)

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

# **remove_team_group_api**
> SuccessResponseBody remove_team_group_api(group_id, team_id)

Remove External Group.

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
    api_instance = bgrafana_api.SyncTeamGroupsApi(api_client)
    group_id = 'group_id_example' # str | 
    team_id = 56 # int | 

    try:
        # Remove External Group.
        api_response = api_instance.remove_team_group_api(group_id, team_id)
        print("The response of SyncTeamGroupsApi->remove_team_group_api:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyncTeamGroupsApi->remove_team_group_api: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **team_id** | **int**|  | 

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
**400** | BadRequestError is returned when the request is invalid and it cannot be processed. |  -  |
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

