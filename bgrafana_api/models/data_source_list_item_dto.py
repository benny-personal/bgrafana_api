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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr

class DataSourceListItemDTO(BaseModel):
    """
    DataSourceListItemDTO
    """
    access: Optional[StrictStr] = None
    basic_auth: Optional[StrictBool] = Field(None, alias="basicAuth")
    database: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    is_default: Optional[StrictBool] = Field(None, alias="isDefault")
    json_data: Optional[Dict[str, Any]] = Field(None, alias="jsonData")
    name: Optional[StrictStr] = None
    org_id: Optional[StrictInt] = Field(None, alias="orgId")
    read_only: Optional[StrictBool] = Field(None, alias="readOnly")
    type: Optional[StrictStr] = None
    type_logo_url: Optional[StrictStr] = Field(None, alias="typeLogoUrl")
    type_name: Optional[StrictStr] = Field(None, alias="typeName")
    uid: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
    user: Optional[StrictStr] = None
    __properties = ["access", "basicAuth", "database", "id", "isDefault", "jsonData", "name", "orgId", "readOnly", "type", "typeLogoUrl", "typeName", "uid", "url", "user"]

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
    def from_json(cls, json_str: str) -> DataSourceListItemDTO:
        """Create an instance of DataSourceListItemDTO from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DataSourceListItemDTO:
        """Create an instance of DataSourceListItemDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DataSourceListItemDTO.parse_obj(obj)

        _obj = DataSourceListItemDTO.parse_obj({
            "access": obj.get("access"),
            "basic_auth": obj.get("basicAuth"),
            "database": obj.get("database"),
            "id": obj.get("id"),
            "is_default": obj.get("isDefault"),
            "json_data": obj.get("jsonData"),
            "name": obj.get("name"),
            "org_id": obj.get("orgId"),
            "read_only": obj.get("readOnly"),
            "type": obj.get("type"),
            "type_logo_url": obj.get("typeLogoUrl"),
            "type_name": obj.get("typeName"),
            "uid": obj.get("uid"),
            "url": obj.get("url"),
            "user": obj.get("user")
        })
        return _obj


