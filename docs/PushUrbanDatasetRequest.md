# PushUrbanDatasetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | Uniquely identifies an UrbanDataset produced by a specific Solution producer (syntax defined in the SCPS Collaboration 2.0) | 
**dataset** | [**ScpsUrbandatasetSchema20**](ScpsUrbandatasetSchema20.md) |  | 

## Example

```python
from urbandatasetgateway_client.models.push_urban_dataset_request import PushUrbanDatasetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PushUrbanDatasetRequest from a JSON string
push_urban_dataset_request_instance = PushUrbanDatasetRequest.from_json(json)
# print the JSON string representation of the object
print(PushUrbanDatasetRequest.to_json())

# convert the object into a dict
push_urban_dataset_request_dict = push_urban_dataset_request_instance.to_dict()
# create an instance of PushUrbanDatasetRequest from a dict
push_urban_dataset_request_from_dict = PushUrbanDatasetRequest.from_dict(push_urban_dataset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


