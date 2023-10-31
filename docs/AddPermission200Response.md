# AddPermission200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**permission_id** | **int** |  | [optional] 

## Example

```python
from bgrafana_api.models.add_permission200_response import AddPermission200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AddPermission200Response from a JSON string
add_permission200_response_instance = AddPermission200Response.from_json(json)
# print the JSON string representation of the object
print AddPermission200Response.to_json()

# convert the object into a dict
add_permission200_response_dict = add_permission200_response_instance.to_dict()
# create an instance of AddPermission200Response from a dict
add_permission200_response_form_dict = add_permission200_response.from_dict(add_permission200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


