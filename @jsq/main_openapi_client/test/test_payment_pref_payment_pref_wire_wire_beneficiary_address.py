# coding: utf-8

"""
    Juniper Square Internal API

    An internal API for inter-service communication at JSQ.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from main_openapi_client.models.payment_pref_payment_pref_wire_wire_beneficiary_address import PaymentPrefPaymentPrefWireWireBeneficiaryAddress

class TestPaymentPrefPaymentPrefWireWireBeneficiaryAddress(unittest.TestCase):
    """PaymentPrefPaymentPrefWireWireBeneficiaryAddress unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaymentPrefPaymentPrefWireWireBeneficiaryAddress:
        """Test PaymentPrefPaymentPrefWireWireBeneficiaryAddress
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentPrefPaymentPrefWireWireBeneficiaryAddress`
        """
        model = PaymentPrefPaymentPrefWireWireBeneficiaryAddress()
        if include_optional:
            return PaymentPrefPaymentPrefWireWireBeneficiaryAddress(
                street1 = '',
                street2 = '',
                street3 = '',
                city = '',
                state = '',
                region = '',
                postal_code = '',
                country = ''
            )
        else:
            return PaymentPrefPaymentPrefWireWireBeneficiaryAddress(
        )
        """

    def testPaymentPrefPaymentPrefWireWireBeneficiaryAddress(self):
        """Test PaymentPrefPaymentPrefWireWireBeneficiaryAddress"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
