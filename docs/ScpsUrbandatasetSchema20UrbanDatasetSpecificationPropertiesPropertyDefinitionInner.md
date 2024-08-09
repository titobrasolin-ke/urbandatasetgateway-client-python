# ScpsUrbandatasetSchema20UrbanDatasetSpecificationPropertiesPropertyDefinitionInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_name** | **str** |  | 
**property_description** | **str** |  | [optional] 
**data_type** | **str** |  | [optional] 
**code_list** | **str** |  | [optional] 
**unit_of_measure** | **str** |  | [optional] 
**measurement_type** | **str** |  | [optional] 
**sub_properties** | [**ScpsUrbandatasetSchema20UrbanDatasetSpecificationPropertiesPropertyDefinitionInnerSubProperties**](ScpsUrbandatasetSchema20UrbanDatasetSpecificationPropertiesPropertyDefinitionInnerSubProperties.md) |  | [optional] 

## Example

```python
from urbandatasetgateway_client.models.scps_urbandataset_schema20_urban_dataset_specification_properties_property_definition_inner import ScpsUrbandatasetSchema20UrbanDatasetSpecificationPropertiesPropertyDefinitionInner

# TODO update the JSON string below
json = "{}"
# create an instance of ScpsUrbandatasetSchema20UrbanDatasetSpecificationPropertiesPropertyDefinitionInner from a JSON string
scps_urbandataset_schema20_urban_dataset_specification_properties_property_definition_inner_instance = ScpsUrbandatasetSchema20UrbanDatasetSpecificationPropertiesPropertyDefinitionInner.from_json(json)
# print the JSON string representation of the object
print(ScpsUrbandatasetSchema20UrbanDatasetSpecificationPropertiesPropertyDefinitionInner.to_json())

# convert the object into a dict
scps_urbandataset_schema20_urban_dataset_specification_properties_property_definition_inner_dict = scps_urbandataset_schema20_urban_dataset_specification_properties_property_definition_inner_instance.to_dict()
# create an instance of ScpsUrbandatasetSchema20UrbanDatasetSpecificationPropertiesPropertyDefinitionInner from a dict
scps_urbandataset_schema20_urban_dataset_specification_properties_property_definition_inner_from_dict = ScpsUrbandatasetSchema20UrbanDatasetSpecificationPropertiesPropertyDefinitionInner.from_dict(scps_urbandataset_schema20_urban_dataset_specification_properties_property_definition_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


