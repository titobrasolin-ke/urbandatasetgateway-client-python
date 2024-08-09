# urbandatasetgateway-client
This technical specification is one of the **Smart City Platform Specification (SCPS) for Interoperability Layer**
[https://smartcityplatform.enea.it/#/en/specification/](https://smartcityplatform.enea.it/#/en/specification/)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
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
    last_request_request = {"resource_id":"SCP-1_SmartBuildingCasaccia-3_SmartBuildingAnomalies-1.0_20180125120000"} # LastRequestRequest |  (optional)

    try:
        # lastRequest REST method
        api_response = api_instance.last_request(last_request_request=last_request_request)
        print("The response of UrbanDatasetGatewayApi->last_request:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UrbanDatasetGatewayApi->last_request: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://kerberos-lab.it/webservices/rest/index.php/UrbanDatasetGateway*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*UrbanDatasetGatewayApi* | [**last_request**](docs/UrbanDatasetGatewayApi.md#last_request) | **POST** /lastRequest | lastRequest REST method
*UrbanDatasetGatewayApi* | [**login**](docs/UrbanDatasetGatewayApi.md#login) | **POST** /login | login REST method
*UrbanDatasetGatewayApi* | [**push**](docs/UrbanDatasetGatewayApi.md#push) | **POST** /push | push REST method
*UrbanDatasetGatewayApi* | [**searching_request**](docs/UrbanDatasetGatewayApi.md#searching_request) | **POST** /searchingRequest | searchingRequest REST method
*UrbanDatasetGatewayApi* | [**test**](docs/UrbanDatasetGatewayApi.md#test) | **GET** /test | test REST method


## Documentation For Models

 - [LastRequest200Response](docs/LastRequest200Response.md)
 - [LastRequestRequest](docs/LastRequestRequest.md)
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
 - [SearchingRequest200Response](docs/SearchingRequest200Response.md)
 - [SearchingRequestRequest](docs/SearchingRequestRequest.md)
 - [Test200Response](docs/Test200Response.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="bearerAuth"></a>
### bearerAuth

- **Type**: Bearer authentication (JWT)


## Author

tito.brasolin@kerberos.energy


