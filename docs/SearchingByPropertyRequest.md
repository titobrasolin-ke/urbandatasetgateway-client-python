# SearchingByPropertyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | Uniquely identifies an UrbanDataset produced by a specific Solution producer (syntax defined in the SCPS Collaboration 2.0) | 
**property_name** | **str** | Name of the property being searched | 
**property_value** | **str** | Value of the property being searched | 
**period_start** | **str** | Date and time from which you want to specify the start of a time interval. | [optional] 
**period_end** | **str** | Date and time from which you want to specify the end of a time interval. | [optional] 
**center_latitude** | **str** | Latitude of the center where space research will be carried out. | [optional] 
**center_longitude** | **str** | Longitude of the center on which space research will be carried out. | [optional] 
**distance** | **str** | Radius of the circle, in meters, on which space research will be carried out. | [optional] 

## Example

```python
from urbandatasetgateway_client.models.searching_by_property_request import SearchingByPropertyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SearchingByPropertyRequest from a JSON string
searching_by_property_request_instance = SearchingByPropertyRequest.from_json(json)
# print the JSON string representation of the object
print(SearchingByPropertyRequest.to_json())

# convert the object into a dict
searching_by_property_request_dict = searching_by_property_request_instance.to_dict()
# create an instance of SearchingByPropertyRequest from a dict
searching_by_property_request_from_dict = SearchingByPropertyRequest.from_dict(searching_by_property_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


