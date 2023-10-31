# TrimDashboardCommand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard** | **object** |  | [optional] 
**meta** | **object** |  | [optional] 

## Example

```python
from bgrafana_api.models.trim_dashboard_command import TrimDashboardCommand

# TODO update the JSON string below
json = "{}"
# create an instance of TrimDashboardCommand from a JSON string
trim_dashboard_command_instance = TrimDashboardCommand.from_json(json)
# print the JSON string representation of the object
print TrimDashboardCommand.to_json()

# convert the object into a dict
trim_dashboard_command_dict = trim_dashboard_command_instance.to_dict()
# create an instance of TrimDashboardCommand from a dict
trim_dashboard_command_form_dict = trim_dashboard_command.from_dict(trim_dashboard_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


