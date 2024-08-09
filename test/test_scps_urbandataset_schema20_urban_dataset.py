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

from urbandatasetgateway_client.models.scps_urbandataset_schema20_urban_dataset import ScpsUrbandatasetSchema20UrbanDataset

class TestScpsUrbandatasetSchema20UrbanDataset(unittest.TestCase):
    """ScpsUrbandatasetSchema20UrbanDataset unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScpsUrbandatasetSchema20UrbanDataset:
        """Test ScpsUrbandatasetSchema20UrbanDataset
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScpsUrbandatasetSchema20UrbanDataset`
        """
        model = ScpsUrbandatasetSchema20UrbanDataset()
        if include_optional:
            return ScpsUrbandatasetSchema20UrbanDataset(
                context = urbandatasetgateway_client.models.scps_urbandataset_schema_2_0_urban_dataset_context.scps_urbandataset_schema_2_0_UrbanDataset_context(
                    producer = urbandatasetgateway_client.models.scps_urbandataset_schema_2_0_urban_dataset_context_producer.scps_urbandataset_schema_2_0_UrbanDataset_context_producer(
                        id = '', 
                        scheme_id = '', ), 
                    time_zone = '', 
                    timestamp = 'iR2M8880-03-31T10:01:39', 
                    coordinates = urbandatasetgateway_client.models.scps_urbandataset_schema_2_0_urban_dataset_context_coordinates.scps_urbandataset_schema_2_0_UrbanDataset_context_coordinates(
                        format = '', 
                        latitude = 1.337, 
                        longitude = 1.337, 
                        height = 1.337, ), 
                    language = '', 
                    note = '', ),
                specification = urbandatasetgateway_client.models.scps_urbandataset_schema_2_0_urban_dataset_specification.scps_urbandataset_schema_2_0_UrbanDataset_specification(
                    version = '', 
                    id = urbandatasetgateway_client.models.scps_urbandataset_schema_2_0_urban_dataset_specification_id.scps_urbandataset_schema_2_0_UrbanDataset_specification_id(
                        value = '', 
                        scheme_id = '', ), 
                    name = '', 
                    uri = '', 
                    properties = urbandatasetgateway_client.models.scps_urbandataset_schema_2_0_urban_dataset_specification_properties.scps_urbandataset_schema_2_0_UrbanDataset_specification_properties(
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
                            ], ), ),
                values = urbandatasetgateway_client.models.scps_urbandataset_schema_2_0_urban_dataset_values.scps_urbandataset_schema_2_0_UrbanDataset_values(
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
                        ], )
            )
        else:
            return ScpsUrbandatasetSchema20UrbanDataset(
                context = urbandatasetgateway_client.models.scps_urbandataset_schema_2_0_urban_dataset_context.scps_urbandataset_schema_2_0_UrbanDataset_context(
                    producer = urbandatasetgateway_client.models.scps_urbandataset_schema_2_0_urban_dataset_context_producer.scps_urbandataset_schema_2_0_UrbanDataset_context_producer(
                        id = '', 
                        scheme_id = '', ), 
                    time_zone = '', 
                    timestamp = 'iR2M8880-03-31T10:01:39', 
                    coordinates = urbandatasetgateway_client.models.scps_urbandataset_schema_2_0_urban_dataset_context_coordinates.scps_urbandataset_schema_2_0_UrbanDataset_context_coordinates(
                        format = '', 
                        latitude = 1.337, 
                        longitude = 1.337, 
                        height = 1.337, ), 
                    language = '', 
                    note = '', ),
                specification = urbandatasetgateway_client.models.scps_urbandataset_schema_2_0_urban_dataset_specification.scps_urbandataset_schema_2_0_UrbanDataset_specification(
                    version = '', 
                    id = urbandatasetgateway_client.models.scps_urbandataset_schema_2_0_urban_dataset_specification_id.scps_urbandataset_schema_2_0_UrbanDataset_specification_id(
                        value = '', 
                        scheme_id = '', ), 
                    name = '', 
                    uri = '', 
                    properties = urbandatasetgateway_client.models.scps_urbandataset_schema_2_0_urban_dataset_specification_properties.scps_urbandataset_schema_2_0_UrbanDataset_specification_properties(
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
                            ], ), ),
                values = urbandatasetgateway_client.models.scps_urbandataset_schema_2_0_urban_dataset_values.scps_urbandataset_schema_2_0_UrbanDataset_values(
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
                        ], ),
        )
        """

    def testScpsUrbandatasetSchema20UrbanDataset(self):
        """Test ScpsUrbandatasetSchema20UrbanDataset"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
