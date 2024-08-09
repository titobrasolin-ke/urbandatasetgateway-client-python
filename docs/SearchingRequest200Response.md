# SearchingRequest200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**message** | **str** |  | 
**dataset** | [**List[ScpsUrbandatasetSchema20]**](ScpsUrbandatasetSchema20.md) | An array of one or more UrbanDatasets, according to the SCPS Information 2.0 specification. | 

## Example

```python
from urbandatasetgateway_client.models.searching_request200_response import SearchingRequest200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SearchingRequest200Response from a JSON string
searching_request200_response_instance = SearchingRequest200Response.from_json(json)
# print the JSON string representation of the object
print(SearchingRequest200Response.to_json())

# convert the object into a dict
searching_request200_response_dict = searching_request200_response_instance.to_dict()
# create an instance of SearchingRequest200Response from a dict
searching_request200_response_from_dict = SearchingRequest200Response.from_dict(searching_request200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


