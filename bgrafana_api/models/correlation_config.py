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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from bgrafana_api.models.transformation import Transformation

class CorrelationConfig(BaseModel):
    """
    CorrelationConfig
    """
    field: StrictStr = Field(..., description="Field used to attach the correlation link")
    target: Dict[str, Any] = Field(..., description="Target data query")
    transformations: Optional[conlist(Transformation)] = None
    type: StrictStr = Field(...)
    __properties = ["field", "target", "transformations", "type"]

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
    def from_json(cls, json_str: str) -> CorrelationConfig:
        """Create an instance of CorrelationConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in transformations (list)
        _items = []
        if self.transformations:
            for _item in self.transformations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['transformations'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CorrelationConfig:
        """Create an instance of CorrelationConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CorrelationConfig.parse_obj(obj)

        _obj = CorrelationConfig.parse_obj({
            "field": obj.get("field"),
            "target": obj.get("target"),
            "transformations": [Transformation.from_dict(_item) for _item in obj.get("transformations")] if obj.get("transformations") is not None else None,
            "type": obj.get("type")
        })
        return _obj


