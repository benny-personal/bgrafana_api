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


from typing import Optional
from pydantic import BaseModel, StrictStr

class PrometheusRemoteWriteTargetJSON(BaseModel):
    """
    PrometheusRemoteWriteTargetJSON
    """
    data_source_uid: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    remote_write_path: Optional[StrictStr] = None
    __properties = ["data_source_uid", "id", "remote_write_path"]

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
    def from_json(cls, json_str: str) -> PrometheusRemoteWriteTargetJSON:
        """Create an instance of PrometheusRemoteWriteTargetJSON from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PrometheusRemoteWriteTargetJSON:
        """Create an instance of PrometheusRemoteWriteTargetJSON from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PrometheusRemoteWriteTargetJSON.parse_obj(obj)

        _obj = PrometheusRemoteWriteTargetJSON.parse_obj({
            "data_source_uid": obj.get("data_source_uid"),
            "id": obj.get("id"),
            "remote_write_path": obj.get("remote_write_path")
        })
        return _obj


