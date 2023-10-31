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


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr

class ImportDashboardResponse(BaseModel):
    """
    ImportDashboardResponse
    """
    dashboard_id: Optional[StrictInt] = Field(None, alias="dashboardId")
    description: Optional[StrictStr] = None
    folder_id: Optional[StrictInt] = Field(None, alias="folderId")
    folder_uid: Optional[StrictStr] = Field(None, alias="folderUid")
    imported: Optional[StrictBool] = None
    imported_revision: Optional[StrictInt] = Field(None, alias="importedRevision")
    imported_uri: Optional[StrictStr] = Field(None, alias="importedUri")
    imported_url: Optional[StrictStr] = Field(None, alias="importedUrl")
    path: Optional[StrictStr] = None
    plugin_id: Optional[StrictStr] = Field(None, alias="pluginId")
    removed: Optional[StrictBool] = None
    revision: Optional[StrictInt] = None
    slug: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
    uid: Optional[StrictStr] = None
    __properties = ["dashboardId", "description", "folderId", "folderUid", "imported", "importedRevision", "importedUri", "importedUrl", "path", "pluginId", "removed", "revision", "slug", "title", "uid"]

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
    def from_json(cls, json_str: str) -> ImportDashboardResponse:
        """Create an instance of ImportDashboardResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ImportDashboardResponse:
        """Create an instance of ImportDashboardResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ImportDashboardResponse.parse_obj(obj)

        _obj = ImportDashboardResponse.parse_obj({
            "dashboard_id": obj.get("dashboardId"),
            "description": obj.get("description"),
            "folder_id": obj.get("folderId"),
            "folder_uid": obj.get("folderUid"),
            "imported": obj.get("imported"),
            "imported_revision": obj.get("importedRevision"),
            "imported_uri": obj.get("importedUri"),
            "imported_url": obj.get("importedUrl"),
            "path": obj.get("path"),
            "plugin_id": obj.get("pluginId"),
            "removed": obj.get("removed"),
            "revision": obj.get("revision"),
            "slug": obj.get("slug"),
            "title": obj.get("title"),
            "uid": obj.get("uid")
        })
        return _obj


