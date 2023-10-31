# TrimDashboardFullWithMeta


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard** | **object** |  | [optional] 
**meta** | **object** |  | [optional] 

## Example

```python
from bgrafana_api.models.trim_dashboard_full_with_meta import TrimDashboardFullWithMeta

# TODO update the JSON string below
json = "{}"
# create an instance of TrimDashboardFullWithMeta from a JSON string
trim_dashboard_full_with_meta_instance = TrimDashboardFullWithMeta.from_json(json)
# print the JSON string representation of the object
print TrimDashboardFullWithMeta.to_json()

# convert the object into a dict
trim_dashboard_full_with_meta_dict = trim_dashboard_full_with_meta_instance.to_dict()
# create an instance of TrimDashboardFullWithMeta from a dict
trim_dashboard_full_with_meta_form_dict = trim_dashboard_full_with_meta.from_dict(trim_dashboard_full_with_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


