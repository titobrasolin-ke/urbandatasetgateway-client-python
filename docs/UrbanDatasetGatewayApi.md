# urbandatasetgateway_client.UrbanDatasetGatewayApi

All URIs are relative to *https://kerberos-lab.it/webservices/rest/index.php/UrbanDatasetGateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**last_request**](UrbanDatasetGatewayApi.md#last_request) | **POST** /lastRequest | lastRequest REST method
[**login**](UrbanDatasetGatewayApi.md#login) | **POST** /login | login REST method
[**push**](UrbanDatasetGatewayApi.md#push) | **POST** /push | push REST method
[**searching_request**](UrbanDatasetGatewayApi.md#searching_request) | **POST** /searchingRequest | searchingRequest REST method
[**test**](UrbanDatasetGatewayApi.md#test) | **GET** /test | test REST method


# **last_request**
> LastRequest200Response last_request(last_request_request)

lastRequest REST method

The \"lastRequest\" method allows you to request the last UrbanDataset generated through a REQUEST / RESPONSE call.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import urbandatasetgateway_client
from urbandatasetgateway_client.models.last_request200_response import LastRequest200Response
from urbandatasetgateway_client.models.last_request_request import LastRequestRequest
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
    last_request_request = {"resource_id":"SCP-1_SmartBuildingCasaccia-3_SmartBuildingAnomalies-1.0_20180125120000"} # LastRequestRequest | 

    try:
        # lastRequest REST method
        api_response = api_instance.last_request(last_request_request)
        print("The response of UrbanDatasetGatewayApi->last_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UrbanDatasetGatewayApi->last_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last_request_request** | [**LastRequestRequest**](LastRequestRequest.md)|  | 

### Return type

[**LastRequest200Response**](LastRequest200Response.md)

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

# **login**
> Login200Response login(login_request)

login REST method

The \"login\" method allows a client to authenticate itself to the service, by using username and password and receiving a JWT (JSON Web Token) in string format which will use in the subsequent calls.

### Example


```python
import urbandatasetgateway_client
from urbandatasetgateway_client.models.login200_response import Login200Response
from urbandatasetgateway_client.models.login_request import LoginRequest
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
    login_request = {"username":"myusername","password":"mypassword"} # LoginRequest | 

    try:
        # login REST method
        api_response = api_instance.login(login_request)
        print("The response of UrbanDatasetGatewayApi->login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UrbanDatasetGatewayApi->login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_request** | [**LoginRequest**](LoginRequest.md)|  | 

### Return type

[**Login200Response**](Login200Response.md)

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

# **push**
> Push200Response push(push_request)

push REST method

The \"push\" method allows a client to send an UrbanDataset through a single PUSH call.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import urbandatasetgateway_client
from urbandatasetgateway_client.models.push200_response import Push200Response
from urbandatasetgateway_client.models.push_request import PushRequest
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
    push_request = urbandatasetgateway_client.PushRequest() # PushRequest | 

    try:
        # push REST method
        api_response = api_instance.push(push_request)
        print("The response of UrbanDatasetGatewayApi->push:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UrbanDatasetGatewayApi->push: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **push_request** | [**PushRequest**](PushRequest.md)|  | 

### Return type

[**Push200Response**](Push200Response.md)

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

# **searching_request**
> SearchingRequest200Response searching_request(searching_request_request)

searchingRequest REST method

The \"searchingRequest\" method allows a client to request one or more UrbanDatasets through a REQUEST/RESPONSE call, providing the identifier of the resource, with search filters like geographical coordinates and period at the context level (contextualization element in the UrbanDataset format).  With all optional parameters set to null, it achieves the same result as a basicRequest.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import urbandatasetgateway_client
from urbandatasetgateway_client.models.searching_request200_response import SearchingRequest200Response
from urbandatasetgateway_client.models.searching_request_request import SearchingRequestRequest
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
    searching_request_request = {"resource_id":"SCP-1_SmartBuildingCasaccia-3_SmartBuildingAnomalies-1.0_20180125120000"} # SearchingRequestRequest | 

    try:
        # searchingRequest REST method
        api_response = api_instance.searching_request(searching_request_request)
        print("The response of UrbanDatasetGatewayApi->searching_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UrbanDatasetGatewayApi->searching_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **searching_request_request** | [**SearchingRequestRequest**](SearchingRequestRequest.md)|  | 

### Return type

[**SearchingRequest200Response**](SearchingRequest200Response.md)

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

# **test**
> Test200Response test()

test REST method

The \"test\" method allows a client to test the online presence of the RESTful web service. It is the only web service method that can be retrieved either with a GET and with a POST.

### Example


```python
import urbandatasetgateway_client
from urbandatasetgateway_client.models.test200_response import Test200Response
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
        api_response = api_instance.test()
        print("The response of UrbanDatasetGatewayApi->test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UrbanDatasetGatewayApi->test: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Test200Response**](Test200Response.md)

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

