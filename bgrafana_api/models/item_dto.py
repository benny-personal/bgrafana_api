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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist

class ItemDTO(BaseModel):
    """
    ItemDTO
    """
    alert_id: Optional[StrictInt] = Field(None, alias="alertId")
    alert_name: Optional[StrictStr] = Field(None, alias="alertName")
    avatar_url: Optional[StrictStr] = Field(None, alias="avatarUrl")
    created: Optional[StrictInt] = None
    dashboard_id: Optional[StrictInt] = Field(None, alias="dashboardId")
    dashboard_uid: Optional[StrictStr] = Field(None, alias="dashboardUID")
    data: Optional[Dict[str, Any]] = None
    email: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    login: Optional[StrictStr] = None
    new_state: Optional[StrictStr] = Field(None, alias="newState")
    panel_id: Optional[StrictInt] = Field(None, alias="panelId")
    prev_state: Optional[StrictStr] = Field(None, alias="prevState")
    tags: Optional[conlist(StrictStr)] = None
    text: Optional[StrictStr] = None
    time: Optional[StrictInt] = None
    time_end: Optional[StrictInt] = Field(None, alias="timeEnd")
    updated: Optional[StrictInt] = None
    user_id: Optional[StrictInt] = Field(None, alias="userId")
    __properties = ["alertId", "alertName", "avatarUrl", "created", "dashboardId", "dashboardUID", "data", "email", "id", "login", "newState", "panelId", "prevState", "tags", "text", "time", "timeEnd", "updated", "userId"]

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
    def from_json(cls, json_str: str) -> ItemDTO:
        """Create an instance of ItemDTO from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ItemDTO:
        """Create an instance of ItemDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ItemDTO.parse_obj(obj)

        _obj = ItemDTO.parse_obj({
            "alert_id": obj.get("alertId"),
            "alert_name": obj.get("alertName"),
            "avatar_url": obj.get("avatarUrl"),
            "created": obj.get("created"),
            "dashboard_id": obj.get("dashboardId"),
            "dashboard_uid": obj.get("dashboardUID"),
            "data": obj.get("data"),
            "email": obj.get("email"),
            "id": obj.get("id"),
            "login": obj.get("login"),
            "new_state": obj.get("newState"),
            "panel_id": obj.get("panelId"),
            "prev_state": obj.get("prevState"),
            "tags": obj.get("tags"),
            "text": obj.get("text"),
            "time": obj.get("time"),
            "time_end": obj.get("timeEnd"),
            "updated": obj.get("updated"),
            "user_id": obj.get("userId")
        })
        return _obj


