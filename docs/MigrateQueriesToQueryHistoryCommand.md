# MigrateQueriesToQueryHistoryCommand

MigrateQueriesToQueryHistoryCommand is the command used for migration of old queries into query history

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queries** | [**List[QueryToMigrate]**](QueryToMigrate.md) | Array of queries to store in query history. | [optional] 

## Example

```python
from bgrafana_api.models.migrate_queries_to_query_history_command import MigrateQueriesToQueryHistoryCommand

# TODO update the JSON string below
json = "{}"
# create an instance of MigrateQueriesToQueryHistoryCommand from a JSON string
migrate_queries_to_query_history_command_instance = MigrateQueriesToQueryHistoryCommand.from_json(json)
# print the JSON string representation of the object
print MigrateQueriesToQueryHistoryCommand.to_json()

# convert the object into a dict
migrate_queries_to_query_history_command_dict = migrate_queries_to_query_history_command_instance.to_dict()
# create an instance of MigrateQueriesToQueryHistoryCommand from a dict
migrate_queries_to_query_history_command_form_dict = migrate_queries_to_query_history_command.from_dict(migrate_queries_to_query_history_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


