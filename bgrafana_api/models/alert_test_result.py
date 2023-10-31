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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from bgrafana_api.models.alert_test_result_log import AlertTestResultLog
from bgrafana_api.models.eval_match import EvalMatch

class AlertTestResult(BaseModel):
    """
    AlertTestResult
    """
    condition_evals: Optional[StrictStr] = Field(None, alias="conditionEvals")
    error: Optional[StrictStr] = None
    firing: Optional[StrictBool] = None
    logs: Optional[conlist(AlertTestResultLog)] = None
    matches: Optional[conlist(EvalMatch)] = None
    state: Optional[StrictStr] = None
    time_ms: Optional[StrictStr] = Field(None, alias="timeMs")
    __properties = ["conditionEvals", "error", "firing", "logs", "matches", "state", "timeMs"]

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
    def from_json(cls, json_str: str) -> AlertTestResult:
        """Create an instance of AlertTestResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in logs (list)
        _items = []
        if self.logs:
            for _item in self.logs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['logs'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in matches (list)
        _items = []
        if self.matches:
            for _item in self.matches:
                if _item:
                    _items.append(_item.to_dict())
            _dict['matches'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AlertTestResult:
        """Create an instance of AlertTestResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AlertTestResult.parse_obj(obj)

        _obj = AlertTestResult.parse_obj({
            "condition_evals": obj.get("conditionEvals"),
            "error": obj.get("error"),
            "firing": obj.get("firing"),
            "logs": [AlertTestResultLog.from_dict(_item) for _item in obj.get("logs")] if obj.get("logs") is not None else None,
            "matches": [EvalMatch.from_dict(_item) for _item in obj.get("matches")] if obj.get("matches") is not None else None,
            "state": obj.get("state"),
            "time_ms": obj.get("timeMs")
        })
        return _obj

