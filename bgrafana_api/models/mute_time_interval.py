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
from pydantic import BaseModel, StrictStr, conlist
from bgrafana_api.models.time_interval import TimeInterval

class MuteTimeInterval(BaseModel):
    """
    MuteTimeInterval
    """
    name: Optional[StrictStr] = None
    time_intervals: Optional[conlist(TimeInterval)] = None
    __properties = ["name", "time_intervals"]

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
    def from_json(cls, json_str: str) -> MuteTimeInterval:
        """Create an instance of MuteTimeInterval from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in time_intervals (list)
        _items = []
        if self.time_intervals:
            for _item in self.time_intervals:
                if _item:
                    _items.append(_item.to_dict())
            _dict['time_intervals'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MuteTimeInterval:
        """Create an instance of MuteTimeInterval from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MuteTimeInterval.parse_obj(obj)

        _obj = MuteTimeInterval.parse_obj({
            "name": obj.get("name"),
            "time_intervals": [TimeInterval.from_dict(_item) for _item in obj.get("time_intervals")] if obj.get("time_intervals") is not None else None
        })
        return _obj


