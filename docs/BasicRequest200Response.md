# BasicRequest200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**message** | **str** |  | 
**dataset** | [**List[ScpsUrbandatasetSchema20]**](ScpsUrbandatasetSchema20.md) | An array of one or more UrbanDatasets, according to the SCPS Information 2.0 specification. | 

## Example

```python
from urbandatasetgateway_client.models.basic_request200_response import BasicRequest200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BasicRequest200Response from a JSON string
basic_request200_response_instance = BasicRequest200Response.from_json(json)
# print the JSON string representation of the object
print(BasicRequest200Response.to_json())

# convert the object into a dict
basic_request200_response_dict = basic_request200_response_instance.to_dict()
# create an instance of BasicRequest200Response from a dict
basic_request200_response_from_dict = BasicRequest200Response.from_dict(basic_request200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


