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
from pydantic import BaseModel, StrictInt, conlist

class SetRoleAssignmentsCommand(BaseModel):
    """
    SetRoleAssignmentsCommand
    """
    service_accounts: Optional[conlist(StrictInt)] = None
    teams: Optional[conlist(StrictInt)] = None
    users: Optional[conlist(StrictInt)] = None
    __properties = ["service_accounts", "teams", "users"]

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
    def from_json(cls, json_str: str) -> SetRoleAssignmentsCommand:
        """Create an instance of SetRoleAssignmentsCommand from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SetRoleAssignmentsCommand:
        """Create an instance of SetRoleAssignmentsCommand from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SetRoleAssignmentsCommand.parse_obj(obj)

        _obj = SetRoleAssignmentsCommand.parse_obj({
            "service_accounts": obj.get("service_accounts"),
            "teams": obj.get("teams"),
            "users": obj.get("users")
        })
        return _obj


