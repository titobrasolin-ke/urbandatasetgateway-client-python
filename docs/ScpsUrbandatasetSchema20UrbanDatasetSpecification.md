# ScpsUrbandatasetSchema20UrbanDatasetSpecification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | [optional] 
**id** | [**ScpsUrbandatasetSchema20UrbanDatasetSpecificationId**](ScpsUrbandatasetSchema20UrbanDatasetSpecificationId.md) |  | 
**name** | **str** |  | 
**uri** | **str** |  | 
**properties** | [**ScpsUrbandatasetSchema20UrbanDatasetSpecificationProperties**](ScpsUrbandatasetSchema20UrbanDatasetSpecificationProperties.md) |  | [optional] 

## Example

```python
from urbandatasetgateway_client.models.scps_urbandataset_schema20_urban_dataset_specification import ScpsUrbandatasetSchema20UrbanDatasetSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of ScpsUrbandatasetSchema20UrbanDatasetSpecification from a JSON string
scps_urbandataset_schema20_urban_dataset_specification_instance = ScpsUrbandatasetSchema20UrbanDatasetSpecification.from_json(json)
# print the JSON string representation of the object
print(ScpsUrbandatasetSchema20UrbanDatasetSpecification.to_json())

# convert the object into a dict
scps_urbandataset_schema20_urban_dataset_specification_dict = scps_urbandataset_schema20_urban_dataset_specification_instance.to_dict()
# create an instance of ScpsUrbandatasetSchema20UrbanDatasetSpecification from a dict
scps_urbandataset_schema20_urban_dataset_specification_from_dict = ScpsUrbandatasetSchema20UrbanDatasetSpecification.from_dict(scps_urbandataset_schema20_urban_dataset_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


