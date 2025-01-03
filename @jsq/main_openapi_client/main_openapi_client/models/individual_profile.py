# coding: utf-8

"""
    Juniper Square Internal API

    An internal API for inter-service communication at JSQ.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from main_openapi_client.models.business_info_documents_inner import BusinessInfoDocumentsInner
from main_openapi_client.models.individual_profile_address import IndividualProfileAddress
from typing import Optional, Set
from typing_extensions import Self

class IndividualProfile(BaseModel):
    """
    Individual profile for diligence
    """ # noqa: E501
    external_profile_id: StrictInt = Field(description="Profile ID for diligence")
    first_name: StrictStr = Field(description="First name")
    last_name: StrictStr = Field(description="Last name")
    date_of_birth: StrictStr = Field(description="Date of birth")
    tax_id: StrictStr = Field(description="SSN")
    address: IndividualProfileAddress
    documents: List[BusinessInfoDocumentsInner] = Field(description="Documents for individual")
    is_beneficial_owner: Optional[StrictBool] = Field(default=None, description="Whether the individual is a beneficial owner")
    is_controller: Optional[StrictBool] = Field(default=None, description="Whether the individual is a controller")
    is_signatory: Optional[StrictBool] = Field(default=None, description="Whether the individual is a signatory")
    business_ownership_percent: Optional[StrictInt] = Field(default=None, description="Potential percentage of the business the individual owns")
    __properties: ClassVar[List[str]] = ["external_profile_id", "first_name", "last_name", "date_of_birth", "tax_id", "address", "documents", "is_beneficial_owner", "is_controller", "is_signatory", "business_ownership_percent"]

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
        """Create an instance of IndividualProfile from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['address'] = self.address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in documents (list)
        _items = []
        if self.documents:
            for _item_documents in self.documents:
                if _item_documents:
                    _items.append(_item_documents.to_dict())
            _dict['documents'] = _items
        # set to None if business_ownership_percent (nullable) is None
        # and model_fields_set contains the field
        if self.business_ownership_percent is None and "business_ownership_percent" in self.model_fields_set:
            _dict['business_ownership_percent'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IndividualProfile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "external_profile_id": obj.get("external_profile_id"),
            "first_name": obj.get("first_name"),
            "last_name": obj.get("last_name"),
            "date_of_birth": obj.get("date_of_birth"),
            "tax_id": obj.get("tax_id"),
            "address": IndividualProfileAddress.from_dict(obj["address"]) if obj.get("address") is not None else None,
            "documents": [BusinessInfoDocumentsInner.from_dict(_item) for _item in obj["documents"]] if obj.get("documents") is not None else None,
            "is_beneficial_owner": obj.get("is_beneficial_owner"),
            "is_controller": obj.get("is_controller"),
            "is_signatory": obj.get("is_signatory"),
            "business_ownership_percent": obj.get("business_ownership_percent")
        })
        return _obj


