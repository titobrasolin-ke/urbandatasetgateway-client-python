# LastRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | Uniquely identifies an UrbanDataset produced by a specific Solution producer (syntax defined in the SCPS Collaboration 2.0) | 

## Example

```python
from urbandatasetgateway_client.models.last_request import LastRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LastRequest from a JSON string
last_request_instance = LastRequest.from_json(json)
# print the JSON string representation of the object
print(LastRequest.to_json())

# convert the object into a dict
last_request_dict = last_request_instance.to_dict()
# create an instance of LastRequest from a dict
last_request_from_dict = LastRequest.from_dict(last_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


