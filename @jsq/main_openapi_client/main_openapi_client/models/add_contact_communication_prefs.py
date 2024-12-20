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
from typing import Optional, Set
from typing_extensions import Self

class AddContactCommunicationPrefs(BaseModel):
    """
    Account contact add communication pref
    """ # noqa: E501
    arena_id: StrictInt = Field(description="Arena ID")
    account_id: StrictInt = Field(description="Account ID")
    label: Optional[StrictStr] = Field(default=None, description="Relationship label for account contact")
    is_main_contact: Optional[StrictBool] = Field(default=None, description="True if the account contact is To contact, False for CC contact")
    is_admin_contact: Optional[StrictBool] = Field(default=None, description="True if the account contact is an admin contact")
    distribution_list: Optional[List[StrictInt]] = Field(default=None, description="List of distribution IDs")
    __properties: ClassVar[List[str]] = ["arena_id", "account_id", "label", "is_main_contact", "is_admin_contact", "distribution_list"]

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
        """Create an instance of AddContactCommunicationPrefs from a JSON string"""
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
        # set to None if label (nullable) is None
        # and model_fields_set contains the field
        if self.label is None and "label" in self.model_fields_set:
            _dict['label'] = None

        # set to None if is_main_contact (nullable) is None
        # and model_fields_set contains the field
        if self.is_main_contact is None and "is_main_contact" in self.model_fields_set:
            _dict['is_main_contact'] = None

        # set to None if is_admin_contact (nullable) is None
        # and model_fields_set contains the field
        if self.is_admin_contact is None and "is_admin_contact" in self.model_fields_set:
            _dict['is_admin_contact'] = None

        # set to None if distribution_list (nullable) is None
        # and model_fields_set contains the field
        if self.distribution_list is None and "distribution_list" in self.model_fields_set:
            _dict['distribution_list'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AddContactCommunicationPrefs from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "arena_id": obj.get("arena_id"),
            "account_id": obj.get("account_id"),
            "label": obj.get("label"),
            "is_main_contact": obj.get("is_main_contact"),
            "is_admin_contact": obj.get("is_admin_contact"),
            "distribution_list": obj.get("distribution_list")
        })
        return _obj

