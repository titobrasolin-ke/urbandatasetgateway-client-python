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

from urbandatasetgateway_client.models.scps_urbandataset_schema20_urban_dataset_values_line_inner_property_inner import ScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPropertyInner

class TestScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPropertyInner(unittest.TestCase):
    """ScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPropertyInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPropertyInner:
        """Test ScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPropertyInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPropertyInner`
        """
        model = ScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPropertyInner()
        if include_optional:
            return ScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPropertyInner(
                name = '',
                val = '',
                var_property = [
                    urbandatasetgateway_client.models.scps_urbandataset_schema_2_0_urban_dataset_values_line_inner_property_inner_property_inner.scps_urbandataset_schema_2_0_UrbanDataset_values_line_inner_property_inner_property_inner(
                        name = '', 
                        val = '', )
                    ]
            )
        else:
            return ScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPropertyInner(
                name = '',
        )
        """

    def testScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPropertyInner(self):
        """Test ScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPropertyInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
