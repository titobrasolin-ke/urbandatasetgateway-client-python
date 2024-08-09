# LastRequest200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**message** | **str** |  | 
**dataset** | [**ScpsUrbandatasetSchema20**](ScpsUrbandatasetSchema20.md) |  | 

## Example

```python
from urbandatasetgateway_client.models.last_request200_response import LastRequest200Response

# TODO update the JSON string below
json = "{}"
# create an instance of LastRequest200Response from a JSON string
last_request200_response_instance = LastRequest200Response.from_json(json)
# print the JSON string representation of the object
print(LastRequest200Response.to_json())

# convert the object into a dict
last_request200_response_dict = last_request200_response_instance.to_dict()
# create an instance of LastRequest200Response from a dict
last_request200_response_from_dict = LastRequest200Response.from_dict(last_request200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


