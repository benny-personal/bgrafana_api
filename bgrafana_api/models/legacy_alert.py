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
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr

class LegacyAlert(BaseModel):
    """
    LegacyAlert
    """
    created: Optional[datetime] = Field(None, alias="Created")
    dashboard_id: Optional[StrictInt] = Field(None, alias="DashboardID")
    eval_data: Optional[Dict[str, Any]] = Field(None, alias="EvalData")
    execution_error: Optional[StrictStr] = Field(None, alias="ExecutionError")
    var_for: Optional[StrictInt] = Field(None, alias="For")
    frequency: Optional[StrictInt] = Field(None, alias="Frequency")
    handler: Optional[StrictInt] = Field(None, alias="Handler")
    id: Optional[StrictInt] = Field(None, alias="ID")
    message: Optional[StrictStr] = Field(None, alias="Message")
    name: Optional[StrictStr] = Field(None, alias="Name")
    new_state_date: Optional[datetime] = Field(None, alias="NewStateDate")
    org_id: Optional[StrictInt] = Field(None, alias="OrgID")
    panel_id: Optional[StrictInt] = Field(None, alias="PanelID")
    settings: Optional[Dict[str, Any]] = Field(None, alias="Settings")
    severity: Optional[StrictStr] = Field(None, alias="Severity")
    silenced: Optional[StrictBool] = Field(None, alias="Silenced")
    state: Optional[StrictStr] = Field(None, alias="State")
    state_changes: Optional[StrictInt] = Field(None, alias="StateChanges")
    updated: Optional[datetime] = Field(None, alias="Updated")
    version: Optional[StrictInt] = Field(None, alias="Version")
    __properties = ["Created", "DashboardID", "EvalData", "ExecutionError", "For", "Frequency", "Handler", "ID", "Message", "Name", "NewStateDate", "OrgID", "PanelID", "Settings", "Severity", "Silenced", "State", "StateChanges", "Updated", "Version"]

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
    def from_json(cls, json_str: str) -> LegacyAlert:
        """Create an instance of LegacyAlert from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LegacyAlert:
        """Create an instance of LegacyAlert from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LegacyAlert.parse_obj(obj)

        _obj = LegacyAlert.parse_obj({
            "created": obj.get("Created"),
            "dashboard_id": obj.get("DashboardID"),
            "eval_data": obj.get("EvalData"),
            "execution_error": obj.get("ExecutionError"),
            "var_for": obj.get("For"),
            "frequency": obj.get("Frequency"),
            "handler": obj.get("Handler"),
            "id": obj.get("ID"),
            "message": obj.get("Message"),
            "name": obj.get("Name"),
            "new_state_date": obj.get("NewStateDate"),
            "org_id": obj.get("OrgID"),
            "panel_id": obj.get("PanelID"),
            "settings": obj.get("Settings"),
            "severity": obj.get("Severity"),
            "silenced": obj.get("Silenced"),
            "state": obj.get("State"),
            "state_changes": obj.get("StateChanges"),
            "updated": obj.get("Updated"),
            "version": obj.get("Version")
        })
        return _obj


