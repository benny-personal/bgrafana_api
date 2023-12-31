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
from bgrafana_api.models.calculate_diff_target import CalculateDiffTarget

class CalculateDashboardDiffRequest(BaseModel):
    """
    CalculateDashboardDiffRequest
    """
    base: Optional[CalculateDiffTarget] = None
    diff_type: Optional[StrictStr] = Field(None, alias="diffType", description="The type of diff to return Description: `basic` `json`")
    new: Optional[CalculateDiffTarget] = None
    __properties = ["base", "diffType", "new"]

    @validator('diff_type')
    def diff_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('basic', 'json'):
            raise ValueError("must be one of enum values ('basic', 'json')")
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
    def from_json(cls, json_str: str) -> CalculateDashboardDiffRequest:
        """Create an instance of CalculateDashboardDiffRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of base
        if self.base:
            _dict['base'] = self.base.to_dict()
        # override the default output from pydantic by calling `to_dict()` of new
        if self.new:
            _dict['new'] = self.new.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CalculateDashboardDiffRequest:
        """Create an instance of CalculateDashboardDiffRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CalculateDashboardDiffRequest.parse_obj(obj)

        _obj = CalculateDashboardDiffRequest.parse_obj({
            "base": CalculateDiffTarget.from_dict(obj.get("base")) if obj.get("base") is not None else None,
            "diff_type": obj.get("diffType"),
            "new": CalculateDiffTarget.from_dict(obj.get("new")) if obj.get("new") is not None else None
        })
        return _obj


