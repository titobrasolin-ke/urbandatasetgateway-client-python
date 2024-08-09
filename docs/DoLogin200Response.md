# DoLogin200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**message** | **str** |  | 
**token** | **str** |  | 

## Example

```python
from urbandatasetgateway_client.models.do_login200_response import DoLogin200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DoLogin200Response from a JSON string
do_login200_response_instance = DoLogin200Response.from_json(json)
# print the JSON string representation of the object
print(DoLogin200Response.to_json())

# convert the object into a dict
do_login200_response_dict = do_login200_response_instance.to_dict()
# create an instance of DoLogin200Response from a dict
do_login200_response_from_dict = DoLogin200Response.from_dict(do_login200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


