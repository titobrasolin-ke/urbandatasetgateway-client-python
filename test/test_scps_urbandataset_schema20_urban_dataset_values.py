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

from urbandatasetgateway_client.models.scps_urbandataset_schema20_urban_dataset_values import ScpsUrbandatasetSchema20UrbanDatasetValues

class TestScpsUrbandatasetSchema20UrbanDatasetValues(unittest.TestCase):
    """ScpsUrbandatasetSchema20UrbanDatasetValues unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScpsUrbandatasetSchema20UrbanDatasetValues:
        """Test ScpsUrbandatasetSchema20UrbanDatasetValues
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScpsUrbandatasetSchema20UrbanDatasetValues`
        """
        model = ScpsUrbandatasetSchema20UrbanDatasetValues()
        if include_optional:
            return ScpsUrbandatasetSchema20UrbanDatasetValues(
                line = [
                    urbandatasetgateway_client.models.scps_urbandataset_schema_2_0_urban_dataset_values_line_inner.scps_urbandataset_schema_2_0_UrbanDataset_values_line_inner(
                        id = 56, 
                        description = '', 
                        timestamp = '', 
                        coordinates = urbandatasetgateway_client.models.scps_urbandataset_schema_2_0_urban_dataset_context_coordinates.scps_urbandataset_schema_2_0_UrbanDataset_context_coordinates(
                            format = '', 
                            latitude = 1.337, 
                            longitude = 1.337, 
                            height = 1.337, ), 
                        period = urbandatasetgateway_client.models.scps_urbandataset_schema_2_0_urban_dataset_values_line_inner_period.scps_urbandataset_schema_2_0_UrbanDataset_values_line_inner_period(
                            start_ts = 'iR2M8880-03-31T10:01:39', 
                            end_ts = 'iR2M8880-03-31T10:01:39', ), 
                        property = [
                            urbandatasetgateway_client.models.scps_urbandataset_schema_2_0_urban_dataset_values_line_inner_property_inner.scps_urbandataset_schema_2_0_UrbanDataset_values_line_inner_property_inner(
                                name = '', 
                                val = '', )
                            ], )
                    ]
            )
        else:
            return ScpsUrbandatasetSchema20UrbanDatasetValues(
                line = [
                    urbandatasetgateway_client.models.scps_urbandataset_schema_2_0_urban_dataset_values_line_inner.scps_urbandataset_schema_2_0_UrbanDataset_values_line_inner(
                        id = 56, 
                        description = '', 
                        timestamp = '', 
                        coordinates = urbandatasetgateway_client.models.scps_urbandataset_schema_2_0_urban_dataset_context_coordinates.scps_urbandataset_schema_2_0_UrbanDataset_context_coordinates(
                            format = '', 
                            latitude = 1.337, 
                            longitude = 1.337, 
                            height = 1.337, ), 
                        period = urbandatasetgateway_client.models.scps_urbandataset_schema_2_0_urban_dataset_values_line_inner_period.scps_urbandataset_schema_2_0_UrbanDataset_values_line_inner_period(
                            start_ts = 'iR2M8880-03-31T10:01:39', 
                            end_ts = 'iR2M8880-03-31T10:01:39', ), 
                        property = [
                            urbandatasetgateway_client.models.scps_urbandataset_schema_2_0_urban_dataset_values_line_inner_property_inner.scps_urbandataset_schema_2_0_UrbanDataset_values_line_inner_property_inner(
                                name = '', 
                                val = '', )
                            ], )
                    ],
        )
        """

    def testScpsUrbandatasetSchema20UrbanDatasetValues(self):
        """Test ScpsUrbandatasetSchema20UrbanDatasetValues"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
