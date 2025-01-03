# coding: utf-8

"""
    Juniper Square Internal API

    An internal API for inter-service communication at JSQ.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from main_openapi_client.models.bulk_update_developer_feature_flags400_response import BulkUpdateDeveloperFeatureFlags400Response

class TestBulkUpdateDeveloperFeatureFlags400Response(unittest.TestCase):
    """BulkUpdateDeveloperFeatureFlags400Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BulkUpdateDeveloperFeatureFlags400Response:
        """Test BulkUpdateDeveloperFeatureFlags400Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BulkUpdateDeveloperFeatureFlags400Response`
        """
        model = BulkUpdateDeveloperFeatureFlags400Response()
        if include_optional:
            return BulkUpdateDeveloperFeatureFlags400Response(
                var_field = '',
                message = '',
                exception = ''
            )
        else:
            return BulkUpdateDeveloperFeatureFlags400Response(
                message = '',
        )
        """

    def testBulkUpdateDeveloperFeatureFlags400Response(self):
        """Test BulkUpdateDeveloperFeatureFlags400Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
