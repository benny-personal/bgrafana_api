# RelativeTimeRange

RelativeTimeRange is the per query start and end time for requests.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **int** |  | [optional] 
**to** | **int** |  | [optional] 

## Example

```python
from bgrafana_api.models.relative_time_range import RelativeTimeRange

# TODO update the JSON string below
json = "{}"
# create an instance of RelativeTimeRange from a JSON string
relative_time_range_instance = RelativeTimeRange.from_json(json)
# print the JSON string representation of the object
print RelativeTimeRange.to_json()

# convert the object into a dict
relative_time_range_dict = relative_time_range_instance.to_dict()
# create an instance of RelativeTimeRange from a dict
relative_time_range_form_dict = relative_time_range.from_dict(relative_time_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


