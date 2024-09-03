# SpecificRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** |  | 
**timestamp** | **datetime** |  | 

## Example

```python
from urbandatasetgateway_client.models.specific_request import SpecificRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SpecificRequest from a JSON string
specific_request_instance = SpecificRequest.from_json(json)
# print the JSON string representation of the object
print(SpecificRequest.to_json())

# convert the object into a dict
specific_request_dict = specific_request_instance.to_dict()
# create an instance of SpecificRequest from a dict
specific_request_from_dict = SpecificRequest.from_dict(specific_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


