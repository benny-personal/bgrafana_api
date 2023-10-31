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


from typing import Dict, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr

class FolderSearchHit(BaseModel):
    """
    FolderSearchHit
    """
    access_control: Optional[Dict[str, StrictBool]] = Field(None, alias="accessControl", description="Metadata contains user accesses for a given resource Ex: map[string]bool{\"create\":true, \"delete\": true}")
    id: Optional[StrictInt] = None
    parent_uid: Optional[StrictStr] = Field(None, alias="parentUid")
    title: Optional[StrictStr] = None
    uid: Optional[StrictStr] = None
    __properties = ["accessControl", "id", "parentUid", "title", "uid"]

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
    def from_json(cls, json_str: str) -> FolderSearchHit:
        """Create an instance of FolderSearchHit from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FolderSearchHit:
        """Create an instance of FolderSearchHit from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FolderSearchHit.parse_obj(obj)

        _obj = FolderSearchHit.parse_obj({
            "access_control": obj.get("accessControl"),
            "id": obj.get("id"),
            "parent_uid": obj.get("parentUid"),
            "title": obj.get("title"),
            "uid": obj.get("uid")
        })
        return _obj


