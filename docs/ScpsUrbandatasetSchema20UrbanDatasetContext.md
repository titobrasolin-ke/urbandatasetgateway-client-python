# ScpsUrbandatasetSchema20UrbanDatasetContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**producer** | [**ScpsUrbandatasetSchema20UrbanDatasetContextProducer**](ScpsUrbandatasetSchema20UrbanDatasetContextProducer.md) |  | 
**time_zone** | **str** |  | 
**timestamp** | **str** |  | 
**coordinates** | [**ScpsUrbandatasetSchema20UrbanDatasetContextCoordinates**](ScpsUrbandatasetSchema20UrbanDatasetContextCoordinates.md) |  | 
**language** | **str** |  | [optional] 
**note** | **str** |  | [optional] 

## Example

```python
from urbandatasetgateway_client.models.scps_urbandataset_schema20_urban_dataset_context import ScpsUrbandatasetSchema20UrbanDatasetContext

# TODO update the JSON string below
json = "{}"
# create an instance of ScpsUrbandatasetSchema20UrbanDatasetContext from a JSON string
scps_urbandataset_schema20_urban_dataset_context_instance = ScpsUrbandatasetSchema20UrbanDatasetContext.from_json(json)
# print the JSON string representation of the object
print(ScpsUrbandatasetSchema20UrbanDatasetContext.to_json())

# convert the object into a dict
scps_urbandataset_schema20_urban_dataset_context_dict = scps_urbandataset_schema20_urban_dataset_context_instance.to_dict()
# create an instance of ScpsUrbandatasetSchema20UrbanDatasetContext from a dict
scps_urbandataset_schema20_urban_dataset_context_from_dict = ScpsUrbandatasetSchema20UrbanDatasetContext.from_dict(scps_urbandataset_schema20_urban_dataset_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


