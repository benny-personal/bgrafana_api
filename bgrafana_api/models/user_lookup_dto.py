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
from pydantic import BaseModel, Field, StrictInt, StrictStr

class UserLookupDTO(BaseModel):
    """
    UserLookupDTO
    """
    avatar_url: Optional[StrictStr] = Field(None, alias="avatarUrl")
    login: Optional[StrictStr] = None
    user_id: Optional[StrictInt] = Field(None, alias="userId")
    __properties = ["avatarUrl", "login", "userId"]

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
    def from_json(cls, json_str: str) -> UserLookupDTO:
        """Create an instance of UserLookupDTO from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UserLookupDTO:
        """Create an instance of UserLookupDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UserLookupDTO.parse_obj(obj)

        _obj = UserLookupDTO.parse_obj({
            "avatar_url": obj.get("avatarUrl"),
            "login": obj.get("login"),
            "user_id": obj.get("userId")
        })
        return _obj


