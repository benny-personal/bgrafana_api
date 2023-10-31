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


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr

class CreateDashboardSnapshot200Response(BaseModel):
    """
    CreateDashboardSnapshot200Response
    """
    delete_key: Optional[StrictStr] = Field(None, alias="deleteKey", description="Unique key used to delete the snapshot. It is different from the key so that only the creator can delete the snapshot.")
    delete_url: Optional[StrictStr] = Field(None, alias="deleteUrl")
    id: Optional[StrictInt] = Field(None, description="Snapshot id")
    key: Optional[StrictStr] = Field(None, description="Unique key")
    url: Optional[StrictStr] = None
    __properties = ["deleteKey", "deleteUrl", "id", "key", "url"]

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
    def from_json(cls, json_str: str) -> CreateDashboardSnapshot200Response:
        """Create an instance of CreateDashboardSnapshot200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateDashboardSnapshot200Response:
        """Create an instance of CreateDashboardSnapshot200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateDashboardSnapshot200Response.parse_obj(obj)

        _obj = CreateDashboardSnapshot200Response.parse_obj({
            "delete_key": obj.get("deleteKey"),
            "delete_url": obj.get("deleteUrl"),
            "id": obj.get("id"),
            "key": obj.get("key"),
            "url": obj.get("url")
        })
        return _obj


