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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Address(BaseModel):
    """
    Address for business
    """ # noqa: E501
    line1: Optional[StrictStr] = Field(default=None, description="Street address")
    line2: Optional[StrictStr] = Field(default=None, description="Street address line 2")
    city: Optional[StrictStr] = Field(default=None, description="City")
    state: Optional[StrictStr] = Field(default=None, description="State")
    postal_code: Optional[StrictStr] = Field(default=None, description="Postal code")
    country: Optional[StrictStr] = Field(default=None, description="Country (ISO 3166-1 alpha-2)")
    __properties: ClassVar[List[str]] = ["line1", "line2", "city", "state", "postal_code", "country"]

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
        """Create an instance of Address from a JSON string"""
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
        # set to None if line2 (nullable) is None
        # and model_fields_set contains the field
        if self.line2 is None and "line2" in self.model_fields_set:
            _dict['line2'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Address from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "line1": obj.get("line1"),
            "line2": obj.get("line2"),
            "city": obj.get("city"),
            "state": obj.get("state"),
            "postal_code": obj.get("postal_code"),
            "country": obj.get("country")
        })
        return _obj

