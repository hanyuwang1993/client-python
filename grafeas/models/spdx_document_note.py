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


class SpdxDocumentNote(object):
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
        'spdx_version': 'str',
        'data_licence': 'str'
    }

    attribute_map = {
        'spdx_version': 'spdxVersion',
        'data_licence': 'dataLicence'
    }

    def __init__(self, spdx_version=None, data_licence=None):  # noqa: E501
        """SpdxDocumentNote - a model defined in Swagger"""  # noqa: E501

        self._spdx_version = None
        self._data_licence = None
        self.discriminator = None

        if spdx_version is not None:
            self.spdx_version = spdx_version
        if data_licence is not None:
            self.data_licence = data_licence

    @property
    def spdx_version(self):
        """Gets the spdx_version of this SpdxDocumentNote.  # noqa: E501


        :return: The spdx_version of this SpdxDocumentNote.  # noqa: E501
        :rtype: str
        """
        return self._spdx_version

    @spdx_version.setter
    def spdx_version(self, spdx_version):
        """Sets the spdx_version of this SpdxDocumentNote.


        :param spdx_version: The spdx_version of this SpdxDocumentNote.  # noqa: E501
        :type: str
        """

        self._spdx_version = spdx_version

    @property
    def data_licence(self):
        """Gets the data_licence of this SpdxDocumentNote.  # noqa: E501


        :return: The data_licence of this SpdxDocumentNote.  # noqa: E501
        :rtype: str
        """
        return self._data_licence

    @data_licence.setter
    def data_licence(self, data_licence):
        """Sets the data_licence of this SpdxDocumentNote.


        :param data_licence: The data_licence of this SpdxDocumentNote.  # noqa: E501
        :type: str
        """

        self._data_licence = data_licence

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
        if issubclass(SpdxDocumentNote, dict):
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
        if not isinstance(other, SpdxDocumentNote):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
