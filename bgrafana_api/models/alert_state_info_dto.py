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
from pydantic import BaseModel, Field, StrictInt, StrictStr

class AlertStateInfoDTO(BaseModel):
    """
    AlertStateInfoDTO
    """
    dashboard_id: Optional[StrictInt] = Field(None, alias="dashboardId")
    id: Optional[StrictInt] = None
    new_state_date: Optional[datetime] = Field(None, alias="newStateDate")
    panel_id: Optional[StrictInt] = Field(None, alias="panelId")
    state: Optional[StrictStr] = None
    __properties = ["dashboardId", "id", "newStateDate", "panelId", "state"]

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
    def from_json(cls, json_str: str) -> AlertStateInfoDTO:
        """Create an instance of AlertStateInfoDTO from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AlertStateInfoDTO:
        """Create an instance of AlertStateInfoDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AlertStateInfoDTO.parse_obj(obj)

        _obj = AlertStateInfoDTO.parse_obj({
            "dashboard_id": obj.get("dashboardId"),
            "id": obj.get("id"),
            "new_state_date": obj.get("newStateDate"),
            "panel_id": obj.get("panelId"),
            "state": obj.get("state")
        })
        return _obj


