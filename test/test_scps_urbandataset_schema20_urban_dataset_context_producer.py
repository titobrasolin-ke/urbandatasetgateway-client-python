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

from urbandatasetgateway_client.models.scps_urbandataset_schema20_urban_dataset_context_producer import ScpsUrbandatasetSchema20UrbanDatasetContextProducer

class TestScpsUrbandatasetSchema20UrbanDatasetContextProducer(unittest.TestCase):
    """ScpsUrbandatasetSchema20UrbanDatasetContextProducer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScpsUrbandatasetSchema20UrbanDatasetContextProducer:
        """Test ScpsUrbandatasetSchema20UrbanDatasetContextProducer
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScpsUrbandatasetSchema20UrbanDatasetContextProducer`
        """
        model = ScpsUrbandatasetSchema20UrbanDatasetContextProducer()
        if include_optional:
            return ScpsUrbandatasetSchema20UrbanDatasetContextProducer(
                id = '',
                scheme_id = ''
            )
        else:
            return ScpsUrbandatasetSchema20UrbanDatasetContextProducer(
                id = '',
        )
        """

    def testScpsUrbandatasetSchema20UrbanDatasetContextProducer(self):
        """Test ScpsUrbandatasetSchema20UrbanDatasetContextProducer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
