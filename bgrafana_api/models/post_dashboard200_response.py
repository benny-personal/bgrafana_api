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

class PostDashboard200Response(BaseModel):
    """
    PostDashboard200Response
    """
    id: StrictStr = Field(..., description="ID The unique identifier (id) of the created/updated dashboard.")
    status: StrictStr = Field(..., description="Status status of the response.")
    title: StrictStr = Field(..., description="Slug The slug of the dashboard.")
    uid: StrictStr = Field(..., description="UID The unique identifier (uid) of the created/updated dashboard.")
    url: StrictStr = Field(..., description="URL The relative URL for accessing the created/updated dashboard.")
    version: StrictInt = Field(..., description="Version The version of the dashboard.")
    __properties = ["id", "status", "title", "uid", "url", "version"]

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
    def from_json(cls, json_str: str) -> PostDashboard200Response:
        """Create an instance of PostDashboard200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PostDashboard200Response:
        """Create an instance of PostDashboard200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PostDashboard200Response.parse_obj(obj)

        _obj = PostDashboard200Response.parse_obj({
            "id": obj.get("id"),
            "status": obj.get("status"),
            "title": obj.get("title"),
            "uid": obj.get("uid"),
            "url": obj.get("url"),
            "version": obj.get("version")
        })
        return _obj


