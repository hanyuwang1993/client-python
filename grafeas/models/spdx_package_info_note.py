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


class SpdxPackageInfoNote(object):
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
        'title': 'str',
        'version': 'str',
        'supplier': 'str',
        'originator': 'str',
        'download_location': 'str',
        'analyzed': 'bool',
        'verification_code': 'str',
        'checksum': 'str',
        'home_page': 'str',
        'files_license_info': 'list[str]',
        'license_declared': 'SpdxLicense',
        'copyright': 'str',
        'summary_description': 'str',
        'detailed_description': 'str',
        'external_refs': 'list[PackageInfoNoteExternalRef]',
        'attribution': 'str',
        'package_type': 'str'
    }

    attribute_map = {
        'title': 'title',
        'version': 'version',
        'supplier': 'supplier',
        'originator': 'originator',
        'download_location': 'downloadLocation',
        'analyzed': 'analyzed',
        'verification_code': 'verificationCode',
        'checksum': 'checksum',
        'home_page': 'homePage',
        'files_license_info': 'filesLicenseInfo',
        'license_declared': 'licenseDeclared',
        'copyright': 'copyright',
        'summary_description': 'summaryDescription',
        'detailed_description': 'detailedDescription',
        'external_refs': 'externalRefs',
        'attribution': 'attribution',
        'package_type': 'packageType'
    }

    def __init__(self, title=None, version=None, supplier=None, originator=None, download_location=None, analyzed=None, verification_code=None, checksum=None, home_page=None, files_license_info=None, license_declared=None, copyright=None, summary_description=None, detailed_description=None, external_refs=None, attribution=None, package_type=None):  # noqa: E501
        """SpdxPackageInfoNote - a model defined in Swagger"""  # noqa: E501

        self._title = None
        self._version = None
        self._supplier = None
        self._originator = None
        self._download_location = None
        self._analyzed = None
        self._verification_code = None
        self._checksum = None
        self._home_page = None
        self._files_license_info = None
        self._license_declared = None
        self._copyright = None
        self._summary_description = None
        self._detailed_description = None
        self._external_refs = None
        self._attribution = None
        self._package_type = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if version is not None:
            self.version = version
        if supplier is not None:
            self.supplier = supplier
        if originator is not None:
            self.originator = originator
        if download_location is not None:
            self.download_location = download_location
        if analyzed is not None:
            self.analyzed = analyzed
        if verification_code is not None:
            self.verification_code = verification_code
        if checksum is not None:
            self.checksum = checksum
        if home_page is not None:
            self.home_page = home_page
        if files_license_info is not None:
            self.files_license_info = files_license_info
        if license_declared is not None:
            self.license_declared = license_declared
        if copyright is not None:
            self.copyright = copyright
        if summary_description is not None:
            self.summary_description = summary_description
        if detailed_description is not None:
            self.detailed_description = detailed_description
        if external_refs is not None:
            self.external_refs = external_refs
        if attribution is not None:
            self.attribution = attribution
        if package_type is not None:
            self.package_type = package_type

    @property
    def title(self):
        """Gets the title of this SpdxPackageInfoNote.  # noqa: E501


        :return: The title of this SpdxPackageInfoNote.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this SpdxPackageInfoNote.


        :param title: The title of this SpdxPackageInfoNote.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def version(self):
        """Gets the version of this SpdxPackageInfoNote.  # noqa: E501


        :return: The version of this SpdxPackageInfoNote.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SpdxPackageInfoNote.


        :param version: The version of this SpdxPackageInfoNote.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def supplier(self):
        """Gets the supplier of this SpdxPackageInfoNote.  # noqa: E501


        :return: The supplier of this SpdxPackageInfoNote.  # noqa: E501
        :rtype: str
        """
        return self._supplier

    @supplier.setter
    def supplier(self, supplier):
        """Sets the supplier of this SpdxPackageInfoNote.


        :param supplier: The supplier of this SpdxPackageInfoNote.  # noqa: E501
        :type: str
        """

        self._supplier = supplier

    @property
    def originator(self):
        """Gets the originator of this SpdxPackageInfoNote.  # noqa: E501


        :return: The originator of this SpdxPackageInfoNote.  # noqa: E501
        :rtype: str
        """
        return self._originator

    @originator.setter
    def originator(self, originator):
        """Sets the originator of this SpdxPackageInfoNote.


        :param originator: The originator of this SpdxPackageInfoNote.  # noqa: E501
        :type: str
        """

        self._originator = originator

    @property
    def download_location(self):
        """Gets the download_location of this SpdxPackageInfoNote.  # noqa: E501


        :return: The download_location of this SpdxPackageInfoNote.  # noqa: E501
        :rtype: str
        """
        return self._download_location

    @download_location.setter
    def download_location(self, download_location):
        """Sets the download_location of this SpdxPackageInfoNote.


        :param download_location: The download_location of this SpdxPackageInfoNote.  # noqa: E501
        :type: str
        """

        self._download_location = download_location

    @property
    def analyzed(self):
        """Gets the analyzed of this SpdxPackageInfoNote.  # noqa: E501


        :return: The analyzed of this SpdxPackageInfoNote.  # noqa: E501
        :rtype: bool
        """
        return self._analyzed

    @analyzed.setter
    def analyzed(self, analyzed):
        """Sets the analyzed of this SpdxPackageInfoNote.


        :param analyzed: The analyzed of this SpdxPackageInfoNote.  # noqa: E501
        :type: bool
        """

        self._analyzed = analyzed

    @property
    def verification_code(self):
        """Gets the verification_code of this SpdxPackageInfoNote.  # noqa: E501


        :return: The verification_code of this SpdxPackageInfoNote.  # noqa: E501
        :rtype: str
        """
        return self._verification_code

    @verification_code.setter
    def verification_code(self, verification_code):
        """Sets the verification_code of this SpdxPackageInfoNote.


        :param verification_code: The verification_code of this SpdxPackageInfoNote.  # noqa: E501
        :type: str
        """

        self._verification_code = verification_code

    @property
    def checksum(self):
        """Gets the checksum of this SpdxPackageInfoNote.  # noqa: E501


        :return: The checksum of this SpdxPackageInfoNote.  # noqa: E501
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """Sets the checksum of this SpdxPackageInfoNote.


        :param checksum: The checksum of this SpdxPackageInfoNote.  # noqa: E501
        :type: str
        """

        self._checksum = checksum

    @property
    def home_page(self):
        """Gets the home_page of this SpdxPackageInfoNote.  # noqa: E501


        :return: The home_page of this SpdxPackageInfoNote.  # noqa: E501
        :rtype: str
        """
        return self._home_page

    @home_page.setter
    def home_page(self, home_page):
        """Sets the home_page of this SpdxPackageInfoNote.


        :param home_page: The home_page of this SpdxPackageInfoNote.  # noqa: E501
        :type: str
        """

        self._home_page = home_page

    @property
    def files_license_info(self):
        """Gets the files_license_info of this SpdxPackageInfoNote.  # noqa: E501


        :return: The files_license_info of this SpdxPackageInfoNote.  # noqa: E501
        :rtype: list[str]
        """
        return self._files_license_info

    @files_license_info.setter
    def files_license_info(self, files_license_info):
        """Sets the files_license_info of this SpdxPackageInfoNote.


        :param files_license_info: The files_license_info of this SpdxPackageInfoNote.  # noqa: E501
        :type: list[str]
        """

        self._files_license_info = files_license_info

    @property
    def license_declared(self):
        """Gets the license_declared of this SpdxPackageInfoNote.  # noqa: E501


        :return: The license_declared of this SpdxPackageInfoNote.  # noqa: E501
        :rtype: SpdxLicense
        """
        return self._license_declared

    @license_declared.setter
    def license_declared(self, license_declared):
        """Sets the license_declared of this SpdxPackageInfoNote.


        :param license_declared: The license_declared of this SpdxPackageInfoNote.  # noqa: E501
        :type: SpdxLicense
        """

        self._license_declared = license_declared

    @property
    def copyright(self):
        """Gets the copyright of this SpdxPackageInfoNote.  # noqa: E501


        :return: The copyright of this SpdxPackageInfoNote.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this SpdxPackageInfoNote.


        :param copyright: The copyright of this SpdxPackageInfoNote.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def summary_description(self):
        """Gets the summary_description of this SpdxPackageInfoNote.  # noqa: E501


        :return: The summary_description of this SpdxPackageInfoNote.  # noqa: E501
        :rtype: str
        """
        return self._summary_description

    @summary_description.setter
    def summary_description(self, summary_description):
        """Sets the summary_description of this SpdxPackageInfoNote.


        :param summary_description: The summary_description of this SpdxPackageInfoNote.  # noqa: E501
        :type: str
        """

        self._summary_description = summary_description

    @property
    def detailed_description(self):
        """Gets the detailed_description of this SpdxPackageInfoNote.  # noqa: E501


        :return: The detailed_description of this SpdxPackageInfoNote.  # noqa: E501
        :rtype: str
        """
        return self._detailed_description

    @detailed_description.setter
    def detailed_description(self, detailed_description):
        """Sets the detailed_description of this SpdxPackageInfoNote.


        :param detailed_description: The detailed_description of this SpdxPackageInfoNote.  # noqa: E501
        :type: str
        """

        self._detailed_description = detailed_description

    @property
    def external_refs(self):
        """Gets the external_refs of this SpdxPackageInfoNote.  # noqa: E501


        :return: The external_refs of this SpdxPackageInfoNote.  # noqa: E501
        :rtype: list[PackageInfoNoteExternalRef]
        """
        return self._external_refs

    @external_refs.setter
    def external_refs(self, external_refs):
        """Sets the external_refs of this SpdxPackageInfoNote.


        :param external_refs: The external_refs of this SpdxPackageInfoNote.  # noqa: E501
        :type: list[PackageInfoNoteExternalRef]
        """

        self._external_refs = external_refs

    @property
    def attribution(self):
        """Gets the attribution of this SpdxPackageInfoNote.  # noqa: E501


        :return: The attribution of this SpdxPackageInfoNote.  # noqa: E501
        :rtype: str
        """
        return self._attribution

    @attribution.setter
    def attribution(self, attribution):
        """Sets the attribution of this SpdxPackageInfoNote.


        :param attribution: The attribution of this SpdxPackageInfoNote.  # noqa: E501
        :type: str
        """

        self._attribution = attribution

    @property
    def package_type(self):
        """Gets the package_type of this SpdxPackageInfoNote.  # noqa: E501

        The type of package: OS, MAVEN, GO, GO_STDLIB, etc.  # noqa: E501

        :return: The package_type of this SpdxPackageInfoNote.  # noqa: E501
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        """Sets the package_type of this SpdxPackageInfoNote.

        The type of package: OS, MAVEN, GO, GO_STDLIB, etc.  # noqa: E501

        :param package_type: The package_type of this SpdxPackageInfoNote.  # noqa: E501
        :type: str
        """

        self._package_type = package_type

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
        if issubclass(SpdxPackageInfoNote, dict):
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
        if not isinstance(other, SpdxPackageInfoNote):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
