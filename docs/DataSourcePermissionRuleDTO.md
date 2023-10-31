# DataSourcePermissionRuleDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**built_in_role** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**datasource_id** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**is_managed** | **bool** |  | [optional] 
**permission** | **int** | Datasource permission Description: &#x60;0&#x60; - No Access &#x60;1&#x60; - Query &#x60;2&#x60; - Edit Enum: 0,1,2 | [optional] 
**permission_name** | **str** |  | [optional] 
**team** | **str** |  | [optional] 
**team_avatar_url** | **str** |  | [optional] 
**team_email** | **str** |  | [optional] 
**team_id** | **int** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**user_avatar_url** | **str** |  | [optional] 
**user_email** | **str** |  | [optional] 
**user_id** | **int** |  | [optional] 
**user_login** | **str** |  | [optional] 

## Example

```python
from bgrafana_api.models.data_source_permission_rule_dto import DataSourcePermissionRuleDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DataSourcePermissionRuleDTO from a JSON string
data_source_permission_rule_dto_instance = DataSourcePermissionRuleDTO.from_json(json)
# print the JSON string representation of the object
print DataSourcePermissionRuleDTO.to_json()

# convert the object into a dict
data_source_permission_rule_dto_dict = data_source_permission_rule_dto_instance.to_dict()
# create an instance of DataSourcePermissionRuleDTO from a dict
data_source_permission_rule_dto_form_dict = data_source_permission_rule_dto.from_dict(data_source_permission_rule_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


