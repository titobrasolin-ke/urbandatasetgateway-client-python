# DoLoginRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from urbandatasetgateway_client.models.do_login_request import DoLoginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DoLoginRequest from a JSON string
do_login_request_instance = DoLoginRequest.from_json(json)
# print the JSON string representation of the object
print(DoLoginRequest.to_json())

# convert the object into a dict
do_login_request_dict = do_login_request_instance.to_dict()
# create an instance of DoLoginRequest from a dict
do_login_request_from_dict = DoLoginRequest.from_dict(do_login_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


