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


from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from bgrafana_api.models.notice import Notice
from bgrafana_api.models.query_stat import QueryStat

class FrameMeta(BaseModel):
    """
    https://github.com/grafana/grafana/blob/master/packages/grafana-data/src/types/data.ts#L11 NOTE -- in javascript this can accept any `[key: string]: any;` however this interface only exposes the values we want to be exposed  # noqa: E501
    """
    channel: Optional[StrictStr] = Field(None, description="Channel is the path to a stream in grafana live that has real-time updates for this data.")
    custom: Optional[Any] = Field(None, description="Custom datasource specific values.")
    data_topic: Optional[StrictStr] = Field(None, alias="dataTopic", description="nolint:revive")
    executed_query_string: Optional[StrictStr] = Field(None, alias="executedQueryString", description="ExecutedQueryString is the raw query sent to the underlying system. All macros and templating have been applied.  When metadata contains this value, it will be shown in the query inspector.")
    notices: Optional[conlist(Notice)] = Field(None, description="Notices provide additional information about the data in the Frame that Grafana can display to the user in the user interface.")
    path: Optional[StrictStr] = Field(None, description="Path is a browsable path on the datasource.")
    path_separator: Optional[StrictStr] = Field(None, alias="pathSeparator", description="PathSeparator defines the separator pattern to decode a hierarchy. The default separator is '/'.")
    preferred_visualisation_type: Optional[StrictStr] = Field(None, alias="preferredVisualisationType")
    stats: Optional[conlist(QueryStat)] = Field(None, description="Stats is an array of query result statistics.")
    type: Optional[StrictStr] = Field(None, description="A FrameType string, when present in a frame's metadata, asserts that the frame's structure conforms to the FrameType's specification. This property is currently optional, so FrameType may be FrameTypeUnknown even if the properties of the Frame correspond to a defined FrameType.")
    type_version: Optional[conlist(StrictInt)] = Field(None, alias="typeVersion")
    __properties = ["channel", "custom", "dataTopic", "executedQueryString", "notices", "path", "pathSeparator", "preferredVisualisationType", "stats", "type", "typeVersion"]

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
    def from_json(cls, json_str: str) -> FrameMeta:
        """Create an instance of FrameMeta from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in notices (list)
        _items = []
        if self.notices:
            for _item in self.notices:
                if _item:
                    _items.append(_item.to_dict())
            _dict['notices'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in stats (list)
        _items = []
        if self.stats:
            for _item in self.stats:
                if _item:
                    _items.append(_item.to_dict())
            _dict['stats'] = _items
        # set to None if custom (nullable) is None
        # and __fields_set__ contains the field
        if self.custom is None and "custom" in self.__fields_set__:
            _dict['custom'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FrameMeta:
        """Create an instance of FrameMeta from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FrameMeta.parse_obj(obj)

        _obj = FrameMeta.parse_obj({
            "channel": obj.get("channel"),
            "custom": obj.get("custom"),
            "data_topic": obj.get("dataTopic"),
            "executed_query_string": obj.get("executedQueryString"),
            "notices": [Notice.from_dict(_item) for _item in obj.get("notices")] if obj.get("notices") is not None else None,
            "path": obj.get("path"),
            "path_separator": obj.get("pathSeparator"),
            "preferred_visualisation_type": obj.get("preferredVisualisationType"),
            "stats": [QueryStat.from_dict(_item) for _item in obj.get("stats")] if obj.get("stats") is not None else None,
            "type": obj.get("type"),
            "type_version": obj.get("typeVersion")
        })
        return _obj


