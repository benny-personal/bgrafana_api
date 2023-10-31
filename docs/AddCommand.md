# AddCommand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**seconds_to_live** | **int** |  | [optional] 

## Example

```python
from bgrafana_api.models.add_command import AddCommand

# TODO update the JSON string below
json = "{}"
# create an instance of AddCommand from a JSON string
add_command_instance = AddCommand.from_json(json)
# print the JSON string representation of the object
print AddCommand.to_json()

# convert the object into a dict
add_command_dict = add_command_instance.to_dict()
# create an instance of AddCommand from a dict
add_command_form_dict = add_command.from_dict(add_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


