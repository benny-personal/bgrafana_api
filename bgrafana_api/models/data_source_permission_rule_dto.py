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
from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr

class DataSourcePermissionRuleDTO(BaseModel):
    """
    DataSourcePermissionRuleDTO
    """
    built_in_role: Optional[StrictStr] = Field(None, alias="builtInRole")
    created: Optional[datetime] = None
    datasource_id: Optional[StrictInt] = Field(None, alias="datasourceId")
    id: Optional[StrictInt] = None
    is_managed: Optional[StrictBool] = Field(None, alias="isManaged")
    permission: Optional[StrictInt] = Field(None, description="Datasource permission Description: `0` - No Access `1` - Query `2` - Edit Enum: 0,1,2")
    permission_name: Optional[StrictStr] = Field(None, alias="permissionName")
    team: Optional[StrictStr] = None
    team_avatar_url: Optional[StrictStr] = Field(None, alias="teamAvatarUrl")
    team_email: Optional[StrictStr] = Field(None, alias="teamEmail")
    team_id: Optional[StrictInt] = Field(None, alias="teamId")
    updated: Optional[datetime] = None
    user_avatar_url: Optional[StrictStr] = Field(None, alias="userAvatarUrl")
    user_email: Optional[StrictStr] = Field(None, alias="userEmail")
    user_id: Optional[StrictInt] = Field(None, alias="userId")
    user_login: Optional[StrictStr] = Field(None, alias="userLogin")
    __properties = ["builtInRole", "created", "datasourceId", "id", "isManaged", "permission", "permissionName", "team", "teamAvatarUrl", "teamEmail", "teamId", "updated", "userAvatarUrl", "userEmail", "userId", "userLogin"]

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
    def from_json(cls, json_str: str) -> DataSourcePermissionRuleDTO:
        """Create an instance of DataSourcePermissionRuleDTO from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DataSourcePermissionRuleDTO:
        """Create an instance of DataSourcePermissionRuleDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DataSourcePermissionRuleDTO.parse_obj(obj)

        _obj = DataSourcePermissionRuleDTO.parse_obj({
            "built_in_role": obj.get("builtInRole"),
            "created": obj.get("created"),
            "datasource_id": obj.get("datasourceId"),
            "id": obj.get("id"),
            "is_managed": obj.get("isManaged"),
            "permission": obj.get("permission"),
            "permission_name": obj.get("permissionName"),
            "team": obj.get("team"),
            "team_avatar_url": obj.get("teamAvatarUrl"),
            "team_email": obj.get("teamEmail"),
            "team_id": obj.get("teamId"),
            "updated": obj.get("updated"),
            "user_avatar_url": obj.get("userAvatarUrl"),
            "user_email": obj.get("userEmail"),
            "user_id": obj.get("userId"),
            "user_login": obj.get("userLogin")
        })
        return _obj


