# coding: utf-8

"""
    UrbanDatasetGateway - OpenAPI 3.0

    **Smart City Platform Specification (SCPS) for Interoperability Layer** [https://smartcityplatform.enea.it/#/en/specification/](https://smartcityplatform.enea.it/#/en/specification/)  **Smart City Platform Specification (SCPS) Communication 2.0** [https://smartcityplatform.enea.it/#/en/specification/communication/2.0/](https://smartcityplatform.enea.it/#/en/specification/communication/2.0/)

    The version of the OpenAPI document: 2.0.0
    Contact: tito.brasolin@kerberos.energy
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "urbandatasetgateway-client"
VERSION = "1.0.0"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="UrbanDatasetGateway - OpenAPI 3.0",
    author="Tito Brasolin",
    author_email="tito.brasolin@kerberos.energy",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "UrbanDatasetGateway - OpenAPI 3.0"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache 2.0",
    long_description_content_type='text/markdown',
    long_description="""\
    **Smart City Platform Specification (SCPS) for Interoperability Layer** [https://smartcityplatform.enea.it/#/en/specification/](https://smartcityplatform.enea.it/#/en/specification/)  **Smart City Platform Specification (SCPS) Communication 2.0** [https://smartcityplatform.enea.it/#/en/specification/communication/2.0/](https://smartcityplatform.enea.it/#/en/specification/communication/2.0/)
    """,  # noqa: E501
    package_data={"urbandatasetgateway_client": ["py.typed"]},
)
