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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field
from bgrafana_api.models.dashboard_report_dto import DashboardReportDTO
from bgrafana_api.models.time_range_dto import TimeRangeDTO

class DashboardDTO(BaseModel):
    """
    DashboardDTO
    """
    dashboard: Optional[DashboardReportDTO] = None
    report_variables: Optional[Dict[str, Any]] = Field(None, alias="reportVariables")
    time_range: Optional[TimeRangeDTO] = Field(None, alias="timeRange")
    __properties = ["dashboard", "reportVariables", "timeRange"]

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
    def from_json(cls, json_str: str) -> DashboardDTO:
        """Create an instance of DashboardDTO from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of dashboard
        if self.dashboard:
            _dict['dashboard'] = self.dashboard.to_dict()
        # override the default output from pydantic by calling `to_dict()` of time_range
        if self.time_range:
            _dict['timeRange'] = self.time_range.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DashboardDTO:
        """Create an instance of DashboardDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DashboardDTO.parse_obj(obj)

        _obj = DashboardDTO.parse_obj({
            "dashboard": DashboardReportDTO.from_dict(obj.get("dashboard")) if obj.get("dashboard") is not None else None,
            "report_variables": obj.get("reportVariables"),
            "time_range": TimeRangeDTO.from_dict(obj.get("timeRange")) if obj.get("timeRange") is not None else None
        })
        return _obj

