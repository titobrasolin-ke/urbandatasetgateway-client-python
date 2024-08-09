# RequestLastUrbanDataset200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**message** | **str** |  | 
**dataset** | [**ScpsUrbandatasetSchema20**](ScpsUrbandatasetSchema20.md) |  | 

## Example

```python
from urbandatasetgateway_client.models.request_last_urban_dataset200_response import RequestLastUrbanDataset200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RequestLastUrbanDataset200Response from a JSON string
request_last_urban_dataset200_response_instance = RequestLastUrbanDataset200Response.from_json(json)
# print the JSON string representation of the object
print(RequestLastUrbanDataset200Response.to_json())

# convert the object into a dict
request_last_urban_dataset200_response_dict = request_last_urban_dataset200_response_instance.to_dict()
# create an instance of RequestLastUrbanDataset200Response from a dict
request_last_urban_dataset200_response_from_dict = RequestLastUrbanDataset200Response.from_dict(request_last_urban_dataset200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


