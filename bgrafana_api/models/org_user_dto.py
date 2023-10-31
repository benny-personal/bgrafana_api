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

from datetime import datetime
from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist

class OrgUserDTO(BaseModel):
    """
    OrgUserDTO
    """
    access_control: Optional[Dict[str, StrictBool]] = Field(None, alias="accessControl")
    auth_labels: Optional[conlist(StrictStr)] = Field(None, alias="authLabels")
    avatar_url: Optional[StrictStr] = Field(None, alias="avatarUrl")
    email: Optional[StrictStr] = None
    is_disabled: Optional[StrictBool] = Field(None, alias="isDisabled")
    is_externally_synced: Optional[StrictBool] = Field(None, alias="isExternallySynced")
    last_seen_at: Optional[datetime] = Field(None, alias="lastSeenAt")
    last_seen_at_age: Optional[StrictStr] = Field(None, alias="lastSeenAtAge")
    login: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    org_id: Optional[StrictInt] = Field(None, alias="orgId")
    role: Optional[StrictStr] = None
    user_id: Optional[StrictInt] = Field(None, alias="userId")
    __properties = ["accessControl", "authLabels", "avatarUrl", "email", "isDisabled", "isExternallySynced", "lastSeenAt", "lastSeenAtAge", "login", "name", "orgId", "role", "userId"]

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
    def from_json(cls, json_str: str) -> OrgUserDTO:
        """Create an instance of OrgUserDTO from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrgUserDTO:
        """Create an instance of OrgUserDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OrgUserDTO.parse_obj(obj)

        _obj = OrgUserDTO.parse_obj({
            "access_control": obj.get("accessControl"),
            "auth_labels": obj.get("authLabels"),
            "avatar_url": obj.get("avatarUrl"),
            "email": obj.get("email"),
            "is_disabled": obj.get("isDisabled"),
            "is_externally_synced": obj.get("isExternallySynced"),
            "last_seen_at": obj.get("lastSeenAt"),
            "last_seen_at_age": obj.get("lastSeenAtAge"),
            "login": obj.get("login"),
            "name": obj.get("name"),
            "org_id": obj.get("orgId"),
            "role": obj.get("role"),
            "user_id": obj.get("userId")
        })
        return _obj

