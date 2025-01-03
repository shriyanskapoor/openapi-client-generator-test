# coding: utf-8

"""
    Juniper Square Internal API

    An internal API for inter-service communication at JSQ.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class DiligenceCategory(str, Enum):
    """
    Category of Diligence
    """

    """
    allowed enum values
    """
    PAYMENTS_ONBOARDING_FLOW = 'payments_onboarding_flow'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DiligenceCategory from a JSON string"""
        return cls(json.loads(json_str))


