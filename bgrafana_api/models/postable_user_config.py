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


from typing import Dict, Optional
from pydantic import BaseModel, StrictStr
from bgrafana_api.models.postable_api_alerting_config import PostableApiAlertingConfig

class PostableUserConfig(BaseModel):
    """
    PostableUserConfig
    """
    alertmanager_config: Optional[PostableApiAlertingConfig] = None
    template_files: Optional[Dict[str, StrictStr]] = None
    __properties = ["alertmanager_config", "template_files"]

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
    def from_json(cls, json_str: str) -> PostableUserConfig:
        """Create an instance of PostableUserConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of alertmanager_config
        if self.alertmanager_config:
            _dict['alertmanager_config'] = self.alertmanager_config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PostableUserConfig:
        """Create an instance of PostableUserConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PostableUserConfig.parse_obj(obj)

        _obj = PostableUserConfig.parse_obj({
            "alertmanager_config": PostableApiAlertingConfig.from_dict(obj.get("alertmanager_config")) if obj.get("alertmanager_config") is not None else None,
            "template_files": obj.get("template_files")
        })
        return _obj


