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
from pydantic import BaseModel, Field, StrictStr, validator

class Transformation(BaseModel):
    """
    Transformation
    """
    expression: Optional[StrictStr] = None
    field: Optional[StrictStr] = None
    map_value: Optional[StrictStr] = Field(None, alias="mapValue")
    type: Optional[StrictStr] = None
    __properties = ["expression", "field", "mapValue", "type"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('regex', 'logfmt'):
            raise ValueError("must be one of enum values ('regex', 'logfmt')")
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
    def from_json(cls, json_str: str) -> Transformation:
        """Create an instance of Transformation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Transformation:
        """Create an instance of Transformation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Transformation.parse_obj(obj)

        _obj = Transformation.parse_obj({
            "expression": obj.get("expression"),
            "field": obj.get("field"),
            "map_value": obj.get("mapValue"),
            "type": obj.get("type")
        })
        return _obj

