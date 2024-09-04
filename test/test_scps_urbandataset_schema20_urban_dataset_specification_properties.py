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

from urbandatasetgateway_client.models.scps_urbandataset_schema20_urban_dataset_specification_properties import ScpsUrbandatasetSchema20UrbanDatasetSpecificationProperties

class TestScpsUrbandatasetSchema20UrbanDatasetSpecificationProperties(unittest.TestCase):
    """ScpsUrbandatasetSchema20UrbanDatasetSpecificationProperties unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScpsUrbandatasetSchema20UrbanDatasetSpecificationProperties:
        """Test ScpsUrbandatasetSchema20UrbanDatasetSpecificationProperties
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScpsUrbandatasetSchema20UrbanDatasetSpecificationProperties`
        """
        model = ScpsUrbandatasetSchema20UrbanDatasetSpecificationProperties()
        if include_optional:
            return ScpsUrbandatasetSchema20UrbanDatasetSpecificationProperties(
                property_definition = [
                    urbandatasetgateway_client.models.scps_urbandataset_schema_2_0_urban_dataset_specification_properties_property_definition_inner.scps_urbandataset_schema_2_0_UrbanDataset_specification_properties_propertyDefinition_inner(
                        property_name = '', 
                        property_description = '', 
                        data_type = '', 
                        code_list = '', 
                        unit_of_measure = '', 
                        measurement_type = '', 
                        sub_properties = urbandatasetgateway_client.models.scps_urbandataset_schema_2_0_urban_dataset_specification_properties_property_definition_inner_sub_properties.scps_urbandataset_schema_2_0_UrbanDataset_specification_properties_propertyDefinition_inner_subProperties(
                            property_name = [
                                ''
                                ], ), )
                    ]
            )
        else:
            return ScpsUrbandatasetSchema20UrbanDatasetSpecificationProperties(
                property_definition = [
                    urbandatasetgateway_client.models.scps_urbandataset_schema_2_0_urban_dataset_specification_properties_property_definition_inner.scps_urbandataset_schema_2_0_UrbanDataset_specification_properties_propertyDefinition_inner(
                        property_name = '', 
                        property_description = '', 
                        data_type = '', 
                        code_list = '', 
                        unit_of_measure = '', 
                        measurement_type = '', 
                        sub_properties = urbandatasetgateway_client.models.scps_urbandataset_schema_2_0_urban_dataset_specification_properties_property_definition_inner_sub_properties.scps_urbandataset_schema_2_0_UrbanDataset_specification_properties_propertyDefinition_inner_subProperties(
                            property_name = [
                                ''
                                ], ), )
                    ],
        )
        """

    def testScpsUrbandatasetSchema20UrbanDatasetSpecificationProperties(self):
        """Test ScpsUrbandatasetSchema20UrbanDatasetSpecificationProperties"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
