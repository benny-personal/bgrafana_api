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

from datetime import datetime
from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist, validator
from bgrafana_api.models.alert_query import AlertQuery

class BacktestConfig(BaseModel):
    """
    BacktestConfig
    """
    annotations: Optional[Dict[str, StrictStr]] = None
    condition: Optional[StrictStr] = None
    data: Optional[conlist(AlertQuery)] = None
    var_for: Optional[StrictInt] = Field(None, alias="for")
    var_from: Optional[datetime] = Field(None, alias="from")
    interval: Optional[StrictInt] = None
    labels: Optional[Dict[str, StrictStr]] = None
    no_data_state: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
    to: Optional[datetime] = None
    __properties = ["annotations", "condition", "data", "for", "from", "interval", "labels", "no_data_state", "title", "to"]

    @validator('no_data_state')
    def no_data_state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Alerting', 'NoData', 'OK'):
            raise ValueError("must be one of enum values ('Alerting', 'NoData', 'OK')")
        return value

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
    def from_json(cls, json_str: str) -> BacktestConfig:
        """Create an instance of BacktestConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item in self.data:
                if _item:
                    _items.append(_item.to_dict())
            _dict['data'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BacktestConfig:
        """Create an instance of BacktestConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BacktestConfig.parse_obj(obj)

        _obj = BacktestConfig.parse_obj({
            "annotations": obj.get("annotations"),
            "condition": obj.get("condition"),
            "data": [AlertQuery.from_dict(_item) for _item in obj.get("data")] if obj.get("data") is not None else None,
            "var_for": obj.get("for"),
            "var_from": obj.get("from"),
            "interval": obj.get("interval"),
            "labels": obj.get("labels"),
            "no_data_state": obj.get("no_data_state"),
            "title": obj.get("title"),
            "to": obj.get("to")
        })
        return _obj


