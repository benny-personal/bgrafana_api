# AlertRuleGroupExport


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder** | **str** |  | [optional] 
**interval** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**org_id** | **int** |  | [optional] 
**rules** | [**List[AlertRuleExport]**](AlertRuleExport.md) |  | [optional] 

## Example

```python
from bgrafana_api.models.alert_rule_group_export import AlertRuleGroupExport

# TODO update the JSON string below
json = "{}"
# create an instance of AlertRuleGroupExport from a JSON string
alert_rule_group_export_instance = AlertRuleGroupExport.from_json(json)
# print the JSON string representation of the object
print AlertRuleGroupExport.to_json()

# convert the object into a dict
alert_rule_group_export_dict = alert_rule_group_export_instance.to_dict()
# create an instance of AlertRuleGroupExport from a dict
alert_rule_group_export_form_dict = alert_rule_group_export.from_dict(alert_rule_group_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


