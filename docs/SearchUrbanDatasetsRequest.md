# SearchUrbanDatasetsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | Uniquely identifies an UrbanDataset produced by a specific Solution producer (syntax defined in the SCPS Collaboration 2.0) | 
**period_start** | **str** | Date and time from which you want to specify the start of a time interval. | [optional] 
**period_end** | **str** | Date and time from which you want to specify the end of a time interval. | [optional] 
**center_latitude** | **str** | Latitude of the center where space research will be carried out. | [optional] 
**center_longitude** | **str** | Longitude of the center on which space research will be carried out. | [optional] 
**distance** | **str** | Radius of the circle, in meters, on which space research will be carried out. | [optional] 

## Example

```python
from urbandatasetgateway_client.models.search_urban_datasets_request import SearchUrbanDatasetsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SearchUrbanDatasetsRequest from a JSON string
search_urban_datasets_request_instance = SearchUrbanDatasetsRequest.from_json(json)
# print the JSON string representation of the object
print(SearchUrbanDatasetsRequest.to_json())

# convert the object into a dict
search_urban_datasets_request_dict = search_urban_datasets_request_instance.to_dict()
# create an instance of SearchUrbanDatasetsRequest from a dict
search_urban_datasets_request_from_dict = SearchUrbanDatasetsRequest.from_dict(search_urban_datasets_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


