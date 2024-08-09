# coding: utf-8

"""
    UrbanDatasetGateway - OpenAPI 3.0

    This technical specification is one of the **Smart City Platform Specification (SCPS) for Interoperability Layer** [https://smartcityplatform.enea.it/#/en/specification/](https://smartcityplatform.enea.it/#/en/specification/)

    The version of the OpenAPI document: 1.0.0
    Contact: tito.brasolin@kerberos.energy
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from urbandatasetgateway_client.models.scps_urbandataset_schema20_urban_dataset_values_line_inner_property_inner_property_inner import ScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPropertyInnerPropertyInner

class TestScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPropertyInnerPropertyInner(unittest.TestCase):
    """ScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPropertyInnerPropertyInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPropertyInnerPropertyInner:
        """Test ScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPropertyInnerPropertyInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPropertyInnerPropertyInner`
        """
        model = ScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPropertyInnerPropertyInner()
        if include_optional:
            return ScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPropertyInnerPropertyInner(
                name = '',
                val = ''
            )
        else:
            return ScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPropertyInnerPropertyInner(
                name = '',
        )
        """

    def testScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPropertyInnerPropertyInner(self):
        """Test ScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPropertyInnerPropertyInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
