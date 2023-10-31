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
from pydantic import BaseModel
from bgrafana_api.models.annotation_actions import AnnotationActions

class AnnotationPermission(BaseModel):
    """
    AnnotationPermission
    """
    dashboard: Optional[AnnotationActions] = None
    organization: Optional[AnnotationActions] = None
    __properties = ["dashboard", "organization"]

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
    def from_json(cls, json_str: str) -> AnnotationPermission:
        """Create an instance of AnnotationPermission from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of dashboard
        if self.dashboard:
            _dict['dashboard'] = self.dashboard.to_dict()
        # override the default output from pydantic by calling `to_dict()` of organization
        if self.organization:
            _dict['organization'] = self.organization.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AnnotationPermission:
        """Create an instance of AnnotationPermission from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AnnotationPermission.parse_obj(obj)

        _obj = AnnotationPermission.parse_obj({
            "dashboard": AnnotationActions.from_dict(obj.get("dashboard")) if obj.get("dashboard") is not None else None,
            "organization": AnnotationActions.from_dict(obj.get("organization")) if obj.get("organization") is not None else None
        })
        return _obj


