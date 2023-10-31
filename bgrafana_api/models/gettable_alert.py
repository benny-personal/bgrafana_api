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
from pydantic import BaseModel, Field, StrictStr, conlist
from bgrafana_api.models.alert_status import AlertStatus
from bgrafana_api.models.receiver import Receiver

class GettableAlert(BaseModel):
    """
    GettableAlert
    """
    annotations: Dict[str, StrictStr] = Field(..., description="LabelSet label set")
    ends_at: datetime = Field(..., alias="endsAt", description="ends at")
    fingerprint: StrictStr = Field(..., description="fingerprint")
    generator_url: Optional[StrictStr] = Field(None, alias="generatorURL", description="generator URL Format: uri")
    labels: Dict[str, StrictStr] = Field(..., description="LabelSet label set")
    receivers: conlist(Receiver) = Field(..., description="receivers")
    starts_at: datetime = Field(..., alias="startsAt", description="starts at")
    status: AlertStatus = Field(...)
    updated_at: datetime = Field(..., alias="updatedAt", description="updated at")
    __properties = ["annotations", "endsAt", "fingerprint", "generatorURL", "labels", "receivers", "startsAt", "status", "updatedAt"]

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
    def from_json(cls, json_str: str) -> GettableAlert:
        """Create an instance of GettableAlert from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in receivers (list)
        _items = []
        if self.receivers:
            for _item in self.receivers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['receivers'] = _items
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GettableAlert:
        """Create an instance of GettableAlert from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GettableAlert.parse_obj(obj)

        _obj = GettableAlert.parse_obj({
            "annotations": obj.get("annotations"),
            "ends_at": obj.get("endsAt"),
            "fingerprint": obj.get("fingerprint"),
            "generator_url": obj.get("generatorURL"),
            "labels": obj.get("labels"),
            "receivers": [Receiver.from_dict(_item) for _item in obj.get("receivers")] if obj.get("receivers") is not None else None,
            "starts_at": obj.get("startsAt"),
            "status": AlertStatus.from_dict(obj.get("status")) if obj.get("status") is not None else None,
            "updated_at": obj.get("updatedAt")
        })
        return _obj

