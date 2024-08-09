# ScpsUrbandatasetSchema20UrbanDatasetValuesLineInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 
**coordinates** | [**ScpsUrbandatasetSchema20UrbanDatasetContextCoordinates**](ScpsUrbandatasetSchema20UrbanDatasetContextCoordinates.md) |  | [optional] 
**period** | [**ScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPeriod**](ScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPeriod.md) |  | [optional] 
**var_property** | [**List[ScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPropertyInner]**](ScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPropertyInner.md) |  | 

## Example

```python
from urbandatasetgateway_client.models.scps_urbandataset_schema20_urban_dataset_values_line_inner import ScpsUrbandatasetSchema20UrbanDatasetValuesLineInner

# TODO update the JSON string below
json = "{}"
# create an instance of ScpsUrbandatasetSchema20UrbanDatasetValuesLineInner from a JSON string
scps_urbandataset_schema20_urban_dataset_values_line_inner_instance = ScpsUrbandatasetSchema20UrbanDatasetValuesLineInner.from_json(json)
# print the JSON string representation of the object
print(ScpsUrbandatasetSchema20UrbanDatasetValuesLineInner.to_json())

# convert the object into a dict
scps_urbandataset_schema20_urban_dataset_values_line_inner_dict = scps_urbandataset_schema20_urban_dataset_values_line_inner_instance.to_dict()
# create an instance of ScpsUrbandatasetSchema20UrbanDatasetValuesLineInner from a dict
scps_urbandataset_schema20_urban_dataset_values_line_inner_from_dict = ScpsUrbandatasetSchema20UrbanDatasetValuesLineInner.from_dict(scps_urbandataset_schema20_urban_dataset_values_line_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


