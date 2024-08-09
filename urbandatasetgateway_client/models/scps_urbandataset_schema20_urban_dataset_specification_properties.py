# coding: utf-8

"""
    UrbanDatasetGateway - OpenAPI 3.0

    This technical specification is one of the **Smart City Platform Specification (SCPS) for Interoperability Layer** [https://smartcityplatform.enea.it/#/en/specification/](https://smartcityplatform.enea.it/#/en/specification/)

    The version of the OpenAPI document: 1.0.0
    Contact: tito.brasolin@kerberos.energy
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from urbandatasetgateway_client.models.scps_urbandataset_schema20_urban_dataset_specification_properties_property_definition_inner import ScpsUrbandatasetSchema20UrbanDatasetSpecificationPropertiesPropertyDefinitionInner
from typing import Optional, Set
from typing_extensions import Self

class ScpsUrbandatasetSchema20UrbanDatasetSpecificationProperties(BaseModel):
    """
    ScpsUrbandatasetSchema20UrbanDatasetSpecificationProperties
    """ # noqa: E501
    property_definition: List[Optional[ScpsUrbandatasetSchema20UrbanDatasetSpecificationPropertiesPropertyDefinitionInner]] = Field(alias="propertyDefinition")
    __properties: ClassVar[List[str]] = ["propertyDefinition"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ScpsUrbandatasetSchema20UrbanDatasetSpecificationProperties from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in property_definition (list)
        _items = []
        if self.property_definition:
            for _item in self.property_definition:
                if _item:
                    _items.append(_item.to_dict())
            _dict['propertyDefinition'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ScpsUrbandatasetSchema20UrbanDatasetSpecificationProperties from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "propertyDefinition": [ScpsUrbandatasetSchema20UrbanDatasetSpecificationPropertiesPropertyDefinitionInner.from_dict(_item) for _item in obj["propertyDefinition"]] if obj.get("propertyDefinition") is not None else None
        })
        return _obj


