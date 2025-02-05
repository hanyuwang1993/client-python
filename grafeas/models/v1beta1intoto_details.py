# coding: utf-8

"""
    grafeas.proto

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1beta1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1beta1intotoDetails(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'signatures': 'list[V1beta1intotoSignature]',
        'signed': 'IntotoLink'
    }

    attribute_map = {
        'signatures': 'signatures',
        'signed': 'signed'
    }

    def __init__(self, signatures=None, signed=None):  # noqa: E501
        """V1beta1intotoDetails - a model defined in Swagger"""  # noqa: E501

        self._signatures = None
        self._signed = None
        self.discriminator = None

        if signatures is not None:
            self.signatures = signatures
        if signed is not None:
            self.signed = signed

    @property
    def signatures(self):
        """Gets the signatures of this V1beta1intotoDetails.  # noqa: E501


        :return: The signatures of this V1beta1intotoDetails.  # noqa: E501
        :rtype: list[V1beta1intotoSignature]
        """
        return self._signatures

    @signatures.setter
    def signatures(self, signatures):
        """Sets the signatures of this V1beta1intotoDetails.


        :param signatures: The signatures of this V1beta1intotoDetails.  # noqa: E501
        :type: list[V1beta1intotoSignature]
        """

        self._signatures = signatures

    @property
    def signed(self):
        """Gets the signed of this V1beta1intotoDetails.  # noqa: E501


        :return: The signed of this V1beta1intotoDetails.  # noqa: E501
        :rtype: IntotoLink
        """
        return self._signed

    @signed.setter
    def signed(self, signed):
        """Sets the signed of this V1beta1intotoDetails.


        :param signed: The signed of this V1beta1intotoDetails.  # noqa: E501
        :type: IntotoLink
        """

        self._signed = signed

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(V1beta1intotoDetails, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1beta1intotoDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
