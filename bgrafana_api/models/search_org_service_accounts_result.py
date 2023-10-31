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
from pydantic import BaseModel, Field, StrictInt, conlist
from bgrafana_api.models.service_account_dto import ServiceAccountDTO

class SearchOrgServiceAccountsResult(BaseModel):
    """
    swagger: model  # noqa: E501
    """
    page: Optional[StrictInt] = None
    per_page: Optional[StrictInt] = Field(None, alias="perPage")
    service_accounts: Optional[conlist(ServiceAccountDTO)] = Field(None, alias="serviceAccounts")
    total_count: Optional[StrictInt] = Field(None, alias="totalCount", description="It can be used for pagination of the user list E.g. if totalCount is equal to 100 users and the perpage parameter is set to 10 then there are 10 pages of users.")
    __properties = ["page", "perPage", "serviceAccounts", "totalCount"]

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
    def from_json(cls, json_str: str) -> SearchOrgServiceAccountsResult:
        """Create an instance of SearchOrgServiceAccountsResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in service_accounts (list)
        _items = []
        if self.service_accounts:
            for _item in self.service_accounts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['serviceAccounts'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SearchOrgServiceAccountsResult:
        """Create an instance of SearchOrgServiceAccountsResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SearchOrgServiceAccountsResult.parse_obj(obj)

        _obj = SearchOrgServiceAccountsResult.parse_obj({
            "page": obj.get("page"),
            "per_page": obj.get("perPage"),
            "service_accounts": [ServiceAccountDTO.from_dict(_item) for _item in obj.get("serviceAccounts")] if obj.get("serviceAccounts") is not None else None,
            "total_count": obj.get("totalCount")
        })
        return _obj


