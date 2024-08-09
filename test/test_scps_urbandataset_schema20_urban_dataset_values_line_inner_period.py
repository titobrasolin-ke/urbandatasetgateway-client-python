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

from urbandatasetgateway_client.models.scps_urbandataset_schema20_urban_dataset_values_line_inner_period import ScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPeriod

class TestScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPeriod(unittest.TestCase):
    """ScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPeriod unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPeriod:
        """Test ScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPeriod
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPeriod`
        """
        model = ScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPeriod()
        if include_optional:
            return ScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPeriod(
                start_ts = 'iR2M8880-03-31T10:01:39',
                end_ts = 'iR2M8880-03-31T10:01:39'
            )
        else:
            return ScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPeriod(
                start_ts = 'iR2M8880-03-31T10:01:39',
                end_ts = 'iR2M8880-03-31T10:01:39',
        )
        """

    def testScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPeriod(self):
        """Test ScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPeriod"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
