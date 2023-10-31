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
from pydantic import BaseModel, conlist
from bgrafana_api.models.search_result_item import SearchResultItem

class SearchResult(BaseModel):
    """
    SearchResult
    """
    result: Optional[conlist(SearchResultItem)] = None
    __properties = ["result"]

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
    def from_json(cls, json_str: str) -> SearchResult:
        """Create an instance of SearchResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in result (list)
        _items = []
        if self.result:
            for _item in self.result:
                if _item:
                    _items.append(_item.to_dict())
            _dict['result'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SearchResult:
        """Create an instance of SearchResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SearchResult.parse_obj(obj)

        _obj = SearchResult.parse_obj({
            "result": [SearchResultItem.from_dict(_item) for _item in obj.get("result")] if obj.get("result") is not None else None
        })
        return _obj


