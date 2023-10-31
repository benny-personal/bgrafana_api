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
from pydantic import BaseModel, StrictInt, StrictStr

class NewApiKeyResult(BaseModel):
    """
    NewApiKeyResult
    """
    id: Optional[StrictInt] = None
    key: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    __properties = ["id", "key", "name"]

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
    def from_json(cls, json_str: str) -> NewApiKeyResult:
        """Create an instance of NewApiKeyResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NewApiKeyResult:
        """Create an instance of NewApiKeyResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NewApiKeyResult.parse_obj(obj)

        _obj = NewApiKeyResult.parse_obj({
            "id": obj.get("id"),
            "key": obj.get("key"),
            "name": obj.get("name")
        })
        return _obj

