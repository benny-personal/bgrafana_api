# Item


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title is an unused property -- it will be removed in the future | [optional] 
**type** | **str** |  | [optional] 
**value** | **str** | Value depends on type and describes the playlist item.  dashboard_by_id: The value is an internal numerical identifier set by Grafana. This is not portable as the numerical identifier is non-deterministic between different instances. Will be replaced by dashboard_by_uid in the future. (deprecated) dashboard_by_tag: The value is a tag which is set on any number of dashboards. All dashboards behind the tag will be added to the playlist. dashboard_by_uid: The value is the dashboard UID | [optional] 

## Example

```python
from bgrafana_api.models.item import Item

# TODO update the JSON string below
json = "{}"
# create an instance of Item from a JSON string
item_instance = Item.from_json(json)
# print the JSON string representation of the object
print Item.to_json()

# convert the object into a dict
item_dict = item_instance.to_dict()
# create an instance of Item from a dict
item_form_dict = item.from_dict(item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


