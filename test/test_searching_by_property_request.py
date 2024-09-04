# coding: utf-8

"""
    UrbanDatasetGateway - OpenAPI 3.0

    **Smart City Platform Specification (SCPS) for Interoperability Layer** [https://smartcityplatform.enea.it/#/en/specification/](https://smartcityplatform.enea.it/#/en/specification/)  **Smart City Platform Specification (SCPS) Communication 2.0** [https://smartcityplatform.enea.it/#/en/specification/communication/2.0/](https://smartcityplatform.enea.it/#/en/specification/communication/2.0/)

    The version of the OpenAPI document: 2.0.0
    Contact: tito.brasolin@kerberos.energy
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from urbandatasetgateway_client.models.searching_by_property_request import SearchingByPropertyRequest

class TestSearchingByPropertyRequest(unittest.TestCase):
    """SearchingByPropertyRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchingByPropertyRequest:
        """Test SearchingByPropertyRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchingByPropertyRequest`
        """
        model = SearchingByPropertyRequest()
        if include_optional:
            return SearchingByPropertyRequest(
                resource_id = '',
                property_name = '',
                property_value = '',
                period_start = '',
                period_end = '',
                center_latitude = '',
                center_longitude = '',
                distance = ''
            )
        else:
            return SearchingByPropertyRequest(
                resource_id = '',
                property_name = '',
                property_value = '',
        )
        """

    def testSearchingByPropertyRequest(self):
        """Test SearchingByPropertyRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
