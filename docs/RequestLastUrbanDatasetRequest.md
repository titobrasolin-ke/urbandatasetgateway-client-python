# RequestLastUrbanDatasetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | Uniquely identifies an UrbanDataset produced by a specific Solution producer (syntax defined in the SCPS Collaboration 2.0) | 

## Example

```python
from urbandatasetgateway_client.models.request_last_urban_dataset_request import RequestLastUrbanDatasetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RequestLastUrbanDatasetRequest from a JSON string
request_last_urban_dataset_request_instance = RequestLastUrbanDatasetRequest.from_json(json)
# print the JSON string representation of the object
print(RequestLastUrbanDatasetRequest.to_json())

# convert the object into a dict
request_last_urban_dataset_request_dict = request_last_urban_dataset_request_instance.to_dict()
# create an instance of RequestLastUrbanDatasetRequest from a dict
request_last_urban_dataset_request_from_dict = RequestLastUrbanDatasetRequest.from_dict(request_last_urban_dataset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


