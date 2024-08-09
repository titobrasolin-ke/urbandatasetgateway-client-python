# PushUrbanDataset200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**message** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from urbandatasetgateway_client.models.push_urban_dataset200_response import PushUrbanDataset200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PushUrbanDataset200Response from a JSON string
push_urban_dataset200_response_instance = PushUrbanDataset200Response.from_json(json)
# print the JSON string representation of the object
print(PushUrbanDataset200Response.to_json())

# convert the object into a dict
push_urban_dataset200_response_dict = push_urban_dataset200_response_instance.to_dict()
# create an instance of PushUrbanDataset200Response from a dict
push_urban_dataset200_response_from_dict = PushUrbanDataset200Response.from_dict(push_urban_dataset200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


