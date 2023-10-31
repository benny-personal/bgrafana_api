# coding: utf-8

"""
    Grafana HTTP API.

    The Grafana backend exposes an HTTP API, the same API is used by the frontend to do everything from saving dashboards, creating users and updating data sources.

    The version of the OpenAPI document: 0.0.1
    Contact: hello@grafana.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from bgrafana_api.models.alert_rule_export import AlertRuleExport

class AlertRuleGroupExport(BaseModel):
    """
    AlertRuleGroupExport
    """
    folder: Optional[StrictStr] = None
    interval: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    org_id: Optional[StrictInt] = Field(None, alias="orgId")
    rules: Optional[conlist(AlertRuleExport)] = None
    __properties = ["folder", "interval", "name", "orgId", "rules"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> AlertRuleGroupExport:
        """Create an instance of AlertRuleGroupExport from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in rules (list)
        _items = []
        if self.rules:
            for _item in self.rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['rules'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AlertRuleGroupExport:
        """Create an instance of AlertRuleGroupExport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AlertRuleGroupExport.parse_obj(obj)

        _obj = AlertRuleGroupExport.parse_obj({
            "folder": obj.get("folder"),
            "interval": obj.get("interval"),
            "name": obj.get("name"),
            "org_id": obj.get("orgId"),
            "rules": [AlertRuleExport.from_dict(_item) for _item in obj.get("rules")] if obj.get("rules") is not None else None
        })
        return _obj

