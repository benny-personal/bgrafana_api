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

class ServiceAccountDTO(BaseModel):
    """
    swagger: model  # noqa: E501
    """
    access_control: Optional[Dict[str, StrictBool]] = Field(None, alias="accessControl")
    avatar_url: Optional[StrictStr] = Field(None, alias="avatarUrl")
    id: Optional[StrictInt] = None
    is_disabled: Optional[StrictBool] = Field(None, alias="isDisabled")
    login: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    org_id: Optional[StrictInt] = Field(None, alias="orgId")
    role: Optional[StrictStr] = None
    tokens: Optional[StrictInt] = None
    __properties = ["accessControl", "avatarUrl", "id", "isDisabled", "login", "name", "orgId", "role", "tokens"]

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
    def from_json(cls, json_str: str) -> ServiceAccountDTO:
        """Create an instance of ServiceAccountDTO from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ServiceAccountDTO:
        """Create an instance of ServiceAccountDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ServiceAccountDTO.parse_obj(obj)

        _obj = ServiceAccountDTO.parse_obj({
            "access_control": obj.get("accessControl"),
            "avatar_url": obj.get("avatarUrl"),
            "id": obj.get("id"),
            "is_disabled": obj.get("isDisabled"),
            "login": obj.get("login"),
            "name": obj.get("name"),
            "org_id": obj.get("orgId"),
            "role": obj.get("role"),
            "tokens": obj.get("tokens")
        })
        return _obj

