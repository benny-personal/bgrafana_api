# QueryToMigrate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 
**datasource_uid** | **str** |  | [optional] 
**queries** | **object** |  | [optional] 
**starred** | **bool** |  | [optional] 

## Example

```python
from bgrafana_api.models.query_to_migrate import QueryToMigrate

# TODO update the JSON string below
json = "{}"
# create an instance of QueryToMigrate from a JSON string
query_to_migrate_instance = QueryToMigrate.from_json(json)
# print the JSON string representation of the object
print QueryToMigrate.to_json()

# convert the object into a dict
query_to_migrate_dict = query_to_migrate_instance.to_dict()
# create an instance of QueryToMigrate from a dict
query_to_migrate_form_dict = query_to_migrate.from_dict(query_to_migrate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


