# Field2

A Field is essentially a slice of various types with extra properties and methods. See NewField() for supported types.  The slice data in the Field is a not exported, so methods on the Field are used to to manipulate its data.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**FieldConfig**](FieldConfig.md) |  | [optional] 
**labels** | **Dict[str, str]** | Labels are used to add metadata to an object.  The JSON will always be sorted keys | [optional] 
**name** | **str** | Name is default identifier of the field. The name does not have to be unique, but the combination of name and Labels should be unique for proper behavior in all situations. | [optional] 

## Example

```python
from bgrafana_api.models.field2 import Field2

# TODO update the JSON string below
json = "{}"
# create an instance of Field2 from a JSON string
field2_instance = Field2.from_json(json)
# print the JSON string representation of the object
print Field2.to_json()

# convert the object into a dict
field2_dict = field2_instance.to_dict()
# create an instance of Field2 from a dict
field2_form_dict = field2.from_dict(field2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


