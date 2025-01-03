# coding: utf-8

"""
    Juniper Square Internal API

    An internal API for inter-service communication at JSQ.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from main_openapi_client.models.update_payment_pref_options import UpdatePaymentPrefOptions

class TestUpdatePaymentPrefOptions(unittest.TestCase):
    """UpdatePaymentPrefOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdatePaymentPrefOptions:
        """Test UpdatePaymentPrefOptions
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdatePaymentPrefOptions`
        """
        model = UpdatePaymentPrefOptions()
        if include_optional:
            return UpdatePaymentPrefOptions(
                verification_status = 'verified'
            )
        else:
            return UpdatePaymentPrefOptions(
        )
        """

    def testUpdatePaymentPrefOptions(self):
        """Test UpdatePaymentPrefOptions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
