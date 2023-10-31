# coding: utf-8

"""
    Grafana HTTP API.

    The Grafana backend exposes an HTTP API, the same API is used by the frontend to do everything from saving dashboards, creating users and updating data sources.

    The version of the OpenAPI document: 0.0.1
    Contact: hello@grafana.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from bgrafana_api.api.annotations_api import AnnotationsApi  # noqa: E501


class TestAnnotationsApi(unittest.TestCase):
    """AnnotationsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AnnotationsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_delete_annotation_by_id(self) -> None:
        """Test case for delete_annotation_by_id

        Delete Annotation By ID.  # noqa: E501
        """
        pass

    def test_get_annotation_by_id(self) -> None:
        """Test case for get_annotation_by_id

        Get Annotation by ID.  # noqa: E501
        """
        pass

    def test_get_annotation_tags(self) -> None:
        """Test case for get_annotation_tags

        Find Annotations Tags.  # noqa: E501
        """
        pass

    def test_get_annotations(self) -> None:
        """Test case for get_annotations

        Find Annotations.  # noqa: E501
        """
        pass

    def test_mass_delete_annotations(self) -> None:
        """Test case for mass_delete_annotations

        Delete multiple annotations.  # noqa: E501
        """
        pass

    def test_patch_annotation(self) -> None:
        """Test case for patch_annotation

        Patch Annotation.  # noqa: E501
        """
        pass

    def test_post_annotation(self) -> None:
        """Test case for post_annotation

        Create Annotation.  # noqa: E501
        """
        pass

    def test_post_graphite_annotation(self) -> None:
        """Test case for post_graphite_annotation

        Create Annotation in Graphite format.  # noqa: E501
        """
        pass

    def test_update_annotation(self) -> None:
        """Test case for update_annotation

        Update Annotation.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()