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
from typing import Dict, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class Rule(BaseModel):
    """
    adapted from cortex  # noqa: E501
    """
    evaluation_time: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="evaluationTime")
    health: StrictStr = Field(...)
    labels: Optional[Dict[str, StrictStr]] = Field(None, description="The custom marshaling for labels.Labels ends up doing this anyways.")
    last_error: Optional[StrictStr] = Field(None, alias="lastError")
    last_evaluation: Optional[datetime] = Field(None, alias="lastEvaluation")
    name: StrictStr = Field(...)
    query: StrictStr = Field(...)
    type: StrictStr = Field(...)
    __properties = ["evaluationTime", "health", "labels", "lastError", "lastEvaluation", "name", "query", "type"]

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
    def from_json(cls, json_str: str) -> Rule:
        """Create an instance of Rule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Rule:
        """Create an instance of Rule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Rule.parse_obj(obj)

        _obj = Rule.parse_obj({
            "evaluation_time": obj.get("evaluationTime"),
            "health": obj.get("health"),
            "labels": obj.get("labels"),
            "last_error": obj.get("lastError"),
            "last_evaluation": obj.get("lastEvaluation"),
            "name": obj.get("name"),
            "query": obj.get("query"),
            "type": obj.get("type")
        })
        return _obj


