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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist

class TeamMemberDTO(BaseModel):
    """
    TeamMemberDTO
    """
    auth_module: Optional[StrictStr] = None
    avatar_url: Optional[StrictStr] = Field(None, alias="avatarUrl")
    email: Optional[StrictStr] = None
    labels: Optional[conlist(StrictStr)] = None
    login: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    org_id: Optional[StrictInt] = Field(None, alias="orgId")
    permission: Optional[StrictInt] = None
    team_id: Optional[StrictInt] = Field(None, alias="teamId")
    user_id: Optional[StrictInt] = Field(None, alias="userId")
    __properties = ["auth_module", "avatarUrl", "email", "labels", "login", "name", "orgId", "permission", "teamId", "userId"]

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
    def from_json(cls, json_str: str) -> TeamMemberDTO:
        """Create an instance of TeamMemberDTO from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TeamMemberDTO:
        """Create an instance of TeamMemberDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TeamMemberDTO.parse_obj(obj)

        _obj = TeamMemberDTO.parse_obj({
            "auth_module": obj.get("auth_module"),
            "avatar_url": obj.get("avatarUrl"),
            "email": obj.get("email"),
            "labels": obj.get("labels"),
            "login": obj.get("login"),
            "name": obj.get("name"),
            "org_id": obj.get("orgId"),
            "permission": obj.get("permission"),
            "team_id": obj.get("teamId"),
            "user_id": obj.get("userId")
        })
        return _obj

