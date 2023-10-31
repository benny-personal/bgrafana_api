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


from typing import Dict, List
from pydantic import BaseModel, Field, StrictStr, conlist
from bgrafana_api.models.gettable_alert import GettableAlert
from bgrafana_api.models.receiver import Receiver

class AlertGroup(BaseModel):
    """
    AlertGroup
    """
    alerts: conlist(GettableAlert) = Field(..., description="alerts")
    labels: Dict[str, StrictStr] = Field(..., description="LabelSet label set")
    receiver: Receiver = Field(...)
    __properties = ["alerts", "labels", "receiver"]

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
    def from_json(cls, json_str: str) -> AlertGroup:
        """Create an instance of AlertGroup from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in alerts (list)
        _items = []
        if self.alerts:
            for _item in self.alerts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['alerts'] = _items
        # override the default output from pydantic by calling `to_dict()` of receiver
        if self.receiver:
            _dict['receiver'] = self.receiver.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AlertGroup:
        """Create an instance of AlertGroup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AlertGroup.parse_obj(obj)

        _obj = AlertGroup.parse_obj({
            "alerts": [GettableAlert.from_dict(_item) for _item in obj.get("alerts")] if obj.get("alerts") is not None else None,
            "labels": obj.get("labels"),
            "receiver": Receiver.from_dict(obj.get("receiver")) if obj.get("receiver") is not None else None
        })
        return _obj

