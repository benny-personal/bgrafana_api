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


from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, conlist
from bgrafana_api.models.data_link import DataLink
from bgrafana_api.models.field_type_config import FieldTypeConfig
from bgrafana_api.models.thresholds_config import ThresholdsConfig

class QueryStat(BaseModel):
    """
    The embedded FieldConfig's display name must be set. It corresponds to the QueryResultMetaStat on the frontend (https://github.com/grafana/grafana/blob/master/packages/grafana-data/src/types/data.ts#L53).  # noqa: E501
    """
    color: Optional[Dict[str, Any]] = Field(None, description="Map values to a display color NOTE: this interface is under development in the frontend... so simple map for now")
    custom: Optional[Dict[str, Any]] = Field(None, description="Panel Specific Values")
    decimals: Optional[StrictInt] = None
    description: Optional[StrictStr] = Field(None, description="Description is human readable field metadata")
    display_name: Optional[StrictStr] = Field(None, alias="displayName", description="DisplayName overrides Grafana default naming, should not be used from a data source")
    display_name_from_ds: Optional[StrictStr] = Field(None, alias="displayNameFromDS", description="DisplayNameFromDS overrides Grafana default naming in a better way that allows users to override it easily.")
    filterable: Optional[StrictBool] = Field(None, description="Filterable indicates if the Field's data can be filtered by additional calls.")
    interval: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Interval indicates the expected regular step between values in the series. When an interval exists, consumers can identify \"missing\" values when the expected value is not present. The grafana timeseries visualization will render disconnected values when missing values are found it the time field. The interval uses the same units as the values.  For time.Time, this is defined in milliseconds.")
    links: Optional[conlist(DataLink)] = Field(None, description="The behavior when clicking on a result")
    mappings: Optional[conlist(Dict[str, Any])] = None
    max: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="ConfFloat64 is a float64. It Marshals float64 values of NaN of Inf to null.")
    min: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="ConfFloat64 is a float64. It Marshals float64 values of NaN of Inf to null.")
    no_value: Optional[StrictStr] = Field(None, alias="noValue", description="Alternative to empty string")
    path: Optional[StrictStr] = Field(None, description="Path is an explicit path to the field in the datasource. When the frame meta includes a path, this will default to `${frame.meta.path}/${field.name}  When defined, this value can be used as an identifier within the datasource scope, and may be used as an identifier to update values in a subsequent request")
    thresholds: Optional[ThresholdsConfig] = None
    type: Optional[FieldTypeConfig] = None
    unit: Optional[StrictStr] = Field(None, description="Numeric Options")
    value: Optional[Union[StrictFloat, StrictInt]] = None
    writeable: Optional[StrictBool] = Field(None, description="Writeable indicates that the datasource knows how to update this value")
    __properties = ["color", "custom", "decimals", "description", "displayName", "displayNameFromDS", "filterable", "interval", "links", "mappings", "max", "min", "noValue", "path", "thresholds", "type", "unit", "value", "writeable"]

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
    def from_json(cls, json_str: str) -> QueryStat:
        """Create an instance of QueryStat from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # override the default output from pydantic by calling `to_dict()` of thresholds
        if self.thresholds:
            _dict['thresholds'] = self.thresholds.to_dict()
        # override the default output from pydantic by calling `to_dict()` of type
        if self.type:
            _dict['type'] = self.type.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> QueryStat:
        """Create an instance of QueryStat from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return QueryStat.parse_obj(obj)

        _obj = QueryStat.parse_obj({
            "color": obj.get("color"),
            "custom": obj.get("custom"),
            "decimals": obj.get("decimals"),
            "description": obj.get("description"),
            "display_name": obj.get("displayName"),
            "display_name_from_ds": obj.get("displayNameFromDS"),
            "filterable": obj.get("filterable"),
            "interval": obj.get("interval"),
            "links": [DataLink.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None,
            "mappings": obj.get("mappings"),
            "max": obj.get("max"),
            "min": obj.get("min"),
            "no_value": obj.get("noValue"),
            "path": obj.get("path"),
            "thresholds": ThresholdsConfig.from_dict(obj.get("thresholds")) if obj.get("thresholds") is not None else None,
            "type": FieldTypeConfig.from_dict(obj.get("type")) if obj.get("type") is not None else None,
            "unit": obj.get("unit"),
            "value": obj.get("value"),
            "writeable": obj.get("writeable")
        })
        return _obj


