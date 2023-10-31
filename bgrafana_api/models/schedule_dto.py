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

class ScheduleDTO(BaseModel):
    """
    ScheduleDTO
    """
    day: Optional[StrictStr] = None
    day_of_month: Optional[StrictStr] = Field(None, alias="dayOfMonth")
    end_date: Optional[datetime] = Field(None, alias="endDate")
    frequency: Optional[StrictStr] = None
    hour: Optional[StrictInt] = None
    interval_amount: Optional[StrictInt] = Field(None, alias="intervalAmount")
    interval_frequency: Optional[StrictStr] = Field(None, alias="intervalFrequency")
    minute: Optional[StrictInt] = None
    start_date: Optional[datetime] = Field(None, alias="startDate")
    time_zone: Optional[StrictStr] = Field(None, alias="timeZone")
    workdays_only: Optional[StrictBool] = Field(None, alias="workdaysOnly")
    __properties = ["day", "dayOfMonth", "endDate", "frequency", "hour", "intervalAmount", "intervalFrequency", "minute", "startDate", "timeZone", "workdaysOnly"]

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
    def from_json(cls, json_str: str) -> ScheduleDTO:
        """Create an instance of ScheduleDTO from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ScheduleDTO:
        """Create an instance of ScheduleDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ScheduleDTO.parse_obj(obj)

        _obj = ScheduleDTO.parse_obj({
            "day": obj.get("day"),
            "day_of_month": obj.get("dayOfMonth"),
            "end_date": obj.get("endDate"),
            "frequency": obj.get("frequency"),
            "hour": obj.get("hour"),
            "interval_amount": obj.get("intervalAmount"),
            "interval_frequency": obj.get("intervalFrequency"),
            "minute": obj.get("minute"),
            "start_date": obj.get("startDate"),
            "time_zone": obj.get("timeZone"),
            "workdays_only": obj.get("workdaysOnly")
        })
        return _obj

