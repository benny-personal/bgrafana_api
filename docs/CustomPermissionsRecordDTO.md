# CustomPermissionsRecordDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_permissions** | **str** |  | [optional] 
**grantee_name** | **str** |  | [optional] 
**grantee_type** | **str** |  | [optional] 
**grantee_url** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_folder** | **bool** |  | [optional] 
**org_id** | **int** |  | [optional] 
**org_role** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**users_count** | **int** |  | [optional] 

## Example

```python
from bgrafana_api.models.custom_permissions_record_dto import CustomPermissionsRecordDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CustomPermissionsRecordDTO from a JSON string
custom_permissions_record_dto_instance = CustomPermissionsRecordDTO.from_json(json)
# print the JSON string representation of the object
print CustomPermissionsRecordDTO.to_json()

# convert the object into a dict
custom_permissions_record_dto_dict = custom_permissions_record_dto_instance.to_dict()
# create an instance of CustomPermissionsRecordDTO from a dict
custom_permissions_record_dto_form_dict = custom_permissions_record_dto.from_dict(custom_permissions_record_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


