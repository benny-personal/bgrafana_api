# DataSourcePermissionsDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datasource_id** | **int** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**permissions** | [**List[DataSourcePermissionRuleDTO]**](DataSourcePermissionRuleDTO.md) |  | [optional] 

## Example

```python
from bgrafana_api.models.data_source_permissions_dto import DataSourcePermissionsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DataSourcePermissionsDTO from a JSON string
data_source_permissions_dto_instance = DataSourcePermissionsDTO.from_json(json)
# print the JSON string representation of the object
print DataSourcePermissionsDTO.to_json()

# convert the object into a dict
data_source_permissions_dto_dict = data_source_permissions_dto_instance.to_dict()
# create an instance of DataSourcePermissionsDTO from a dict
data_source_permissions_dto_form_dict = data_source_permissions_dto.from_dict(data_source_permissions_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


