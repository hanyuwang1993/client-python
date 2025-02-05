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


class V1beta1RelatedUrl(object):
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
        'url': 'str',
        'label': 'str'
    }

    attribute_map = {
        'url': 'url',
        'label': 'label'
    }

    def __init__(self, url=None, label=None):  # noqa: E501
        """V1beta1RelatedUrl - a model defined in Swagger"""  # noqa: E501

        self._url = None
        self._label = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if label is not None:
            self.label = label

    @property
    def url(self):
        """Gets the url of this V1beta1RelatedUrl.  # noqa: E501

        Specific URL associated with the resource.  # noqa: E501

        :return: The url of this V1beta1RelatedUrl.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this V1beta1RelatedUrl.

        Specific URL associated with the resource.  # noqa: E501

        :param url: The url of this V1beta1RelatedUrl.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def label(self):
        """Gets the label of this V1beta1RelatedUrl.  # noqa: E501

        Label to describe usage of the URL.  # noqa: E501

        :return: The label of this V1beta1RelatedUrl.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this V1beta1RelatedUrl.

        Label to describe usage of the URL.  # noqa: E501

        :param label: The label of this V1beta1RelatedUrl.  # noqa: E501
        :type: str
        """

        self._label = label

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
        if issubclass(V1beta1RelatedUrl, dict):
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
        if not isinstance(other, V1beta1RelatedUrl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
