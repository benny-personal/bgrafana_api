# TimeRange

For example, 4:00PM to End of the day would Begin at 1020 and End at 1440.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_minute** | **int** |  | [optional] 
**start_minute** | **int** |  | [optional] 

## Example

```python
from bgrafana_api.models.time_range import TimeRange

# TODO update the JSON string below
json = "{}"
# create an instance of TimeRange from a JSON string
time_range_instance = TimeRange.from_json(json)
# print the JSON string representation of the object
print TimeRange.to_json()

# convert the object into a dict
time_range_dict = time_range_instance.to_dict()
# create an instance of TimeRange from a dict
time_range_form_dict = time_range.from_dict(time_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


