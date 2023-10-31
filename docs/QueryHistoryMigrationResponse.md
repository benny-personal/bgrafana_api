# QueryHistoryMigrationResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**starred_count** | **int** |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from bgrafana_api.models.query_history_migration_response import QueryHistoryMigrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueryHistoryMigrationResponse from a JSON string
query_history_migration_response_instance = QueryHistoryMigrationResponse.from_json(json)
# print the JSON string representation of the object
print QueryHistoryMigrationResponse.to_json()

# convert the object into a dict
query_history_migration_response_dict = query_history_migration_response_instance.to_dict()
# create an instance of QueryHistoryMigrationResponse from a dict
query_history_migration_response_form_dict = query_history_migration_response.from_dict(query_history_migration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


