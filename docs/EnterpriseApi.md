# bgrafana_api.EnterpriseApi

All URIs are relative to *https://grafana-dev.nftgo.dev/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_permission**](EnterpriseApi.md#add_permission) | **POST** /datasources/{datasourceId}/permissions | Add permissions for a data source.
[**add_team_group_api**](EnterpriseApi.md#add_team_group_api) | **POST** /teams/{teamId}/groups | Add External Group.
[**add_team_role**](EnterpriseApi.md#add_team_role) | **POST** /access-control/teams/{teamId}/roles | Add team role.
[**add_user_role**](EnterpriseApi.md#add_user_role) | **POST** /access-control/users/{userId}/roles | Add a user role assignment.
[**admin_provisioning_reload_access_control**](EnterpriseApi.md#admin_provisioning_reload_access_control) | **POST** /admin/provisioning/access-control/reload | You need to have a permission with action &#x60;provisioning:reload&#x60; with scope &#x60;provisioners:accesscontrol&#x60;.
[**create_recording_rule**](EnterpriseApi.md#create_recording_rule) | **POST** /recording-rules | Create a recording rule that is then registered and started.
[**create_recording_rule_write_target**](EnterpriseApi.md#create_recording_rule_write_target) | **POST** /recording-rules/writer | Create a remote write target.
[**create_report**](EnterpriseApi.md#create_report) | **POST** /reports | Create a report.
[**create_role**](EnterpriseApi.md#create_role) | **POST** /access-control/roles | Create a new custom role.
[**delete_license_token**](EnterpriseApi.md#delete_license_token) | **DELETE** /licensing/token | Remove license from database.
[**delete_permissions**](EnterpriseApi.md#delete_permissions) | **DELETE** /datasources/{datasourceId}/permissions/{permissionId} | Remove permission for a data source.
[**delete_recording_rule**](EnterpriseApi.md#delete_recording_rule) | **DELETE** /recording-rules/{recordingRuleID} | Delete removes the rule from the registry and stops it.
[**delete_recording_rule_write_target**](EnterpriseApi.md#delete_recording_rule_write_target) | **DELETE** /recording-rules/writer | Delete the remote write target.
[**delete_report**](EnterpriseApi.md#delete_report) | **DELETE** /reports/{id} | Delete a report.
[**delete_role**](EnterpriseApi.md#delete_role) | **DELETE** /access-control/roles/{roleUID} | Delete a custom role.
[**disable_permissions**](EnterpriseApi.md#disable_permissions) | **POST** /datasources/{datasourceId}/disable-permissions | Disable permissions for a data source.
[**enable_permissions**](EnterpriseApi.md#enable_permissions) | **POST** /datasources/{datasourceId}/enable-permissions | Enable permissions for a data source.
[**get_access_control_status**](EnterpriseApi.md#get_access_control_status) | **GET** /access-control/status | Get status.
[**get_all_permissions**](EnterpriseApi.md#get_all_permissions) | **GET** /datasources/{datasourceId}/permissions | Get permissions for a data source.
[**get_custom_permissions_csv**](EnterpriseApi.md#get_custom_permissions_csv) | **GET** /licensing/custom-permissions-csv | Get custom permissions report in CSV format.
[**get_custom_permissions_report**](EnterpriseApi.md#get_custom_permissions_report) | **GET** /licensing/custom-permissions | Get custom permissions report.
[**get_license_token**](EnterpriseApi.md#get_license_token) | **GET** /licensing/token | Get license token.
[**get_metadata**](EnterpriseApi.md#get_metadata) | **GET** /saml/metadata | It exposes the SP (Grafana&#39;s) metadata for the IdP&#39;s consumption.
[**get_recording_rule_write_target**](EnterpriseApi.md#get_recording_rule_write_target) | **GET** /recording-rules/writer | Return the prometheus remote write target.
[**get_report**](EnterpriseApi.md#get_report) | **GET** /reports/{id} | Get a report.
[**get_report_settings**](EnterpriseApi.md#get_report_settings) | **GET** /reports/settings | Get settings.
[**get_reports**](EnterpriseApi.md#get_reports) | **GET** /reports | List reports.
[**get_role**](EnterpriseApi.md#get_role) | **GET** /access-control/roles/{roleUID} | Get a role.
[**get_role_assignments**](EnterpriseApi.md#get_role_assignments) | **GET** /access-control/roles/{roleUID}/assignments | Get role assignments.
[**get_saml_logout**](EnterpriseApi.md#get_saml_logout) | **GET** /logout/saml | GetLogout initiates single logout process.
[**get_slo**](EnterpriseApi.md#get_slo) | **GET** /saml/slo | It performs Single Logout (SLO) callback.
[**get_status**](EnterpriseApi.md#get_status) | **GET** /licensing/check | Check license availability.
[**get_team_groups_api**](EnterpriseApi.md#get_team_groups_api) | **GET** /teams/{teamId}/groups | Get External Groups.
[**list_recording_rules**](EnterpriseApi.md#list_recording_rules) | **GET** /recording-rules | Lists all rules in the database: active or deleted.
[**list_roles**](EnterpriseApi.md#list_roles) | **GET** /access-control/roles | Get all roles.
[**list_team_roles**](EnterpriseApi.md#list_team_roles) | **GET** /access-control/teams/{teamId}/roles | Get team roles.
[**list_user_roles**](EnterpriseApi.md#list_user_roles) | **GET** /access-control/users/{userId}/roles | List roles assigned to a user.
[**post_acs**](EnterpriseApi.md#post_acs) | **POST** /saml/acs | It performs assertion Consumer Service (ACS).
[**post_license_token**](EnterpriseApi.md#post_license_token) | **POST** /licensing/token | Create license token.
[**post_renew_license_token**](EnterpriseApi.md#post_renew_license_token) | **POST** /licensing/token/renew | Manually force license refresh.
[**post_slo**](EnterpriseApi.md#post_slo) | **POST** /saml/slo | It performs Single Logout (SLO) callback.
[**refresh_license_stats**](EnterpriseApi.md#refresh_license_stats) | **GET** /licensing/refresh-stats | Refresh license stats.
[**remove_team_group_api**](EnterpriseApi.md#remove_team_group_api) | **DELETE** /teams/{teamId}/groups/{groupId} | Remove External Group.
[**remove_team_role**](EnterpriseApi.md#remove_team_role) | **DELETE** /access-control/teams/{teamId}/roles/{roleUID} | Remove team role.
[**remove_user_role**](EnterpriseApi.md#remove_user_role) | **DELETE** /access-control/users/{userId}/roles/{roleUID} | Remove a user role assignment.
[**render_report_pdf**](EnterpriseApi.md#render_report_pdf) | **GET** /reports/render/pdf/{dashboardID} | Render report for dashboard.
[**render_report_pdfs**](EnterpriseApi.md#render_report_pdfs) | **GET** /reports/render/pdfs | Render report for multiple dashboards.
[**save_report_settings**](EnterpriseApi.md#save_report_settings) | **POST** /reports/settings | Save settings.
[**search_result**](EnterpriseApi.md#search_result) | **POST** /access-control/assignments/search | Debug permissions.
[**send_report**](EnterpriseApi.md#send_report) | **POST** /reports/email | Send a report.
[**send_test_email**](EnterpriseApi.md#send_test_email) | **POST** /reports/test-email | Send test report via email.
[**set_role_assignments**](EnterpriseApi.md#set_role_assignments) | **PUT** /access-control/roles/{roleUID}/assignments | Set role assignments.
[**set_team_roles**](EnterpriseApi.md#set_team_roles) | **PUT** /access-control/teams/{teamId}/roles | Update team role.
[**set_user_roles**](EnterpriseApi.md#set_user_roles) | **PUT** /access-control/users/{userId}/roles | Set user role assignments.
[**test_create_recording_rule**](EnterpriseApi.md#test_create_recording_rule) | **POST** /recording-rules/test | Test a recording rule.
[**update_recording_rule**](EnterpriseApi.md#update_recording_rule) | **PUT** /recording-rules | Update the active status of a rule.
[**update_report**](EnterpriseApi.md#update_report) | **PUT** /reports/{id} | Update a report.
[**update_role**](EnterpriseApi.md#update_role) | **PUT** /access-control/roles/{roleUID} | Update a custom role.


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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    datasource_id = 'datasource_id_example' # str | 
    user_id = 56 # int |  (optional)
    team_id = 56 # int |  (optional)
    builtin_role = 'builtin_role_example' # str |  (optional)
    permission = 56 # int |  (optional)

    try:
        # Add permissions for a data source.
        api_response = api_instance.add_permission(datasource_id, user_id=user_id, team_id=team_id, builtin_role=builtin_role, permission=permission)
        print("The response of EnterpriseApi->add_permission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->add_permission: %s\n" % e)
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    team_id = 56 # int | 
    team_group_mapping = bgrafana_api.TeamGroupMapping() # TeamGroupMapping | 

    try:
        # Add External Group.
        api_response = api_instance.add_team_group_api(team_id, team_group_mapping)
        print("The response of EnterpriseApi->add_team_group_api:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->add_team_group_api: %s\n" % e)
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

# **add_team_role**
> SuccessResponseBody add_team_role(team_id, add_team_role_command)

Add team role.

You need to have a permission with action `teams.roles:add` and scope `permissions:type:delegate`.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.add_team_role_command import AddTeamRoleCommand
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    team_id = 56 # int | 
    add_team_role_command = bgrafana_api.AddTeamRoleCommand() # AddTeamRoleCommand | 

    try:
        # Add team role.
        api_response = api_instance.add_team_role(team_id, add_team_role_command)
        print("The response of EnterpriseApi->add_team_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->add_team_role: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**|  | 
 **add_team_role_command** | [**AddTeamRoleCommand**](AddTeamRoleCommand.md)|  | 

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
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_user_role**
> SuccessResponseBody add_user_role(user_id, add_user_role_command)

Add a user role assignment.

Assign a role to a specific user. For bulk updates consider Set user role assignments.  You need to have a permission with action `users.roles:add` and scope `permissions:type:delegate`. `permissions:type:delegate` scope ensures that users can only assign roles which have same, or a subset of permissions which the user has. For example, if a user does not have required permissions for creating users, they won’t be able to assign a role which will allow to do that. This is done to prevent escalation of privileges.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.add_user_role_command import AddUserRoleCommand
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    user_id = 56 # int | 
    add_user_role_command = bgrafana_api.AddUserRoleCommand() # AddUserRoleCommand | 

    try:
        # Add a user role assignment.
        api_response = api_instance.add_user_role(user_id, add_user_role_command)
        print("The response of EnterpriseApi->add_user_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->add_user_role: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **add_user_role_command** | [**AddUserRoleCommand**](AddUserRoleCommand.md)|  | 

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
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_provisioning_reload_access_control**
> ErrorResponseBody admin_provisioning_reload_access_control()

You need to have a permission with action `provisioning:reload` with scope `provisioners:accesscontrol`.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.error_response_body import ErrorResponseBody
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)

    try:
        # You need to have a permission with action `provisioning:reload` with scope `provisioners:accesscontrol`.
        api_response = api_instance.admin_provisioning_reload_access_control()
        print("The response of EnterpriseApi->admin_provisioning_reload_access_control:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->admin_provisioning_reload_access_control: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ErrorResponseBody**](ErrorResponseBody.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | AcceptedResponse |  -  |
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_recording_rule**
> RecordingRuleJSON create_recording_rule(recording_rule_json)

Create a recording rule that is then registered and started.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.recording_rule_json import RecordingRuleJSON
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    recording_rule_json = bgrafana_api.RecordingRuleJSON() # RecordingRuleJSON | 

    try:
        # Create a recording rule that is then registered and started.
        api_response = api_instance.create_recording_rule(recording_rule_json)
        print("The response of EnterpriseApi->create_recording_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->create_recording_rule: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_rule_json** | [**RecordingRuleJSON**](RecordingRuleJSON.md)|  | 

### Return type

[**RecordingRuleJSON**](RecordingRuleJSON.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
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

# **create_recording_rule_write_target**
> PrometheusRemoteWriteTargetJSON create_recording_rule_write_target(prometheus_remote_write_target_json)

Create a remote write target.

It returns a 422 if there is not an existing prometheus data source configured.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.prometheus_remote_write_target_json import PrometheusRemoteWriteTargetJSON
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    prometheus_remote_write_target_json = bgrafana_api.PrometheusRemoteWriteTargetJSON() # PrometheusRemoteWriteTargetJSON | 

    try:
        # Create a remote write target.
        api_response = api_instance.create_recording_rule_write_target(prometheus_remote_write_target_json)
        print("The response of EnterpriseApi->create_recording_rule_write_target:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->create_recording_rule_write_target: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prometheus_remote_write_target_json** | [**PrometheusRemoteWriteTargetJSON**](PrometheusRemoteWriteTargetJSON.md)|  | 

### Return type

[**PrometheusRemoteWriteTargetJSON**](PrometheusRemoteWriteTargetJSON.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**422** | UnprocessableEntityError |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_report**
> CreateReport200Response create_report(create_or_update_config_cmd)

Create a report.

Available to org admins only and with a valid license.  You need to have a permission with action `reports.admin:create`.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.create_or_update_config_cmd import CreateOrUpdateConfigCmd
from bgrafana_api.models.create_report200_response import CreateReport200Response
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    create_or_update_config_cmd = bgrafana_api.CreateOrUpdateConfigCmd() # CreateOrUpdateConfigCmd | 

    try:
        # Create a report.
        api_response = api_instance.create_report(create_or_update_config_cmd)
        print("The response of EnterpriseApi->create_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->create_report: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_or_update_config_cmd** | [**CreateOrUpdateConfigCmd**](CreateOrUpdateConfigCmd.md)|  | 

### Return type

[**CreateReport200Response**](CreateReport200Response.md)

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
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_role**
> RoleDTO create_role(create_role_form)

Create a new custom role.

Creates a new custom role and maps given permissions to that role. Note that roles with the same prefix as Fixed Roles can’t be created.  You need to have a permission with action `roles:write` and scope `permissions:type:delegate`. `permissions:type:delegate` scope ensures that users can only create custom roles with the same, or a subset of permissions which the user has. For example, if a user does not have required permissions for creating users, they won’t be able to create a custom role which allows to do that. This is done to prevent escalation of privileges.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.create_role_form import CreateRoleForm
from bgrafana_api.models.role_dto import RoleDTO
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    create_role_form = bgrafana_api.CreateRoleForm() # CreateRoleForm | 

    try:
        # Create a new custom role.
        api_response = api_instance.create_role(create_role_form)
        print("The response of EnterpriseApi->create_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->create_role: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_role_form** | [**CreateRoleForm**](CreateRoleForm.md)|  | 

### Return type

[**RoleDTO**](RoleDTO.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | (empty) |  -  |
**400** | BadRequestError is returned when the request is invalid and it cannot be processed. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_license_token**
> ErrorResponseBody delete_license_token(delete_token_command)

Remove license from database.

Removes the license stored in the Grafana database. Available in Grafana Enterprise v7.4+.  You need to have a permission with action `licensing:delete`.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.delete_token_command import DeleteTokenCommand
from bgrafana_api.models.error_response_body import ErrorResponseBody
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    delete_token_command = bgrafana_api.DeleteTokenCommand() # DeleteTokenCommand | 

    try:
        # Remove license from database.
        api_response = api_instance.delete_license_token(delete_token_command)
        print("The response of EnterpriseApi->delete_license_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->delete_license_token: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_token_command** | [**DeleteTokenCommand**](DeleteTokenCommand.md)|  | 

### Return type

[**ErrorResponseBody**](ErrorResponseBody.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | AcceptedResponse |  -  |
**400** | BadRequestError is returned when the request is invalid and it cannot be processed. |  -  |
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**422** | UnprocessableEntityError |  -  |
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    datasource_id = 'datasource_id_example' # str | 
    permission_id = 'permission_id_example' # str | 

    try:
        # Remove permission for a data source.
        api_response = api_instance.delete_permissions(datasource_id, permission_id)
        print("The response of EnterpriseApi->delete_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->delete_permissions: %s\n" % e)
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

# **delete_recording_rule**
> SuccessResponseBody delete_recording_rule(recording_rule_id)

Delete removes the rule from the registry and stops it.

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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    recording_rule_id = 56 # int | 

    try:
        # Delete removes the rule from the registry and stops it.
        api_response = api_instance.delete_recording_rule(recording_rule_id)
        print("The response of EnterpriseApi->delete_recording_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->delete_recording_rule: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_rule_id** | **int**|  | 

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

# **delete_recording_rule_write_target**
> SuccessResponseBody delete_recording_rule_write_target()

Delete the remote write target.

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
    api_instance = bgrafana_api.EnterpriseApi(api_client)

    try:
        # Delete the remote write target.
        api_response = api_instance.delete_recording_rule_write_target()
        print("The response of EnterpriseApi->delete_recording_rule_write_target:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->delete_recording_rule_write_target: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

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

# **delete_report**
> SuccessResponseBody delete_report(id)

Delete a report.

Available to org admins only and with a valid or expired license.  You need to have a permission with action `reports.delete` with scope `reports:id:<report ID>`.

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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    id = 56 # int | 

    try:
        # Delete a report.
        api_response = api_instance.delete_report(id)
        print("The response of EnterpriseApi->delete_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->delete_report: %s\n" % e)
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
**400** | BadRequestError is returned when the request is invalid and it cannot be processed. |  -  |
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role**
> SuccessResponseBody delete_role(role_uid, force=force, var_global=var_global)

Delete a custom role.

Delete a role with the given UID, and it’s permissions. If the role is assigned to a built-in role, the deletion operation will fail, unless force query param is set to true, and in that case all assignments will also be deleted.  You need to have a permission with action `roles:delete` and scope `permissions:type:delegate`. `permissions:type:delegate` scope ensures that users can only delete a custom role with the same, or a subset of permissions which the user has. For example, if a user does not have required permissions for creating users, they won’t be able to delete a custom role which allows to do that.

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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    role_uid = 'role_uid_example' # str | 
    force = True # bool |  (optional)
    var_global = True # bool |  (optional)

    try:
        # Delete a custom role.
        api_response = api_instance.delete_role(role_uid, force=force, var_global=var_global)
        print("The response of EnterpriseApi->delete_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->delete_role: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_uid** | **str**|  | 
 **force** | **bool**|  | [optional] 
 **var_global** | **bool**|  | [optional] 

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
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    datasource_id = 'datasource_id_example' # str | 

    try:
        # Disable permissions for a data source.
        api_response = api_instance.disable_permissions(datasource_id)
        print("The response of EnterpriseApi->disable_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->disable_permissions: %s\n" % e)
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    datasource_id = 'datasource_id_example' # str | 

    try:
        # Enable permissions for a data source.
        api_response = api_instance.enable_permissions(datasource_id)
        print("The response of EnterpriseApi->enable_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->enable_permissions: %s\n" % e)
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

# **get_access_control_status**
> int get_access_control_status()

Get status.

Returns an indicator to check if fine-grained access control is enabled or not.  You need to have a permission with action `status:accesscontrol` and scope `services:accesscontrol`.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)

    try:
        # Get status.
        api_response = api_instance.get_access_control_status()
        print("The response of EnterpriseApi->get_access_control_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->get_access_control_status: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**int**

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    datasource_id = 'datasource_id_example' # str | 

    try:
        # Get permissions for a data source.
        api_response = api_instance.get_all_permissions(datasource_id)
        print("The response of EnterpriseApi->get_all_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->get_all_permissions: %s\n" % e)
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

# **get_custom_permissions_csv**
> List[CustomPermissionsRecordDTO] get_custom_permissions_csv()

Get custom permissions report in CSV format.

You need to have a permission with action `licensing.reports:read`.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.custom_permissions_record_dto import CustomPermissionsRecordDTO
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)

    try:
        # Get custom permissions report in CSV format.
        api_response = api_instance.get_custom_permissions_csv()
        print("The response of EnterpriseApi->get_custom_permissions_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->get_custom_permissions_csv: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[CustomPermissionsRecordDTO]**](CustomPermissionsRecordDTO.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_permissions_report**
> List[CustomPermissionsRecordDTO] get_custom_permissions_report()

Get custom permissions report.

You need to have a permission with action `licensing.reports:read`.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.custom_permissions_record_dto import CustomPermissionsRecordDTO
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)

    try:
        # Get custom permissions report.
        api_response = api_instance.get_custom_permissions_report()
        print("The response of EnterpriseApi->get_custom_permissions_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->get_custom_permissions_report: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[CustomPermissionsRecordDTO]**](CustomPermissionsRecordDTO.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license_token**
> Token get_license_token()

Get license token.

You need to have a permission with action `licensing:read`.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.token import Token
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)

    try:
        # Get license token.
        api_response = api_instance.get_license_token()
        print("The response of EnterpriseApi->get_license_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->get_license_token: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**Token**](Token.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata**
> List[int] get_metadata()

It exposes the SP (Grafana's) metadata for the IdP's consumption.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)

    try:
        # It exposes the SP (Grafana's) metadata for the IdP's consumption.
        api_response = api_instance.get_metadata()
        print("The response of EnterpriseApi->get_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->get_metadata: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**List[int]**

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recording_rule_write_target**
> PrometheusRemoteWriteTargetJSON get_recording_rule_write_target()

Return the prometheus remote write target.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.prometheus_remote_write_target_json import PrometheusRemoteWriteTargetJSON
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)

    try:
        # Return the prometheus remote write target.
        api_response = api_instance.get_recording_rule_write_target()
        print("The response of EnterpriseApi->get_recording_rule_write_target:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->get_recording_rule_write_target: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**PrometheusRemoteWriteTargetJSON**](PrometheusRemoteWriteTargetJSON.md)

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

# **get_report**
> ConfigDTO get_report(id)

Get a report.

Available to org admins only and with a valid or expired license.  You need to have a permission with action `reports:read` with scope `reports:id:<report ID>`.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.config_dto import ConfigDTO
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    id = 56 # int | 

    try:
        # Get a report.
        api_response = api_instance.get_report(id)
        print("The response of EnterpriseApi->get_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->get_report: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ConfigDTO**](ConfigDTO.md)

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

# **get_report_settings**
> SettingsDTO get_report_settings()

Get settings.

Available to org admins only and with a valid or expired license.  You need to have a permission with action `reports.settings:read`x.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.settings_dto import SettingsDTO
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)

    try:
        # Get settings.
        api_response = api_instance.get_report_settings()
        print("The response of EnterpriseApi->get_report_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->get_report_settings: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**SettingsDTO**](SettingsDTO.md)

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
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reports**
> List[ConfigDTO] get_reports()

List reports.

Available to org admins only and with a valid or expired license.  You need to have a permission with action `reports:read` with scope `reports:*`.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.config_dto import ConfigDTO
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)

    try:
        # List reports.
        api_response = api_instance.get_reports()
        print("The response of EnterpriseApi->get_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->get_reports: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[ConfigDTO]**](ConfigDTO.md)

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
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role**
> RoleDTO get_role(role_uid)

Get a role.

Get a role for the given UID.  You need to have a permission with action `roles:read` and scope `roles:*`.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.role_dto import RoleDTO
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    role_uid = 'role_uid_example' # str | 

    try:
        # Get a role.
        api_response = api_instance.get_role(role_uid)
        print("The response of EnterpriseApi->get_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->get_role: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_uid** | **str**|  | 

### Return type

[**RoleDTO**](RoleDTO.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_assignments**
> RoleAssignmentsDTO get_role_assignments(role_uid)

Get role assignments.

Get role assignments for the role with the given UID.  You need to have a permission with action `teams.roles:list` and scope `teams:id:*` and `users.roles:list` and scope `users:id:*`.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.role_assignments_dto import RoleAssignmentsDTO
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    role_uid = 'role_uid_example' # str | 

    try:
        # Get role assignments.
        api_response = api_instance.get_role_assignments(role_uid)
        print("The response of EnterpriseApi->get_role_assignments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->get_role_assignments: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_uid** | **str**|  | 

### Return type

[**RoleAssignmentsDTO**](RoleAssignmentsDTO.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_saml_logout**
> get_saml_logout()

GetLogout initiates single logout process.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)

    try:
        # GetLogout initiates single logout process.
        api_instance.get_saml_logout()
    except Exception as e:
        print("Exception when calling EnterpriseApi->get_saml_logout: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | (empty) |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_slo**
> get_slo()

It performs Single Logout (SLO) callback.

There might be two possible requests: 1. Logout response (callback) when Grafana initiates single logout and IdP returns response to logout request. 2. Logout request when another SP initiates single logout and IdP sends logout request to the Grafana, or in case of IdP-initiated logout.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)

    try:
        # It performs Single Logout (SLO) callback.
        api_instance.get_slo()
    except Exception as e:
        print("Exception when calling EnterpriseApi->get_slo: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | (empty) |  -  |
**400** | BadRequestError is returned when the request is invalid and it cannot be processed. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status**
> get_status()

Check license availability.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)

    try:
        # Check license availability.
        api_instance.get_status()
    except Exception as e:
        print("Exception when calling EnterpriseApi->get_status: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |

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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    team_id = 56 # int | 

    try:
        # Get External Groups.
        api_response = api_instance.get_team_groups_api(team_id)
        print("The response of EnterpriseApi->get_team_groups_api:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->get_team_groups_api: %s\n" % e)
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

# **list_recording_rules**
> List[RecordingRuleJSON] list_recording_rules()

Lists all rules in the database: active or deleted.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.recording_rule_json import RecordingRuleJSON
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)

    try:
        # Lists all rules in the database: active or deleted.
        api_response = api_instance.list_recording_rules()
        print("The response of EnterpriseApi->list_recording_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->list_recording_rules: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[RecordingRuleJSON]**](RecordingRuleJSON.md)

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

# **list_roles**
> List[RoleDTO] list_roles(delegatable=delegatable)

Get all roles.

Gets all existing roles. The response contains all global and organization local roles, for the organization which user is signed in.  You need to have a permission with action `roles:read` and scope `roles:*`.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.role_dto import RoleDTO
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    delegatable = True # bool |  (optional)

    try:
        # Get all roles.
        api_response = api_instance.list_roles(delegatable=delegatable)
        print("The response of EnterpriseApi->list_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->list_roles: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegatable** | **bool**|  | [optional] 

### Return type

[**List[RoleDTO]**](RoleDTO.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_team_roles**
> SuccessResponseBody list_team_roles(team_id)

Get team roles.

You need to have a permission with action `teams.roles:read` and scope `teams:id:<team ID>`.

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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    team_id = 56 # int | 

    try:
        # Get team roles.
        api_response = api_instance.list_team_roles(team_id)
        print("The response of EnterpriseApi->list_team_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->list_team_roles: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_roles**
> List[RoleDTO] list_user_roles(user_id)

List roles assigned to a user.

Lists the roles that have been directly assigned to a given user. The list does not include built-in roles (Viewer, Editor, Admin or Grafana Admin), and it does not include roles that have been inherited from a team.  You need to have a permission with action `users.roles:read` and scope `users:id:<user ID>`.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.role_dto import RoleDTO
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    user_id = 56 # int | 

    try:
        # List roles assigned to a user.
        api_response = api_instance.list_user_roles(user_id)
        print("The response of EnterpriseApi->list_user_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->list_user_roles: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**List[RoleDTO]**](RoleDTO.md)

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
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_acs**
> post_acs(relay_state=relay_state)

It performs assertion Consumer Service (ACS).

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    relay_state = 'relay_state_example' # str |  (optional)

    try:
        # It performs assertion Consumer Service (ACS).
        api_instance.post_acs(relay_state=relay_state)
    except Exception as e:
        print("Exception when calling EnterpriseApi->post_acs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relay_state** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | (empty) |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_license_token**
> Token post_license_token(delete_token_command)

Create license token.

You need to have a permission with action `licensing:update`.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.delete_token_command import DeleteTokenCommand
from bgrafana_api.models.token import Token
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    delete_token_command = bgrafana_api.DeleteTokenCommand() # DeleteTokenCommand | 

    try:
        # Create license token.
        api_response = api_instance.post_license_token(delete_token_command)
        print("The response of EnterpriseApi->post_license_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->post_license_token: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_token_command** | [**DeleteTokenCommand**](DeleteTokenCommand.md)|  | 

### Return type

[**Token**](Token.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_renew_license_token**
> post_renew_license_token(body)

Manually force license refresh.

Manually ask license issuer for a new token. Available in Grafana Enterprise v7.4+.  You need to have a permission with action `licensing:update`.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    body = None # object | 

    try:
        # Manually force license refresh.
        api_instance.post_renew_license_token(body)
    except Exception as e:
        print("Exception when calling EnterpriseApi->post_renew_license_token: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_slo**
> post_slo(saml_request=saml_request, saml_response=saml_response)

It performs Single Logout (SLO) callback.

There might be two possible requests: 1. Logout response (callback) when Grafana initiates single logout and IdP returns response to logout request. 2. Logout request when another SP initiates single logout and IdP sends logout request to the Grafana, or in case of IdP-initiated logout.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    saml_request = 'saml_request_example' # str |  (optional)
    saml_response = 'saml_response_example' # str |  (optional)

    try:
        # It performs Single Logout (SLO) callback.
        api_instance.post_slo(saml_request=saml_request, saml_response=saml_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->post_slo: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **saml_request** | **str**|  | [optional] 
 **saml_response** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | (empty) |  -  |
**400** | BadRequestError is returned when the request is invalid and it cannot be processed. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_license_stats**
> ActiveUserStats refresh_license_stats()

Refresh license stats.

You need to have a permission with action `licensing:read`.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.active_user_stats import ActiveUserStats
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)

    try:
        # Refresh license stats.
        api_response = api_instance.refresh_license_stats()
        print("The response of EnterpriseApi->refresh_license_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->refresh_license_stats: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ActiveUserStats**](ActiveUserStats.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    group_id = 'group_id_example' # str | 
    team_id = 56 # int | 

    try:
        # Remove External Group.
        api_response = api_instance.remove_team_group_api(group_id, team_id)
        print("The response of EnterpriseApi->remove_team_group_api:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->remove_team_group_api: %s\n" % e)
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

# **remove_team_role**
> SuccessResponseBody remove_team_role(role_uid, team_id)

Remove team role.

You need to have a permission with action `teams.roles:remove` and scope `permissions:type:delegate`.

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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    role_uid = 'role_uid_example' # str | 
    team_id = 56 # int | 

    try:
        # Remove team role.
        api_response = api_instance.remove_team_role(role_uid, team_id)
        print("The response of EnterpriseApi->remove_team_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->remove_team_role: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_uid** | **str**|  | 
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
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_role**
> SuccessResponseBody remove_user_role(role_uid, user_id, var_global=var_global)

Remove a user role assignment.

Revoke a role from a user. For bulk updates consider Set user role assignments.  You need to have a permission with action `users.roles:remove` and scope `permissions:type:delegate`. `permissions:type:delegate` scope ensures that users can only unassign roles which have same, or a subset of permissions which the user has. For example, if a user does not have required permissions for creating users, they won’t be able to unassign a role which will allow to do that. This is done to prevent escalation of privileges.

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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    role_uid = 'role_uid_example' # str | 
    user_id = 56 # int | 
    var_global = True # bool | A flag indicating if the assignment is global or not. If set to false, the default org ID of the authenticated user will be used from the request to remove assignment. (optional)

    try:
        # Remove a user role assignment.
        api_response = api_instance.remove_user_role(role_uid, user_id, var_global=var_global)
        print("The response of EnterpriseApi->remove_user_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->remove_user_role: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_uid** | **str**|  | 
 **user_id** | **int**|  | 
 **var_global** | **bool**| A flag indicating if the assignment is global or not. If set to false, the default org ID of the authenticated user will be used from the request to remove assignment. | [optional] 

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
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_report_pdf**
> List[int] render_report_pdf(dashboard_id, dashboard_id2, title=title, variables=variables, var_from=var_from, to=to, orientation=orientation, layout=layout)

Render report for dashboard.

Please refer to [reports enterprise](#/reports/renderReportPDFs) instead. This will be removed in Grafana 10.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    dashboard_id = 56 # int | 
    dashboard_id2 = 56 # int | 
    title = 'title_example' # str |  (optional)
    variables = 'variables_example' # str |  (optional)
    var_from = 'var_from_example' # str |  (optional)
    to = 'to_example' # str |  (optional)
    orientation = 'orientation_example' # str |  (optional)
    layout = 'layout_example' # str |  (optional)

    try:
        # Render report for dashboard.
        api_response = api_instance.render_report_pdf(dashboard_id, dashboard_id2, title=title, variables=variables, var_from=var_from, to=to, orientation=orientation, layout=layout)
        print("The response of EnterpriseApi->render_report_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->render_report_pdf: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **int**|  | 
 **dashboard_id2** | **int**|  | 
 **title** | **str**|  | [optional] 
 **variables** | **str**|  | [optional] 
 **var_from** | **str**|  | [optional] 
 **to** | **str**|  | [optional] 
 **orientation** | **str**|  | [optional] 
 **layout** | **str**|  | [optional] 

### Return type

**List[int]**

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
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_report_pdfs**
> List[int] render_report_pdfs(dashboard_id=dashboard_id, orientation=orientation, layout=layout)

Render report for multiple dashboards.

Available to all users and with a valid license.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    dashboard_id = 'dashboard_id_example' # str |  (optional)
    orientation = 'orientation_example' # str |  (optional)
    layout = 'layout_example' # str |  (optional)

    try:
        # Render report for multiple dashboards.
        api_response = api_instance.render_report_pdfs(dashboard_id=dashboard_id, orientation=orientation, layout=layout)
        print("The response of EnterpriseApi->render_report_pdfs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->render_report_pdfs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**|  | [optional] 
 **orientation** | **str**|  | [optional] 
 **layout** | **str**|  | [optional] 

### Return type

**List[int]**

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
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_report_settings**
> SuccessResponseBody save_report_settings(settings_dto)

Save settings.

Available to org admins only and with a valid or expired license.  You need to have a permission with action `reports.settings:write`xx.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.settings_dto import SettingsDTO
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    settings_dto = bgrafana_api.SettingsDTO() # SettingsDTO | 

    try:
        # Save settings.
        api_response = api_instance.save_report_settings(settings_dto)
        print("The response of EnterpriseApi->save_report_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->save_report_settings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_dto** | [**SettingsDTO**](SettingsDTO.md)|  | 

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
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_result**
> SearchResult search_result()

Debug permissions.

Returns the result of the search through access-control role assignments.  You need to have a permission with action `teams.roles:read` on scope `teams:*` and a permission with action `users.roles:read` on scope `users:*`.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.search_result import SearchResult
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)

    try:
        # Debug permissions.
        api_response = api_instance.search_result()
        print("The response of EnterpriseApi->search_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->search_result: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**SearchResult**](SearchResult.md)

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
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_report**
> SuccessResponseBody send_report(report_email_dto)

Send a report.

Generate and send a report. This API waits for the report to be generated before returning. We recommend that you set the client’s timeout to at least 60 seconds. Available to org admins only and with a valid license.  Only available in Grafana Enterprise v7.0+. This API endpoint is experimental and may be deprecated in a future release. On deprecation, a migration strategy will be provided and the endpoint will remain functional until the next major release of Grafana.  You need to have a permission with action `reports:send`.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.report_email_dto import ReportEmailDTO
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    report_email_dto = bgrafana_api.ReportEmailDTO() # ReportEmailDTO | 

    try:
        # Send a report.
        api_response = api_instance.send_report(report_email_dto)
        print("The response of EnterpriseApi->send_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->send_report: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_email_dto** | [**ReportEmailDTO**](ReportEmailDTO.md)|  | 

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

# **send_test_email**
> SuccessResponseBody send_test_email(create_or_update_config_cmd)

Send test report via email.

Available to org admins only and with a valid license.  You need to have a permission with action `reports:send`.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.create_or_update_config_cmd import CreateOrUpdateConfigCmd
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    create_or_update_config_cmd = bgrafana_api.CreateOrUpdateConfigCmd() # CreateOrUpdateConfigCmd | 

    try:
        # Send test report via email.
        api_response = api_instance.send_test_email(create_or_update_config_cmd)
        print("The response of EnterpriseApi->send_test_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->send_test_email: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_or_update_config_cmd** | [**CreateOrUpdateConfigCmd**](CreateOrUpdateConfigCmd.md)|  | 

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

# **set_role_assignments**
> RoleAssignmentsDTO set_role_assignments(role_uid, set_role_assignments_command)

Set role assignments.

Set role assignments for the role with the given UID.  You need to have a permission with action `teams.roles:add` and `teams.roles:remove` and scope `permissions:type:delegate`, and `users.roles:add` and `users.roles:remove` and scope `permissions:type:delegate`.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.role_assignments_dto import RoleAssignmentsDTO
from bgrafana_api.models.set_role_assignments_command import SetRoleAssignmentsCommand
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    role_uid = 'role_uid_example' # str | 
    set_role_assignments_command = bgrafana_api.SetRoleAssignmentsCommand() # SetRoleAssignmentsCommand | 

    try:
        # Set role assignments.
        api_response = api_instance.set_role_assignments(role_uid, set_role_assignments_command)
        print("The response of EnterpriseApi->set_role_assignments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->set_role_assignments: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_uid** | **str**|  | 
 **set_role_assignments_command** | [**SetRoleAssignmentsCommand**](SetRoleAssignmentsCommand.md)|  | 

### Return type

[**RoleAssignmentsDTO**](RoleAssignmentsDTO.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_team_roles**
> SuccessResponseBody set_team_roles(team_id)

Update team role.

You need to have a permission with action `teams.roles:add` and `teams.roles:remove` and scope `permissions:type:delegate` for each.

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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    team_id = 56 # int | 

    try:
        # Update team role.
        api_response = api_instance.set_team_roles(team_id)
        print("The response of EnterpriseApi->set_team_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->set_team_roles: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_user_roles**
> SuccessResponseBody set_user_roles(user_id, set_user_roles_command)

Set user role assignments.

Update the user’s role assignments to match the provided set of UIDs. This will remove any assigned roles that aren’t in the request and add roles that are in the set but are not already assigned to the user. If you want to add or remove a single role, consider using Add a user role assignment or Remove a user role assignment instead.  You need to have a permission with action `users.roles:add` and `users.roles:remove` and scope `permissions:type:delegate` for each. `permissions:type:delegate`  scope ensures that users can only assign or unassign roles which have same, or a subset of permissions which the user has. For example, if a user does not have required permissions for creating users, they won’t be able to assign or unassign a role which will allow to do that. This is done to prevent escalation of privileges.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.set_user_roles_command import SetUserRolesCommand
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    user_id = 56 # int | 
    set_user_roles_command = bgrafana_api.SetUserRolesCommand() # SetUserRolesCommand | 

    try:
        # Set user role assignments.
        api_response = api_instance.set_user_roles(user_id, set_user_roles_command)
        print("The response of EnterpriseApi->set_user_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->set_user_roles: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **set_user_roles_command** | [**SetUserRolesCommand**](SetUserRolesCommand.md)|  | 

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
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_create_recording_rule**
> SuccessResponseBody test_create_recording_rule(recording_rule_json)

Test a recording rule.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.recording_rule_json import RecordingRuleJSON
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    recording_rule_json = bgrafana_api.RecordingRuleJSON() # RecordingRuleJSON | 

    try:
        # Test a recording rule.
        api_response = api_instance.test_create_recording_rule(recording_rule_json)
        print("The response of EnterpriseApi->test_create_recording_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->test_create_recording_rule: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_rule_json** | [**RecordingRuleJSON**](RecordingRuleJSON.md)|  | 

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
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**422** | UnprocessableEntityError |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_recording_rule**
> RecordingRuleJSON update_recording_rule(recording_rule_json)

Update the active status of a rule.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.recording_rule_json import RecordingRuleJSON
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    recording_rule_json = bgrafana_api.RecordingRuleJSON() # RecordingRuleJSON | 

    try:
        # Update the active status of a rule.
        api_response = api_instance.update_recording_rule(recording_rule_json)
        print("The response of EnterpriseApi->update_recording_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->update_recording_rule: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_rule_json** | [**RecordingRuleJSON**](RecordingRuleJSON.md)|  | 

### Return type

[**RecordingRuleJSON**](RecordingRuleJSON.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
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

# **update_report**
> SuccessResponseBody update_report(id, create_or_update_config_cmd)

Update a report.

Available to org admins only and with a valid or expired license.  You need to have a permission with action `reports.admin:write` with scope `reports:id:<report ID>`.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.create_or_update_config_cmd import CreateOrUpdateConfigCmd
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    id = 56 # int | 
    create_or_update_config_cmd = bgrafana_api.CreateOrUpdateConfigCmd() # CreateOrUpdateConfigCmd | 

    try:
        # Update a report.
        api_response = api_instance.update_report(id, create_or_update_config_cmd)
        print("The response of EnterpriseApi->update_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->update_report: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **create_or_update_config_cmd** | [**CreateOrUpdateConfigCmd**](CreateOrUpdateConfigCmd.md)|  | 

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

# **update_role**
> RoleDTO update_role(role_uid, update_role_command)

Update a custom role.

You need to have a permission with action `roles:write` and scope `permissions:type:delegate`. `permissions:type:delegate` scope ensures that users can only create custom roles with the same, or a subset of permissions which the user has.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import bgrafana_api
from bgrafana_api.models.role_dto import RoleDTO
from bgrafana_api.models.update_role_command import UpdateRoleCommand
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
    api_instance = bgrafana_api.EnterpriseApi(api_client)
    role_uid = 'role_uid_example' # str | 
    update_role_command = bgrafana_api.UpdateRoleCommand() # UpdateRoleCommand | 

    try:
        # Update a custom role.
        api_response = api_instance.update_role(role_uid, update_role_command)
        print("The response of EnterpriseApi->update_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->update_role: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_uid** | **str**|  | 
 **update_role_command** | [**UpdateRoleCommand**](UpdateRoleCommand.md)|  | 

### Return type

[**RoleDTO**](RoleDTO.md)

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
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

