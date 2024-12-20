# coding: utf-8

"""
    Juniper Square Internal API

    An internal API for inter-service communication at JSQ.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from main_openapi_client.models.contact_details_attributes_employments_inner import ContactDetailsAttributesEmploymentsInner

class TestContactDetailsAttributesEmploymentsInner(unittest.TestCase):
    """ContactDetailsAttributesEmploymentsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContactDetailsAttributesEmploymentsInner:
        """Test ContactDetailsAttributesEmploymentsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContactDetailsAttributesEmploymentsInner`
        """
        model = ContactDetailsAttributesEmploymentsInner()
        if include_optional:
            return ContactDetailsAttributesEmploymentsInner(
                employer = main_openapi_client.models.contact_details_attributes_employments_inner_employer.ContactDetails_attributes_employments_inner_employer(
                    lazy_create = False, 
                    object_id = 56, 
                    object_name = 'TestCompany', 
                    object_type = 3, ),
                is_current = True,
                job_title = 'Director',
                sort_order = 1
            )
        else:
            return ContactDetailsAttributesEmploymentsInner(
        )
        """

    def testContactDetailsAttributesEmploymentsInner(self):
        """Test ContactDetailsAttributesEmploymentsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()