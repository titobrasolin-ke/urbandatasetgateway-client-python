# urbandatasetgateway_client.UrbanDatasetGatewayApi

All URIs are relative to *https://kerberos-lab.it/webservices/rest/index.php/UrbanDatasetGateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**do_login**](UrbanDatasetGatewayApi.md#do_login) | **POST** /login | login REST method
[**do_test**](UrbanDatasetGatewayApi.md#do_test) | **GET** /test | test REST method
[**push_urban_dataset**](UrbanDatasetGatewayApi.md#push_urban_dataset) | **POST** /push | push REST method
[**request_last_urban_dataset**](UrbanDatasetGatewayApi.md#request_last_urban_dataset) | **POST** /lastRequest | lastRequest REST method
[**search_urban_datasets**](UrbanDatasetGatewayApi.md#search_urban_datasets) | **POST** /searchingRequest | searchingRequest REST method


# **do_login**
> DoLogin200Response do_login(do_login_request=do_login_request)

login REST method

The \"login\" method allows a client to authenticate itself to the service, by using username and password and receiving a JWT (JSON Web Token) in string format which will use in the subsequent calls.

### Example


```python
import urbandatasetgateway_client
from urbandatasetgateway_client.models.do_login200_response import DoLogin200Response
from urbandatasetgateway_client.models.do_login_request import DoLoginRequest
from urbandatasetgateway_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://kerberos-lab.it/webservices/rest/index.php/UrbanDatasetGateway
# See configuration.py for a list of all supported configuration parameters.
configuration = urbandatasetgateway_client.Configuration(
    host = "https://kerberos-lab.it/webservices/rest/index.php/UrbanDatasetGateway"
)


# Enter a context with an instance of the API client
with urbandatasetgateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = urbandatasetgateway_client.UrbanDatasetGatewayApi(api_client)
    do_login_request = {"username":"myusername","password":"mypassword"} # DoLoginRequest |  (optional)

    try:
        # login REST method
        api_response = api_instance.do_login(do_login_request=do_login_request)
        print("The response of UrbanDatasetGatewayApi->do_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UrbanDatasetGatewayApi->do_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **do_login_request** | [**DoLoginRequest**](DoLoginRequest.md)|  | [optional] 

### Return type

[**DoLogin200Response**](DoLogin200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **do_test**
> DoTest200Response do_test()

test REST method

The \"test\" method allows a client to test the online presence of the RESTful web service. It is the only web service method that can be retrieved either with a GET and with a POST.

### Example


```python
import urbandatasetgateway_client
from urbandatasetgateway_client.models.do_test200_response import DoTest200Response
from urbandatasetgateway_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://kerberos-lab.it/webservices/rest/index.php/UrbanDatasetGateway
# See configuration.py for a list of all supported configuration parameters.
configuration = urbandatasetgateway_client.Configuration(
    host = "https://kerberos-lab.it/webservices/rest/index.php/UrbanDatasetGateway"
)


# Enter a context with an instance of the API client
with urbandatasetgateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = urbandatasetgateway_client.UrbanDatasetGatewayApi(api_client)

    try:
        # test REST method
        api_response = api_instance.do_test()
        print("The response of UrbanDatasetGatewayApi->do_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UrbanDatasetGatewayApi->do_test: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DoTest200Response**](DoTest200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **push_urban_dataset**
> PushUrbanDataset200Response push_urban_dataset(push_urban_dataset_request=push_urban_dataset_request)

push REST method

The \"push\" method allows a client to send an UrbanDataset through a single PUSH call.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import urbandatasetgateway_client
from urbandatasetgateway_client.models.push_urban_dataset200_response import PushUrbanDataset200Response
from urbandatasetgateway_client.models.push_urban_dataset_request import PushUrbanDatasetRequest
from urbandatasetgateway_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://kerberos-lab.it/webservices/rest/index.php/UrbanDatasetGateway
# See configuration.py for a list of all supported configuration parameters.
configuration = urbandatasetgateway_client.Configuration(
    host = "https://kerberos-lab.it/webservices/rest/index.php/UrbanDatasetGateway"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = urbandatasetgateway_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with urbandatasetgateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = urbandatasetgateway_client.UrbanDatasetGatewayApi(api_client)
    push_urban_dataset_request = urbandatasetgateway_client.PushUrbanDatasetRequest() # PushUrbanDatasetRequest |  (optional)

    try:
        # push REST method
        api_response = api_instance.push_urban_dataset(push_urban_dataset_request=push_urban_dataset_request)
        print("The response of UrbanDatasetGatewayApi->push_urban_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UrbanDatasetGatewayApi->push_urban_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **push_urban_dataset_request** | [**PushUrbanDatasetRequest**](PushUrbanDatasetRequest.md)|  | [optional] 

### Return type

[**PushUrbanDataset200Response**](PushUrbanDataset200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The fields [CODE] , [MSG] and [DETAIL] take specific values depending on the type of error/detail found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_last_urban_dataset**
> RequestLastUrbanDataset200Response request_last_urban_dataset(request_last_urban_dataset_request=request_last_urban_dataset_request)

lastRequest REST method

The \"lastRequest\" method allows you to request the last UrbanDataset generated through a REQUEST / RESPONSE call.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import urbandatasetgateway_client
from urbandatasetgateway_client.models.request_last_urban_dataset200_response import RequestLastUrbanDataset200Response
from urbandatasetgateway_client.models.request_last_urban_dataset_request import RequestLastUrbanDatasetRequest
from urbandatasetgateway_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://kerberos-lab.it/webservices/rest/index.php/UrbanDatasetGateway
# See configuration.py for a list of all supported configuration parameters.
configuration = urbandatasetgateway_client.Configuration(
    host = "https://kerberos-lab.it/webservices/rest/index.php/UrbanDatasetGateway"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = urbandatasetgateway_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with urbandatasetgateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = urbandatasetgateway_client.UrbanDatasetGatewayApi(api_client)
    request_last_urban_dataset_request = {"resource_id":"SCP-1_SmartBuildingCasaccia-3_SmartBuildingAnomalies-1.0_20180125120000"} # RequestLastUrbanDatasetRequest |  (optional)

    try:
        # lastRequest REST method
        api_response = api_instance.request_last_urban_dataset(request_last_urban_dataset_request=request_last_urban_dataset_request)
        print("The response of UrbanDatasetGatewayApi->request_last_urban_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UrbanDatasetGatewayApi->request_last_urban_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_last_urban_dataset_request** | [**RequestLastUrbanDatasetRequest**](RequestLastUrbanDatasetRequest.md)|  | [optional] 

### Return type

[**RequestLastUrbanDataset200Response**](RequestLastUrbanDataset200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_urban_datasets**
> SearchUrbanDatasets200Response search_urban_datasets(search_urban_datasets_request=search_urban_datasets_request)

searchingRequest REST method

The \"searchingRequest\" method allows a client to request one or more UrbanDatasets through a REQUEST/RESPONSE call, providing the identifier of the resource, with search filters like geographical coordinates and period at the context level (contextualization element in the UrbanDataset format).  With all optional parameters set to null, it achieves the same result as a basicRequest.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import urbandatasetgateway_client
from urbandatasetgateway_client.models.search_urban_datasets200_response import SearchUrbanDatasets200Response
from urbandatasetgateway_client.models.search_urban_datasets_request import SearchUrbanDatasetsRequest
from urbandatasetgateway_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://kerberos-lab.it/webservices/rest/index.php/UrbanDatasetGateway
# See configuration.py for a list of all supported configuration parameters.
configuration = urbandatasetgateway_client.Configuration(
    host = "https://kerberos-lab.it/webservices/rest/index.php/UrbanDatasetGateway"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = urbandatasetgateway_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with urbandatasetgateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = urbandatasetgateway_client.UrbanDatasetGatewayApi(api_client)
    search_urban_datasets_request = {"resource_id":"SCP-1_SmartBuildingCasaccia-3_SmartBuildingAnomalies-1.0_20180125120000"} # SearchUrbanDatasetsRequest |  (optional)

    try:
        # searchingRequest REST method
        api_response = api_instance.search_urban_datasets(search_urban_datasets_request=search_urban_datasets_request)
        print("The response of UrbanDatasetGatewayApi->search_urban_datasets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UrbanDatasetGatewayApi->search_urban_datasets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_urban_datasets_request** | [**SearchUrbanDatasetsRequest**](SearchUrbanDatasetsRequest.md)|  | [optional] 

### Return type

[**SearchUrbanDatasets200Response**](SearchUrbanDatasets200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

