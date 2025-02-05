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


class Grafeasv1beta1Signature(object):
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
        'signature': 'str',
        'public_key_id': 'str'
    }

    attribute_map = {
        'signature': 'signature',
        'public_key_id': 'publicKeyId'
    }

    def __init__(self, signature=None, public_key_id=None):  # noqa: E501
        """Grafeasv1beta1Signature - a model defined in Swagger"""  # noqa: E501

        self._signature = None
        self._public_key_id = None
        self.discriminator = None

        if signature is not None:
            self.signature = signature
        if public_key_id is not None:
            self.public_key_id = public_key_id

    @property
    def signature(self):
        """Gets the signature of this Grafeasv1beta1Signature.  # noqa: E501

        The content of the signature, an opaque bytestring. The payload that this signature verifies MUST be unambiguously provided with the Signature during verification. A wrapper message might provide the payload explicitly. Alternatively, a message might have a canonical serialization that can always be unambiguously computed to derive the payload.  # noqa: E501

        :return: The signature of this Grafeasv1beta1Signature.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this Grafeasv1beta1Signature.

        The content of the signature, an opaque bytestring. The payload that this signature verifies MUST be unambiguously provided with the Signature during verification. A wrapper message might provide the payload explicitly. Alternatively, a message might have a canonical serialization that can always be unambiguously computed to derive the payload.  # noqa: E501

        :param signature: The signature of this Grafeasv1beta1Signature.  # noqa: E501
        :type: str
        """
        if signature is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', signature):  # noqa: E501
            raise ValueError(r"Invalid value for `signature`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._signature = signature

    @property
    def public_key_id(self):
        """Gets the public_key_id of this Grafeasv1beta1Signature.  # noqa: E501

        The identifier for the public key that verifies this signature.   * The `public_key_id` is required.   * The `public_key_id` SHOULD be an RFC3986 conformant URI.   * When possible, the `public_key_id` SHOULD be an immutable reference,     such as a cryptographic digest.  Examples of valid `public_key_id`s:  OpenPGP V4 public key fingerprint:   * \"openpgp4fpr:74FAF3B861BDA0870C7B6DEF607E48D2A663AEEA\" See https://www.iana.org/assignments/uri-schemes/prov/openpgp4fpr for more details on this scheme.  RFC6920 digest-named SubjectPublicKeyInfo (digest of the DER serialization):   * \"ni:///sha-256;cD9o9Cq6LG3jD0iKXqEi_vdjJGecm_iXkbqVoScViaU\"   * \"nih:///sha-256;703f68f42aba2c6de30f488a5ea122fef76324679c9bf89791ba95a1271589a5\"  # noqa: E501

        :return: The public_key_id of this Grafeasv1beta1Signature.  # noqa: E501
        :rtype: str
        """
        return self._public_key_id

    @public_key_id.setter
    def public_key_id(self, public_key_id):
        """Sets the public_key_id of this Grafeasv1beta1Signature.

        The identifier for the public key that verifies this signature.   * The `public_key_id` is required.   * The `public_key_id` SHOULD be an RFC3986 conformant URI.   * When possible, the `public_key_id` SHOULD be an immutable reference,     such as a cryptographic digest.  Examples of valid `public_key_id`s:  OpenPGP V4 public key fingerprint:   * \"openpgp4fpr:74FAF3B861BDA0870C7B6DEF607E48D2A663AEEA\" See https://www.iana.org/assignments/uri-schemes/prov/openpgp4fpr for more details on this scheme.  RFC6920 digest-named SubjectPublicKeyInfo (digest of the DER serialization):   * \"ni:///sha-256;cD9o9Cq6LG3jD0iKXqEi_vdjJGecm_iXkbqVoScViaU\"   * \"nih:///sha-256;703f68f42aba2c6de30f488a5ea122fef76324679c9bf89791ba95a1271589a5\"  # noqa: E501

        :param public_key_id: The public_key_id of this Grafeasv1beta1Signature.  # noqa: E501
        :type: str
        """

        self._public_key_id = public_key_id

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
        if issubclass(Grafeasv1beta1Signature, dict):
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
        if not isinstance(other, Grafeasv1beta1Signature):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
