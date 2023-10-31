# SyncResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elapsed** | **int** |  | [optional] 
**failed_users** | [**List[FailedUser]**](FailedUser.md) |  | [optional] 
**missing_user_ids** | **List[int]** |  | [optional] 
**started** | **datetime** |  | [optional] 
**updated_user_ids** | **List[int]** |  | [optional] 

## Example

```python
from bgrafana_api.models.sync_result import SyncResult

# TODO update the JSON string below
json = "{}"
# create an instance of SyncResult from a JSON string
sync_result_instance = SyncResult.from_json(json)
# print the JSON string representation of the object
print SyncResult.to_json()

# convert the object into a dict
sync_result_dict = sync_result_instance.to_dict()
# create an instance of SyncResult from a dict
sync_result_form_dict = sync_result.from_dict(sync_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


