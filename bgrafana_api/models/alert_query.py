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
from pydantic import BaseModel, Field, StrictStr
from bgrafana_api.models.relative_time_range import RelativeTimeRange

class AlertQuery(BaseModel):
    """
    AlertQuery
    """
    datasource_uid: Optional[StrictStr] = Field(None, alias="datasourceUid", description="Grafana data source unique identifier; it should be '__expr__' for a Server Side Expression operation.")
    model: Optional[Dict[str, Any]] = Field(None, description="JSON is the raw JSON query and includes the above properties as well as custom properties.")
    query_type: Optional[StrictStr] = Field(None, alias="queryType", description="QueryType is an optional identifier for the type of query. It can be used to distinguish different types of queries.")
    ref_id: Optional[StrictStr] = Field(None, alias="refId", description="RefID is the unique identifier of the query, set by the frontend call.")
    relative_time_range: Optional[RelativeTimeRange] = Field(None, alias="relativeTimeRange")
    __properties = ["datasourceUid", "model", "queryType", "refId", "relativeTimeRange"]

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
    def from_json(cls, json_str: str) -> AlertQuery:
        """Create an instance of AlertQuery from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of relative_time_range
        if self.relative_time_range:
            _dict['relativeTimeRange'] = self.relative_time_range.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AlertQuery:
        """Create an instance of AlertQuery from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AlertQuery.parse_obj(obj)

        _obj = AlertQuery.parse_obj({
            "datasource_uid": obj.get("datasourceUid"),
            "model": obj.get("model"),
            "query_type": obj.get("queryType"),
            "ref_id": obj.get("refId"),
            "relative_time_range": RelativeTimeRange.from_dict(obj.get("relativeTimeRange")) if obj.get("relativeTimeRange") is not None else None
        })
        return _obj


