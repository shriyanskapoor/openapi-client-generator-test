# coding: utf-8

"""
    Juniper Square Internal API

    An internal API for inter-service communication at JSQ.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from main_openapi_client.models.update_feature_flag import UpdateFeatureFlag

class TestUpdateFeatureFlag(unittest.TestCase):
    """UpdateFeatureFlag unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateFeatureFlag:
        """Test UpdateFeatureFlag
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateFeatureFlag`
        """
        model = UpdateFeatureFlag()
        if include_optional:
            return UpdateFeatureFlag(
                is_enabled = True
            )
        else:
            return UpdateFeatureFlag(
                is_enabled = True,
        )
        """

    def testUpdateFeatureFlag(self):
        """Test UpdateFeatureFlag"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
