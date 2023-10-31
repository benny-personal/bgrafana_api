# AddPermissionDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**builtin_role** | **str** |  | [optional] 
**permission** | **int** | Datasource permission Description: &#x60;0&#x60; - No Access &#x60;1&#x60; - Query &#x60;2&#x60; - Edit Enum: 0,1,2 | [optional] 
**team_id** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 

## Example

```python
from bgrafana_api.models.add_permission_dto import AddPermissionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AddPermissionDTO from a JSON string
add_permission_dto_instance = AddPermissionDTO.from_json(json)
# print the JSON string representation of the object
print AddPermissionDTO.to_json()

# convert the object into a dict
add_permission_dto_dict = add_permission_dto_instance.to_dict()
# create an instance of AddPermissionDTO from a dict
add_permission_dto_form_dict = add_permission_dto.from_dict(add_permission_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


