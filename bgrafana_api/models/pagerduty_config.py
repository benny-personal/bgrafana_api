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


from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from bgrafana_api.models.http_client_config import HTTPClientConfig
from bgrafana_api.models.pagerduty_image import PagerdutyImage
from bgrafana_api.models.pagerduty_link import PagerdutyLink
from bgrafana_api.models.url import URL

class PagerdutyConfig(BaseModel):
    """
    PagerdutyConfig
    """
    var_class: Optional[StrictStr] = Field(None, alias="class")
    client: Optional[StrictStr] = None
    client_url: Optional[StrictStr] = None
    component: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    details: Optional[Dict[str, StrictStr]] = None
    group: Optional[StrictStr] = None
    http_config: Optional[HTTPClientConfig] = None
    images: Optional[conlist(PagerdutyImage)] = None
    links: Optional[conlist(PagerdutyLink)] = None
    routing_key: Optional[StrictStr] = None
    routing_key_file: Optional[StrictStr] = None
    send_resolved: Optional[StrictBool] = None
    service_key: Optional[StrictStr] = None
    service_key_file: Optional[StrictStr] = None
    severity: Optional[StrictStr] = None
    source: Optional[StrictStr] = None
    url: Optional[URL] = None
    __properties = ["class", "client", "client_url", "component", "description", "details", "group", "http_config", "images", "links", "routing_key", "routing_key_file", "send_resolved", "service_key", "service_key_file", "severity", "source", "url"]

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
    def from_json(cls, json_str: str) -> PagerdutyConfig:
        """Create an instance of PagerdutyConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of http_config
        if self.http_config:
            _dict['http_config'] = self.http_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in images (list)
        _items = []
        if self.images:
            for _item in self.images:
                if _item:
                    _items.append(_item.to_dict())
            _dict['images'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # override the default output from pydantic by calling `to_dict()` of url
        if self.url:
            _dict['url'] = self.url.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PagerdutyConfig:
        """Create an instance of PagerdutyConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PagerdutyConfig.parse_obj(obj)

        _obj = PagerdutyConfig.parse_obj({
            "var_class": obj.get("class"),
            "client": obj.get("client"),
            "client_url": obj.get("client_url"),
            "component": obj.get("component"),
            "description": obj.get("description"),
            "details": obj.get("details"),
            "group": obj.get("group"),
            "http_config": HTTPClientConfig.from_dict(obj.get("http_config")) if obj.get("http_config") is not None else None,
            "images": [PagerdutyImage.from_dict(_item) for _item in obj.get("images")] if obj.get("images") is not None else None,
            "links": [PagerdutyLink.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None,
            "routing_key": obj.get("routing_key"),
            "routing_key_file": obj.get("routing_key_file"),
            "send_resolved": obj.get("send_resolved"),
            "service_key": obj.get("service_key"),
            "service_key_file": obj.get("service_key_file"),
            "severity": obj.get("severity"),
            "source": obj.get("source"),
            "url": URL.from_dict(obj.get("url")) if obj.get("url") is not None else None
        })
        return _obj


