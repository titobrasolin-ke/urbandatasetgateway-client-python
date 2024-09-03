# Last200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**message** | **str** |  | 
**dataset** | [**ScpsUrbandatasetSchema20**](ScpsUrbandatasetSchema20.md) |  | 

## Example

```python
from urbandatasetgateway_client.models.last200_response import Last200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Last200Response from a JSON string
last200_response_instance = Last200Response.from_json(json)
# print the JSON string representation of the object
print(Last200Response.to_json())

# convert the object into a dict
last200_response_dict = last200_response_instance.to_dict()
# create an instance of Last200Response from a dict
last200_response_from_dict = Last200Response.from_dict(last200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


