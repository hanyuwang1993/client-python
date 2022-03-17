# coding: utf-8

"""
    project.proto

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1beta1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import grafeas
from grafeas.api.projects_api import ProjectsApi  # noqa: E501
from grafeas.rest import ApiException


class TestProjectsApi(unittest.TestCase):
    """ProjectsApi unit test stubs"""

    def setUp(self):
        self.api = grafeas.api.projects_api.ProjectsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_projects_create_project(self):
        """Test case for projects_create_project

        Creates a new project.  # noqa: E501
        """
        pass

    def test_projects_delete_project(self):
        """Test case for projects_delete_project

        Deletes the specified project.  # noqa: E501
        """
        pass

    def test_projects_get_project(self):
        """Test case for projects_get_project

        Gets the specified project.  # noqa: E501
        """
        pass

    def test_projects_list_projects(self):
        """Test case for projects_list_projects

        Lists projects.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
