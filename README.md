# urbandatasetgateway-client
**Smart City Platform Specification (SCPS) for Interoperability Layer**
[https://smartcityplatform.enea.it/#/en/specification/](https://smartcityplatform.enea.it/#/en/specification/)

**Smart City Platform Specification (SCPS) Communication 2.0**
[https://smartcityplatform.enea.it/#/en/specification/communication/2.0/](https://smartcityplatform.enea.it/#/en/specification/communication/2.0/)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.0.0
- Package version: 1.0.0
- Generator version: 7.7.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://kerberos.energy/en/kerberos/Home/Contactus](https://kerberos.energy/en/kerberos/Home/Contactus)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/titobrasolin-ke/urbandatasetgateway-client-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/titobrasolin-ke/urbandatasetgateway-client-python.git`)

Then import the package:
```python
import urbandatasetgateway_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import urbandatasetgateway_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import urbandatasetgateway_client
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
    except ApiException as e:
        print("Exception when calling UrbanDatasetGatewayApi->basic: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://scp-casaccia.bologna.enea.it:8443/webservices/rest/UrbanDatasetGateway*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*UrbanDatasetGatewayApi* | [**basic**](docs/UrbanDatasetGatewayApi.md#basic) | **POST** /basicRequest | Request an UrbanDataset, through the REQUEST / RESPONSE call, providing the identifier of the resource
*UrbanDatasetGatewayApi* | [**deep_searching**](docs/UrbanDatasetGatewayApi.md#deep_searching) | **POST** /deepSearchingRequest | Request an UrbanDataset through a REQUEST / RESPONSE call, providing the identifier of the resource, with a spatial-temporal refinement of the search at line level (elements of specification of the dataset value records, present in the format); with all optional parameters set to null, it achieves the same result as a basic Request
*UrbanDatasetGatewayApi* | [**delete**](docs/UrbanDatasetGatewayApi.md#delete) | **POST** /delete | Delete a particular UrbanDataset, providing the resource identifier and the specific generation timestamp
*UrbanDatasetGatewayApi* | [**is_alive**](docs/UrbanDatasetGatewayApi.md#is_alive) | **POST** /isAlive | Verify that the token is still valid
*UrbanDatasetGatewayApi* | [**last**](docs/UrbanDatasetGatewayApi.md#last) | **POST** /lastRequest | Request the last UrbanDataset generated through a REQUEST / RESPONSE call
*UrbanDatasetGatewayApi* | [**login**](docs/UrbanDatasetGatewayApi.md#login) | **POST** /login | Authenticate with the service that exposes this method through username and password, receiving in response a token that will use in subsequent calls
*UrbanDatasetGatewayApi* | [**logout**](docs/UrbanDatasetGatewayApi.md#logout) | **POST** /logout | Cancel authentication at the service that exposes this method making the token received in the previous login call invalid
*UrbanDatasetGatewayApi* | [**push**](docs/UrbanDatasetGatewayApi.md#push) | **POST** /push | Send an UrbanDataset via the PUSH call
*UrbanDatasetGatewayApi* | [**searching**](docs/UrbanDatasetGatewayApi.md#searching) | **POST** /searchingRequest | Request an UrbanDataset through a REQUEST / RESPONSE call, providing the identifier of the resource, with a spatial-temporal refinement of the search at the context level (UrbanDataset contextualization element present in the format); with all optional parameters set to null, it achieves the same result as a basic Request
*UrbanDatasetGatewayApi* | [**searching_by_property**](docs/UrbanDatasetGatewayApi.md#searching_by_property) | **POST** /searchingByPropertyRequest | Request an UrbanDataset through a REQUEST / RESPONSE call, providing the identifier of the resource, with a spatial-temporal refinement of the search at the context level (UrbanDataset contextualization element present in the format); searching among the UD properties that one is matching with the input property
*UrbanDatasetGatewayApi* | [**specific**](docs/UrbanDatasetGatewayApi.md#specific) | **POST** /specificRequest | Request a particular UrbanDataset, through a REQUEST / RESPONSE call, providing the identifier of the resource and the specific generation timestamp
*UrbanDatasetGatewayApi* | [**test**](docs/UrbanDatasetGatewayApi.md#test) | **POST** /test | Test the presence of the web service
*UrbanDatasetGatewayApi* | [**test_get**](docs/UrbanDatasetGatewayApi.md#test_get) | **GET** /test | Test the presence of the web service


## Documentation For Models

 - [Basic200Response](docs/Basic200Response.md)
 - [BasicRequest](docs/BasicRequest.md)
 - [DeepSearchingRequest](docs/DeepSearchingRequest.md)
 - [IsAlive200Response](docs/IsAlive200Response.md)
 - [Last200Response](docs/Last200Response.md)
 - [LastRequest](docs/LastRequest.md)
 - [Login200Response](docs/Login200Response.md)
 - [LoginRequest](docs/LoginRequest.md)
 - [Push200Response](docs/Push200Response.md)
 - [PushRequest](docs/PushRequest.md)
 - [ScpsUrbandatasetSchema20](docs/ScpsUrbandatasetSchema20.md)
 - [ScpsUrbandatasetSchema20UrbanDataset](docs/ScpsUrbandatasetSchema20UrbanDataset.md)
 - [ScpsUrbandatasetSchema20UrbanDatasetContext](docs/ScpsUrbandatasetSchema20UrbanDatasetContext.md)
 - [ScpsUrbandatasetSchema20UrbanDatasetContextCoordinates](docs/ScpsUrbandatasetSchema20UrbanDatasetContextCoordinates.md)
 - [ScpsUrbandatasetSchema20UrbanDatasetContextProducer](docs/ScpsUrbandatasetSchema20UrbanDatasetContextProducer.md)
 - [ScpsUrbandatasetSchema20UrbanDatasetSpecification](docs/ScpsUrbandatasetSchema20UrbanDatasetSpecification.md)
 - [ScpsUrbandatasetSchema20UrbanDatasetSpecificationId](docs/ScpsUrbandatasetSchema20UrbanDatasetSpecificationId.md)
 - [ScpsUrbandatasetSchema20UrbanDatasetSpecificationProperties](docs/ScpsUrbandatasetSchema20UrbanDatasetSpecificationProperties.md)
 - [ScpsUrbandatasetSchema20UrbanDatasetSpecificationPropertiesPropertyDefinitionInner](docs/ScpsUrbandatasetSchema20UrbanDatasetSpecificationPropertiesPropertyDefinitionInner.md)
 - [ScpsUrbandatasetSchema20UrbanDatasetSpecificationPropertiesPropertyDefinitionInnerNot](docs/ScpsUrbandatasetSchema20UrbanDatasetSpecificationPropertiesPropertyDefinitionInnerNot.md)
 - [ScpsUrbandatasetSchema20UrbanDatasetSpecificationPropertiesPropertyDefinitionInnerSubProperties](docs/ScpsUrbandatasetSchema20UrbanDatasetSpecificationPropertiesPropertyDefinitionInnerSubProperties.md)
 - [ScpsUrbandatasetSchema20UrbanDatasetValues](docs/ScpsUrbandatasetSchema20UrbanDatasetValues.md)
 - [ScpsUrbandatasetSchema20UrbanDatasetValuesLineInner](docs/ScpsUrbandatasetSchema20UrbanDatasetValuesLineInner.md)
 - [ScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPeriod](docs/ScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPeriod.md)
 - [ScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPropertyInner](docs/ScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPropertyInner.md)
 - [ScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPropertyInnerPropertyInner](docs/ScpsUrbandatasetSchema20UrbanDatasetValuesLineInnerPropertyInnerPropertyInner.md)
 - [SearchingByPropertyRequest](docs/SearchingByPropertyRequest.md)
 - [SearchingRequest](docs/SearchingRequest.md)
 - [SpecificRequest](docs/SpecificRequest.md)
 - [TestGet200Response](docs/TestGet200Response.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="bearerAuth"></a>
### bearerAuth

- **Type**: Bearer authentication (JWT)


## Author

tito.brasolin@kerberos.energy


