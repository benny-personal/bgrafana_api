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


from typing import Any, Optional
from pydantic import BaseModel, StrictInt, StrictStr

class PostGraphiteAnnotationsCmd(BaseModel):
    """
    PostGraphiteAnnotationsCmd
    """
    data: Optional[StrictStr] = None
    tags: Optional[Any] = None
    what: Optional[StrictStr] = None
    when: Optional[StrictInt] = None
    __properties = ["data", "tags", "what", "when"]

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
    def from_json(cls, json_str: str) -> PostGraphiteAnnotationsCmd:
        """Create an instance of PostGraphiteAnnotationsCmd from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if tags (nullable) is None
        # and __fields_set__ contains the field
        if self.tags is None and "tags" in self.__fields_set__:
            _dict['tags'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PostGraphiteAnnotationsCmd:
        """Create an instance of PostGraphiteAnnotationsCmd from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PostGraphiteAnnotationsCmd.parse_obj(obj)

        _obj = PostGraphiteAnnotationsCmd.parse_obj({
            "data": obj.get("data"),
            "tags": obj.get("tags"),
            "what": obj.get("what"),
            "when": obj.get("when")
        })
        return _obj


