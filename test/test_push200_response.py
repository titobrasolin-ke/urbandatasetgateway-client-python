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

from urbandatasetgateway_client.models.push200_response import Push200Response

class TestPush200Response(unittest.TestCase):
    """Push200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Push200Response:
        """Test Push200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Push200Response`
        """
        model = Push200Response()
        if include_optional:
            return Push200Response(
                code = '',
                message = '',
                detail = ''
            )
        else:
            return Push200Response(
                code = '',
                message = '',
                detail = '',
        )
        """

    def testPush200Response(self):
        """Test Push200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
