# urbandatasetgateway_client.UrbanDatasetGatewayApi

All URIs are relative to *https://scp-casaccia.bologna.enea.it:8443/webservices/rest/UrbanDatasetGateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**basic**](UrbanDatasetGatewayApi.md#basic) | **POST** /basicRequest | Request an UrbanDataset, through the REQUEST / RESPONSE call, providing the identifier of the resource
[**deep_searching**](UrbanDatasetGatewayApi.md#deep_searching) | **POST** /deepSearchingRequest | Request an UrbanDataset through a REQUEST / RESPONSE call, providing the identifier of the resource, with a spatial-temporal refinement of the search at line level (elements of specification of the dataset value records, present in the format); with all optional parameters set to null, it achieves the same result as a basic Request
[**delete**](UrbanDatasetGatewayApi.md#delete) | **POST** /delete | Delete a particular UrbanDataset, providing the resource identifier and the specific generation timestamp
[**is_alive**](UrbanDatasetGatewayApi.md#is_alive) | **POST** /isAlive | Verify that the token is still valid
[**last**](UrbanDatasetGatewayApi.md#last) | **POST** /lastRequest | Request the last UrbanDataset generated through a REQUEST / RESPONSE call
[**login**](UrbanDatasetGatewayApi.md#login) | **POST** /login | Authenticate with the service that exposes this method through username and password, receiving in response a token that will use in subsequent calls
[**logout**](UrbanDatasetGatewayApi.md#logout) | **POST** /logout | Cancel authentication at the service that exposes this method making the token received in the previous login call invalid
[**push**](UrbanDatasetGatewayApi.md#push) | **POST** /push | Send an UrbanDataset via the PUSH call
[**searching**](UrbanDatasetGatewayApi.md#searching) | **POST** /searchingRequest | Request an UrbanDataset through a REQUEST / RESPONSE call, providing the identifier of the resource, with a spatial-temporal refinement of the search at the context level (UrbanDataset contextualization element present in the format); with all optional parameters set to null, it achieves the same result as a basic Request
[**searching_by_property**](UrbanDatasetGatewayApi.md#searching_by_property) | **POST** /searchingByPropertyRequest | Request an UrbanDataset through a REQUEST / RESPONSE call, providing the identifier of the resource, with a spatial-temporal refinement of the search at the context level (UrbanDataset contextualization element present in the format); searching among the UD properties that one is matching with the input property
[**specific**](UrbanDatasetGatewayApi.md#specific) | **POST** /specificRequest | Request a particular UrbanDataset, through a REQUEST / RESPONSE call, providing the identifier of the resource and the specific generation timestamp
[**test**](UrbanDatasetGatewayApi.md#test) | **POST** /test | Test the presence of the web service
[**test_get**](UrbanDatasetGatewayApi.md#test_get) | **GET** /test | Test the presence of the web service


# **basic**
> Basic200Response basic(basic_request=basic_request)

Request an UrbanDataset, through the REQUEST / RESPONSE call, providing the identifier of the resource



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import urbandatasetgateway_client
from urbandatasetgateway_client.models.basic200_response import Basic200Response
from urbandatasetgateway_client.models.basic_request import BasicRequest
from urbandatasetgateway_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://scp-casaccia.bologna.enea.it:8443/webservices/rest/UrbanDatasetGateway
# See configuration.py for a list of all supported configuration parameters.
configuration = urbandatasetgateway_client.Configuration(
    host = "https://scp-casaccia.bologna.enea.it:8443/webservices/rest/UrbanDatasetGateway"
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
    basic_request = urbandatasetgateway_client.BasicRequest() # BasicRequest |  (optional)

    try:
        # Request an UrbanDataset, through the REQUEST / RESPONSE call, providing the identifier of the resource
        api_response = api_instance.basic(basic_request=basic_request)
        print("The response of UrbanDatasetGatewayApi->basic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UrbanDatasetGatewayApi->basic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **basic_request** | [**BasicRequest**](BasicRequest.md)|  | [optional] 

### Return type

[**Basic200Response**](Basic200Response.md)

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

# **deep_searching**
> Basic200Response deep_searching(deep_searching_request=deep_searching_request)

Request an UrbanDataset through a REQUEST / RESPONSE call, providing the identifier of the resource, with a spatial-temporal refinement of the search at line level (elements of specification of the dataset value records, present in the format); with all optional parameters set to null, it achieves the same result as a basic Request



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import urbandatasetgateway_client
from urbandatasetgateway_client.models.basic200_response import Basic200Response
from urbandatasetgateway_client.models.deep_searching_request import DeepSearchingRequest
from urbandatasetgateway_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://scp-casaccia.bologna.enea.it:8443/webservices/rest/UrbanDatasetGateway
# See configuration.py for a list of all supported configuration parameters.
configuration = urbandatasetgateway_client.Configuration(
    host = "https://scp-casaccia.bologna.enea.it:8443/webservices/rest/UrbanDatasetGateway"
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
    deep_searching_request = urbandatasetgateway_client.DeepSearchingRequest() # DeepSearchingRequest |  (optional)

    try:
        # Request an UrbanDataset through a REQUEST / RESPONSE call, providing the identifier of the resource, with a spatial-temporal refinement of the search at line level (elements of specification of the dataset value records, present in the format); with all optional parameters set to null, it achieves the same result as a basic Request
        api_response = api_instance.deep_searching(deep_searching_request=deep_searching_request)
        print("The response of UrbanDatasetGatewayApi->deep_searching:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UrbanDatasetGatewayApi->deep_searching: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deep_searching_request** | [**DeepSearchingRequest**](DeepSearchingRequest.md)|  | [optional] 

### Return type

[**Basic200Response**](Basic200Response.md)

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

# **delete**
> TestGet200Response delete(specific_request=specific_request)

Delete a particular UrbanDataset, providing the resource identifier and the specific generation timestamp



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import urbandatasetgateway_client
from urbandatasetgateway_client.models.specific_request import SpecificRequest
from urbandatasetgateway_client.models.test_get200_response import TestGet200Response
from urbandatasetgateway_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://scp-casaccia.bologna.enea.it:8443/webservices/rest/UrbanDatasetGateway
# See configuration.py for a list of all supported configuration parameters.
configuration = urbandatasetgateway_client.Configuration(
    host = "https://scp-casaccia.bologna.enea.it:8443/webservices/rest/UrbanDatasetGateway"
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
    specific_request = urbandatasetgateway_client.SpecificRequest() # SpecificRequest |  (optional)

    try:
        # Delete a particular UrbanDataset, providing the resource identifier and the specific generation timestamp
        api_response = api_instance.delete(specific_request=specific_request)
        print("The response of UrbanDatasetGatewayApi->delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UrbanDatasetGatewayApi->delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specific_request** | [**SpecificRequest**](SpecificRequest.md)|  | [optional] 

### Return type

[**TestGet200Response**](TestGet200Response.md)

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

# **is_alive**
> IsAlive200Response is_alive(body=body)

Verify that the token is still valid



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import urbandatasetgateway_client
from urbandatasetgateway_client.models.is_alive200_response import IsAlive200Response
from urbandatasetgateway_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://scp-casaccia.bologna.enea.it:8443/webservices/rest/UrbanDatasetGateway
# See configuration.py for a list of all supported configuration parameters.
configuration = urbandatasetgateway_client.Configuration(
    host = "https://scp-casaccia.bologna.enea.it:8443/webservices/rest/UrbanDatasetGateway"
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
    body = 'body_example' # str |  (optional)

    try:
        # Verify that the token is still valid
        api_response = api_instance.is_alive(body=body)
        print("The response of UrbanDatasetGatewayApi->is_alive:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UrbanDatasetGatewayApi->is_alive: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | [optional] 

### Return type

[**IsAlive200Response**](IsAlive200Response.md)

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

# **last**
> Last200Response last(last_request)

Request the last UrbanDataset generated through a REQUEST / RESPONSE call



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import urbandatasetgateway_client
from urbandatasetgateway_client.models.last200_response import Last200Response
from urbandatasetgateway_client.models.last_request import LastRequest
from urbandatasetgateway_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://scp-casaccia.bologna.enea.it:8443/webservices/rest/UrbanDatasetGateway
# See configuration.py for a list of all supported configuration parameters.
configuration = urbandatasetgateway_client.Configuration(
    host = "https://scp-casaccia.bologna.enea.it:8443/webservices/rest/UrbanDatasetGateway"
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
    last_request = {"resource_id":"SCP-1_SmartBuildingCasaccia-3_SmartBuildingAnomalies-1.0_20180125120000"} # LastRequest | 

    try:
        # Request the last UrbanDataset generated through a REQUEST / RESPONSE call
        api_response = api_instance.last(last_request)
        print("The response of UrbanDatasetGatewayApi->last:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UrbanDatasetGatewayApi->last: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last_request** | [**LastRequest**](LastRequest.md)|  | 

### Return type

[**Last200Response**](Last200Response.md)

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

Authenticate with the service that exposes this method through username and password, receiving in response a token that will use in subsequent calls



### Example


```python
import urbandatasetgateway_client
from urbandatasetgateway_client.models.login200_response import Login200Response
from urbandatasetgateway_client.models.login_request import LoginRequest
from urbandatasetgateway_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://scp-casaccia.bologna.enea.it:8443/webservices/rest/UrbanDatasetGateway
# See configuration.py for a list of all supported configuration parameters.
configuration = urbandatasetgateway_client.Configuration(
    host = "https://scp-casaccia.bologna.enea.it:8443/webservices/rest/UrbanDatasetGateway"
)


# Enter a context with an instance of the API client
with urbandatasetgateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = urbandatasetgateway_client.UrbanDatasetGatewayApi(api_client)
    login_request = urbandatasetgateway_client.LoginRequest() # LoginRequest | 

    try:
        # Authenticate with the service that exposes this method through username and password, receiving in response a token that will use in subsequent calls
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

# **logout**
> TestGet200Response logout(body=body)

Cancel authentication at the service that exposes this method making the token received in the previous login call invalid



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import urbandatasetgateway_client
from urbandatasetgateway_client.models.test_get200_response import TestGet200Response
from urbandatasetgateway_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://scp-casaccia.bologna.enea.it:8443/webservices/rest/UrbanDatasetGateway
# See configuration.py for a list of all supported configuration parameters.
configuration = urbandatasetgateway_client.Configuration(
    host = "https://scp-casaccia.bologna.enea.it:8443/webservices/rest/UrbanDatasetGateway"
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
    body = 'body_example' # str |  (optional)

    try:
        # Cancel authentication at the service that exposes this method making the token received in the previous login call invalid
        api_response = api_instance.logout(body=body)
        print("The response of UrbanDatasetGatewayApi->logout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UrbanDatasetGatewayApi->logout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | [optional] 

### Return type

[**TestGet200Response**](TestGet200Response.md)

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

# **push**
> Push200Response push(push_request)

Send an UrbanDataset via the PUSH call



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import urbandatasetgateway_client
from urbandatasetgateway_client.models.push200_response import Push200Response
from urbandatasetgateway_client.models.push_request import PushRequest
from urbandatasetgateway_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://scp-casaccia.bologna.enea.it:8443/webservices/rest/UrbanDatasetGateway
# See configuration.py for a list of all supported configuration parameters.
configuration = urbandatasetgateway_client.Configuration(
    host = "https://scp-casaccia.bologna.enea.it:8443/webservices/rest/UrbanDatasetGateway"
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
        # Send an UrbanDataset via the PUSH call
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
**200** | The fields [CODE], [MSG] and [DETAIL] take specific values depending on the type of error/detail found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searching**
> Basic200Response searching(searching_request)

Request an UrbanDataset through a REQUEST / RESPONSE call, providing the identifier of the resource, with a spatial-temporal refinement of the search at the context level (UrbanDataset contextualization element present in the format); with all optional parameters set to null, it achieves the same result as a basic Request



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import urbandatasetgateway_client
from urbandatasetgateway_client.models.basic200_response import Basic200Response
from urbandatasetgateway_client.models.searching_request import SearchingRequest
from urbandatasetgateway_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://scp-casaccia.bologna.enea.it:8443/webservices/rest/UrbanDatasetGateway
# See configuration.py for a list of all supported configuration parameters.
configuration = urbandatasetgateway_client.Configuration(
    host = "https://scp-casaccia.bologna.enea.it:8443/webservices/rest/UrbanDatasetGateway"
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
    searching_request = {"resource_id":"SCP-1_SmartBuildingCasaccia-3_SmartBuildingAnomalies-1.0_20180125120000"} # SearchingRequest | 

    try:
        # Request an UrbanDataset through a REQUEST / RESPONSE call, providing the identifier of the resource, with a spatial-temporal refinement of the search at the context level (UrbanDataset contextualization element present in the format); with all optional parameters set to null, it achieves the same result as a basic Request
        api_response = api_instance.searching(searching_request)
        print("The response of UrbanDatasetGatewayApi->searching:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UrbanDatasetGatewayApi->searching: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **searching_request** | [**SearchingRequest**](SearchingRequest.md)|  | 

### Return type

[**Basic200Response**](Basic200Response.md)

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

# **searching_by_property**
> Basic200Response searching_by_property(searching_by_property_request=searching_by_property_request)

Request an UrbanDataset through a REQUEST / RESPONSE call, providing the identifier of the resource, with a spatial-temporal refinement of the search at the context level (UrbanDataset contextualization element present in the format); searching among the UD properties that one is matching with the input property



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import urbandatasetgateway_client
from urbandatasetgateway_client.models.basic200_response import Basic200Response
from urbandatasetgateway_client.models.searching_by_property_request import SearchingByPropertyRequest
from urbandatasetgateway_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://scp-casaccia.bologna.enea.it:8443/webservices/rest/UrbanDatasetGateway
# See configuration.py for a list of all supported configuration parameters.
configuration = urbandatasetgateway_client.Configuration(
    host = "https://scp-casaccia.bologna.enea.it:8443/webservices/rest/UrbanDatasetGateway"
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
    searching_by_property_request = urbandatasetgateway_client.SearchingByPropertyRequest() # SearchingByPropertyRequest |  (optional)

    try:
        # Request an UrbanDataset through a REQUEST / RESPONSE call, providing the identifier of the resource, with a spatial-temporal refinement of the search at the context level (UrbanDataset contextualization element present in the format); searching among the UD properties that one is matching with the input property
        api_response = api_instance.searching_by_property(searching_by_property_request=searching_by_property_request)
        print("The response of UrbanDatasetGatewayApi->searching_by_property:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UrbanDatasetGatewayApi->searching_by_property: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **searching_by_property_request** | [**SearchingByPropertyRequest**](SearchingByPropertyRequest.md)|  | [optional] 

### Return type

[**Basic200Response**](Basic200Response.md)

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

# **specific**
> Last200Response specific(specific_request=specific_request)

Request a particular UrbanDataset, through a REQUEST / RESPONSE call, providing the identifier of the resource and the specific generation timestamp



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import urbandatasetgateway_client
from urbandatasetgateway_client.models.last200_response import Last200Response
from urbandatasetgateway_client.models.specific_request import SpecificRequest
from urbandatasetgateway_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://scp-casaccia.bologna.enea.it:8443/webservices/rest/UrbanDatasetGateway
# See configuration.py for a list of all supported configuration parameters.
configuration = urbandatasetgateway_client.Configuration(
    host = "https://scp-casaccia.bologna.enea.it:8443/webservices/rest/UrbanDatasetGateway"
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
    specific_request = urbandatasetgateway_client.SpecificRequest() # SpecificRequest |  (optional)

    try:
        # Request a particular UrbanDataset, through a REQUEST / RESPONSE call, providing the identifier of the resource and the specific generation timestamp
        api_response = api_instance.specific(specific_request=specific_request)
        print("The response of UrbanDatasetGatewayApi->specific:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UrbanDatasetGatewayApi->specific: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specific_request** | [**SpecificRequest**](SpecificRequest.md)|  | [optional] 

### Return type

[**Last200Response**](Last200Response.md)

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
> TestGet200Response test(body=body)

Test the presence of the web service



### Example


```python
import urbandatasetgateway_client
from urbandatasetgateway_client.models.test_get200_response import TestGet200Response
from urbandatasetgateway_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://scp-casaccia.bologna.enea.it:8443/webservices/rest/UrbanDatasetGateway
# See configuration.py for a list of all supported configuration parameters.
configuration = urbandatasetgateway_client.Configuration(
    host = "https://scp-casaccia.bologna.enea.it:8443/webservices/rest/UrbanDatasetGateway"
)


# Enter a context with an instance of the API client
with urbandatasetgateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = urbandatasetgateway_client.UrbanDatasetGatewayApi(api_client)
    body = 'body_example' # str |  (optional)

    try:
        # Test the presence of the web service
        api_response = api_instance.test(body=body)
        print("The response of UrbanDatasetGatewayApi->test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UrbanDatasetGatewayApi->test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | [optional] 

### Return type

[**TestGet200Response**](TestGet200Response.md)

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

# **test_get**
> TestGet200Response test_get()

Test the presence of the web service



### Example


```python
import urbandatasetgateway_client
from urbandatasetgateway_client.models.test_get200_response import TestGet200Response
from urbandatasetgateway_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://scp-casaccia.bologna.enea.it:8443/webservices/rest/UrbanDatasetGateway
# See configuration.py for a list of all supported configuration parameters.
configuration = urbandatasetgateway_client.Configuration(
    host = "https://scp-casaccia.bologna.enea.it:8443/webservices/rest/UrbanDatasetGateway"
)


# Enter a context with an instance of the API client
with urbandatasetgateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = urbandatasetgateway_client.UrbanDatasetGatewayApi(api_client)

    try:
        # Test the presence of the web service
        api_response = api_instance.test_get()
        print("The response of UrbanDatasetGatewayApi->test_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UrbanDatasetGatewayApi->test_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TestGet200Response**](TestGet200Response.md)

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

