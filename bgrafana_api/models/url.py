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
from pydantic import BaseModel, Field, StrictBool, StrictStr

class URL(BaseModel):
    """
    The general form represented is:  [scheme:][//[userinfo@]host][/]path[?query][#fragment]  URLs that do not start with a slash after the scheme are interpreted as:  scheme:opaque[?query][#fragment]  Note that the Path field is stored in decoded form: /%47%6f%2f becomes /Go/. A consequence is that it is impossible to tell which slashes in the Path were slashes in the raw URL and which were %2f. This distinction is rarely important, but when it is, the code should use RawPath, an optional field which only gets set if the default encoding is different from Path.  URL's String method uses the EscapedPath method to obtain the path. See the EscapedPath method for more details.  # noqa: E501
    """
    force_query: Optional[StrictBool] = Field(None, alias="ForceQuery")
    fragment: Optional[StrictStr] = Field(None, alias="Fragment")
    host: Optional[StrictStr] = Field(None, alias="Host")
    omit_host: Optional[StrictBool] = Field(None, alias="OmitHost")
    opaque: Optional[StrictStr] = Field(None, alias="Opaque")
    path: Optional[StrictStr] = Field(None, alias="Path")
    raw_fragment: Optional[StrictStr] = Field(None, alias="RawFragment")
    raw_path: Optional[StrictStr] = Field(None, alias="RawPath")
    raw_query: Optional[StrictStr] = Field(None, alias="RawQuery")
    scheme: Optional[StrictStr] = Field(None, alias="Scheme")
    user: Optional[Dict[str, Any]] = Field(None, alias="User", description="The Userinfo type is an immutable encapsulation of username and password details for a URL. An existing Userinfo value is guaranteed to have a username set (potentially empty, as allowed by RFC 2396), and optionally a password.")
    __properties = ["ForceQuery", "Fragment", "Host", "OmitHost", "Opaque", "Path", "RawFragment", "RawPath", "RawQuery", "Scheme", "User"]

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
    def from_json(cls, json_str: str) -> URL:
        """Create an instance of URL from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> URL:
        """Create an instance of URL from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return URL.parse_obj(obj)

        _obj = URL.parse_obj({
            "force_query": obj.get("ForceQuery"),
            "fragment": obj.get("Fragment"),
            "host": obj.get("Host"),
            "omit_host": obj.get("OmitHost"),
            "opaque": obj.get("Opaque"),
            "path": obj.get("Path"),
            "raw_fragment": obj.get("RawFragment"),
            "raw_path": obj.get("RawPath"),
            "raw_query": obj.get("RawQuery"),
            "scheme": obj.get("Scheme"),
            "user": obj.get("User")
        })
        return _obj

