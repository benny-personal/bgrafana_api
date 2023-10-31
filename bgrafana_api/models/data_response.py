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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from bgrafana_api.models.frame import Frame

class DataResponse(BaseModel):
    """
    A map of RefIDs (unique query identifiers) to this type makes up the Responses property of a QueryDataResponse. The Error property is used to allow for partial success responses from the containing QueryDataResponse.  # noqa: E501
    """
    error: Optional[StrictStr] = Field(None, alias="Error", description="Error is a property to be set if the corresponding DataQuery has an error.")
    frames: Optional[conlist(Frame)] = Field(None, alias="Frames", description="It is the main data container within a backend.DataResponse. There should be no `nil` entries in the Frames slice (making them pointers was a mistake).")
    status: Optional[StrictInt] = Field(None, alias="Status")
    __properties = ["Error", "Frames", "Status"]

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
    def from_json(cls, json_str: str) -> DataResponse:
        """Create an instance of DataResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in frames (list)
        _items = []
        if self.frames:
            for _item in self.frames:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Frames'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DataResponse:
        """Create an instance of DataResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DataResponse.parse_obj(obj)

        _obj = DataResponse.parse_obj({
            "error": obj.get("Error"),
            "frames": [Frame.from_dict(_item) for _item in obj.get("Frames")] if obj.get("Frames") is not None else None,
            "status": obj.get("Status")
        })
        return _obj


