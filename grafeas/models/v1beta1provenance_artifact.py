# coding: utf-8

"""
    grafeas.proto

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: version not set
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1beta1provenanceArtifact(object):
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
        'checksum': 'str',
        'id': 'str',
        'names': 'list[str]'
    }

    attribute_map = {
        'checksum': 'checksum',
        'id': 'id',
        'names': 'names'
    }

    def __init__(self, checksum=None, id=None, names=None):  # noqa: E501
        """V1beta1provenanceArtifact - a model defined in Swagger"""  # noqa: E501

        self._checksum = None
        self._id = None
        self._names = None
        self.discriminator = None

        if checksum is not None:
            self.checksum = checksum
        if id is not None:
            self.id = id
        if names is not None:
            self.names = names

    @property
    def checksum(self):
        """Gets the checksum of this V1beta1provenanceArtifact.  # noqa: E501

        Hash or checksum value of a binary, or Docker Registry 2.0 digest of a container.  # noqa: E501

        :return: The checksum of this V1beta1provenanceArtifact.  # noqa: E501
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """Sets the checksum of this V1beta1provenanceArtifact.

        Hash or checksum value of a binary, or Docker Registry 2.0 digest of a container.  # noqa: E501

        :param checksum: The checksum of this V1beta1provenanceArtifact.  # noqa: E501
        :type: str
        """

        self._checksum = checksum

    @property
    def id(self):
        """Gets the id of this V1beta1provenanceArtifact.  # noqa: E501

        Artifact ID, if any; for container images, this will be a URL by digest like `gcr.io/projectID/imagename@sha256:123456`.  # noqa: E501

        :return: The id of this V1beta1provenanceArtifact.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V1beta1provenanceArtifact.

        Artifact ID, if any; for container images, this will be a URL by digest like `gcr.io/projectID/imagename@sha256:123456`.  # noqa: E501

        :param id: The id of this V1beta1provenanceArtifact.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def names(self):
        """Gets the names of this V1beta1provenanceArtifact.  # noqa: E501

        Related artifact names. This may be the path to a binary or jar file, or in the case of a container build, the name used to push the container image to Google Container Registry, as presented to `docker push`. Note that a single Artifact ID can have multiple names, for example if two tags are applied to one image.  # noqa: E501

        :return: The names of this V1beta1provenanceArtifact.  # noqa: E501
        :rtype: list[str]
        """
        return self._names

    @names.setter
    def names(self, names):
        """Sets the names of this V1beta1provenanceArtifact.

        Related artifact names. This may be the path to a binary or jar file, or in the case of a container build, the name used to push the container image to Google Container Registry, as presented to `docker push`. Note that a single Artifact ID can have multiple names, for example if two tags are applied to one image.  # noqa: E501

        :param names: The names of this V1beta1provenanceArtifact.  # noqa: E501
        :type: list[str]
        """

        self._names = names

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
        if issubclass(V1beta1provenanceArtifact, dict):
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
        if not isinstance(other, V1beta1provenanceArtifact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
