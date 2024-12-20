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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from main_openapi_client.models.bank_account_ach_info import BankAccountAchInfo
from typing import Optional, Set
from typing_extensions import Self

class BankAccount(BaseModel):
    """
    A bank account
    """ # noqa: E501
    id: StrictInt = Field(description="ID of the bank account.")
    owner_name: StrictStr = Field(description="Name of the bank account owner.")
    account_number: StrictStr = Field(description="Bank account number.")
    routing_number: StrictStr = Field(description="Bank account routing number.")
    arena_id: StrictInt = Field(description="Arena ID this bank account belongs to.")
    ach_info: Optional[BankAccountAchInfo] = None
    __properties: ClassVar[List[str]] = ["id", "owner_name", "account_number", "routing_number", "arena_id", "ach_info"]

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
        """Create an instance of BankAccount from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
            "owner_name",
            "account_number",
            "routing_number",
            "arena_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of ach_info
        if self.ach_info:
            _dict['ach_info'] = self.ach_info.to_dict()
        # set to None if ach_info (nullable) is None
        # and model_fields_set contains the field
        if self.ach_info is None and "ach_info" in self.model_fields_set:
            _dict['ach_info'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BankAccount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "owner_name": obj.get("owner_name"),
            "account_number": obj.get("account_number"),
            "routing_number": obj.get("routing_number"),
            "arena_id": obj.get("arena_id"),
            "ach_info": BankAccountAchInfo.from_dict(obj["ach_info"]) if obj.get("ach_info") is not None else None
        })
        return _obj

