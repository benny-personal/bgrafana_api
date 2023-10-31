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
from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist, validator
from bgrafana_api.models.alert_query import AlertQuery

class GettableGrafanaRule(BaseModel):
    """
    GettableGrafanaRule
    """
    condition: Optional[StrictStr] = None
    data: Optional[conlist(AlertQuery)] = None
    exec_err_state: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    interval_seconds: Optional[StrictInt] = Field(None, alias="intervalSeconds")
    is_paused: Optional[StrictBool] = None
    namespace_id: Optional[StrictInt] = None
    namespace_uid: Optional[StrictStr] = None
    no_data_state: Optional[StrictStr] = None
    org_id: Optional[StrictInt] = Field(None, alias="orgId")
    provenance: Optional[StrictStr] = None
    rule_group: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
    uid: Optional[StrictStr] = None
    updated: Optional[datetime] = None
    version: Optional[StrictInt] = None
    __properties = ["condition", "data", "exec_err_state", "id", "intervalSeconds", "is_paused", "namespace_id", "namespace_uid", "no_data_state", "orgId", "provenance", "rule_group", "title", "uid", "updated", "version"]

    @validator('exec_err_state')
    def exec_err_state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('OK', 'Alerting', 'Error'):
            raise ValueError("must be one of enum values ('OK', 'Alerting', 'Error')")
        return value

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
    def from_json(cls, json_str: str) -> GettableGrafanaRule:
        """Create an instance of GettableGrafanaRule from a JSON string"""
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
    def from_dict(cls, obj: dict) -> GettableGrafanaRule:
        """Create an instance of GettableGrafanaRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GettableGrafanaRule.parse_obj(obj)

        _obj = GettableGrafanaRule.parse_obj({
            "condition": obj.get("condition"),
            "data": [AlertQuery.from_dict(_item) for _item in obj.get("data")] if obj.get("data") is not None else None,
            "exec_err_state": obj.get("exec_err_state"),
            "id": obj.get("id"),
            "interval_seconds": obj.get("intervalSeconds"),
            "is_paused": obj.get("is_paused"),
            "namespace_id": obj.get("namespace_id"),
            "namespace_uid": obj.get("namespace_uid"),
            "no_data_state": obj.get("no_data_state"),
            "org_id": obj.get("orgId"),
            "provenance": obj.get("provenance"),
            "rule_group": obj.get("rule_group"),
            "title": obj.get("title"),
            "uid": obj.get("uid"),
            "updated": obj.get("updated"),
            "version": obj.get("version")
        })
        return _obj

