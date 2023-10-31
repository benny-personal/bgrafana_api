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
from pydantic import BaseModel, Field, StrictStr, conlist, validator
from bgrafana_api.models.peer_status import PeerStatus

class ClusterStatus(BaseModel):
    """
    ClusterStatus cluster status  # noqa: E501
    """
    name: Optional[StrictStr] = Field(None, description="name")
    peers: Optional[conlist(PeerStatus)] = Field(None, description="peers")
    status: StrictStr = Field(..., description="status")
    __properties = ["name", "peers", "status"]

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('[ready settling disabled]'):
            raise ValueError("must be one of enum values ('[ready settling disabled]')")
        return value

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
    def from_json(cls, json_str: str) -> ClusterStatus:
        """Create an instance of ClusterStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in peers (list)
        _items = []
        if self.peers:
            for _item in self.peers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['peers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ClusterStatus:
        """Create an instance of ClusterStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ClusterStatus.parse_obj(obj)

        _obj = ClusterStatus.parse_obj({
            "name": obj.get("name"),
            "peers": [PeerStatus.from_dict(_item) for _item in obj.get("peers")] if obj.get("peers") is not None else None,
            "status": obj.get("status")
        })
        return _obj


