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


class IntotoLink(object):
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
        'command': 'list[str]',
        'materials': 'list[IntotoLinkArtifact]',
        'products': 'list[IntotoLinkArtifact]',
        'byproducts': 'LinkByProducts',
        'environment': 'LinkEnvironment'
    }

    attribute_map = {
        'command': 'command',
        'materials': 'materials',
        'products': 'products',
        'byproducts': 'byproducts',
        'environment': 'environment'
    }

    def __init__(self, command=None, materials=None, products=None, byproducts=None, environment=None):  # noqa: E501
        """IntotoLink - a model defined in Swagger"""  # noqa: E501

        self._command = None
        self._materials = None
        self._products = None
        self._byproducts = None
        self._environment = None
        self.discriminator = None

        if command is not None:
            self.command = command
        if materials is not None:
            self.materials = materials
        if products is not None:
            self.products = products
        if byproducts is not None:
            self.byproducts = byproducts
        if environment is not None:
            self.environment = environment

    @property
    def command(self):
        """Gets the command of this IntotoLink.  # noqa: E501


        :return: The command of this IntotoLink.  # noqa: E501
        :rtype: list[str]
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this IntotoLink.


        :param command: The command of this IntotoLink.  # noqa: E501
        :type: list[str]
        """

        self._command = command

    @property
    def materials(self):
        """Gets the materials of this IntotoLink.  # noqa: E501


        :return: The materials of this IntotoLink.  # noqa: E501
        :rtype: list[IntotoLinkArtifact]
        """
        return self._materials

    @materials.setter
    def materials(self, materials):
        """Sets the materials of this IntotoLink.


        :param materials: The materials of this IntotoLink.  # noqa: E501
        :type: list[IntotoLinkArtifact]
        """

        self._materials = materials

    @property
    def products(self):
        """Gets the products of this IntotoLink.  # noqa: E501

        Products are the supply chain artifacts generated as a result of the step. The structure is identical to that of materials.  # noqa: E501

        :return: The products of this IntotoLink.  # noqa: E501
        :rtype: list[IntotoLinkArtifact]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this IntotoLink.

        Products are the supply chain artifacts generated as a result of the step. The structure is identical to that of materials.  # noqa: E501

        :param products: The products of this IntotoLink.  # noqa: E501
        :type: list[IntotoLinkArtifact]
        """

        self._products = products

    @property
    def byproducts(self):
        """Gets the byproducts of this IntotoLink.  # noqa: E501

        ByProducts are data generated as part of a software supply chain step, but are not the actual result of the step.  # noqa: E501

        :return: The byproducts of this IntotoLink.  # noqa: E501
        :rtype: LinkByProducts
        """
        return self._byproducts

    @byproducts.setter
    def byproducts(self, byproducts):
        """Sets the byproducts of this IntotoLink.

        ByProducts are data generated as part of a software supply chain step, but are not the actual result of the step.  # noqa: E501

        :param byproducts: The byproducts of this IntotoLink.  # noqa: E501
        :type: LinkByProducts
        """

        self._byproducts = byproducts

    @property
    def environment(self):
        """Gets the environment of this IntotoLink.  # noqa: E501


        :return: The environment of this IntotoLink.  # noqa: E501
        :rtype: LinkEnvironment
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this IntotoLink.


        :param environment: The environment of this IntotoLink.  # noqa: E501
        :type: LinkEnvironment
        """

        self._environment = environment

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
        if issubclass(IntotoLink, dict):
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
        if not isinstance(other, IntotoLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
