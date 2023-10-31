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



from pydantic import BaseModel, Field, StrictInt, StrictStr
from bgrafana_api.models.data_source import DataSource

class AddDataSource200Response(BaseModel):
    """
    AddDataSource200Response
    """
    datasource: DataSource = Field(...)
    id: StrictInt = Field(..., description="ID Identifier of the new data source.")
    message: StrictStr = Field(..., description="Message Message of the deleted dashboard.")
    name: StrictStr = Field(..., description="Name of the new data source.")
    __properties = ["datasource", "id", "message", "name"]

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
    def from_json(cls, json_str: str) -> AddDataSource200Response:
        """Create an instance of AddDataSource200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of datasource
        if self.datasource:
            _dict['datasource'] = self.datasource.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AddDataSource200Response:
        """Create an instance of AddDataSource200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AddDataSource200Response.parse_obj(obj)

        _obj = AddDataSource200Response.parse_obj({
            "datasource": DataSource.from_dict(obj.get("datasource")) if obj.get("datasource") is not None else None,
            "id": obj.get("id"),
            "message": obj.get("message"),
            "name": obj.get("name")
        })
        return _obj

