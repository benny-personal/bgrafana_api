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
from pydantic import BaseModel, Field, StrictStr, conlist
from bgrafana_api.models.field2 import Field2
from bgrafana_api.models.frame_meta import FrameMeta

class Frame(BaseModel):
    """
    Each Field is well typed by its FieldType and supports optional Labels.  A Frame is a general data container for Grafana. A Frame can be table data or time series data depending on its content and field types.  # noqa: E501
    """
    fields: Optional[conlist(Field2)] = Field(None, alias="Fields", description="Fields are the columns of a frame. All Fields must be of the same the length when marshalling the Frame for transmission. There should be no `nil` entries in the Fields slice (making them pointers was a mistake).")
    meta: Optional[FrameMeta] = Field(None, alias="Meta")
    name: Optional[StrictStr] = Field(None, alias="Name", description="Name is used in some Grafana visualizations.")
    ref_id: Optional[StrictStr] = Field(None, alias="RefID", description="RefID is a property that can be set to match a Frame to its originating query.")
    __properties = ["Fields", "Meta", "Name", "RefID"]

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
    def from_json(cls, json_str: str) -> Frame:
        """Create an instance of Frame from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in fields (list)
        _items = []
        if self.fields:
            for _item in self.fields:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Fields'] = _items
        # override the default output from pydantic by calling `to_dict()` of meta
        if self.meta:
            _dict['Meta'] = self.meta.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Frame:
        """Create an instance of Frame from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Frame.parse_obj(obj)

        _obj = Frame.parse_obj({
            "fields": [Field2.from_dict(_item) for _item in obj.get("Fields")] if obj.get("Fields") is not None else None,
            "meta": FrameMeta.from_dict(obj.get("Meta")) if obj.get("Meta") is not None else None,
            "name": obj.get("Name"),
            "ref_id": obj.get("RefID")
        })
        return _obj


