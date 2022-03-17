# grafeas.ProjectsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projects_create_project**](ProjectsApi.md#projects_create_project) | **POST** /v1beta1/projects | Creates a new project.
[**projects_delete_project**](ProjectsApi.md#projects_delete_project) | **DELETE** /v1beta1/{name} | Deletes the specified project.
[**projects_get_project**](ProjectsApi.md#projects_get_project) | **GET** /v1beta1/{name} | Gets the specified project.
[**projects_list_projects**](ProjectsApi.md#projects_list_projects) | **GET** /v1beta1/projects | Lists projects.


# **projects_create_project**
> ProjectProject projects_create_project(body)

Creates a new project.

### Example
```python
from __future__ import print_function
import time
import grafeas
from grafeas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = grafeas.ProjectsApi()
body = grafeas.ProjectProject() # ProjectProject | The project to create.

try:
    # Creates a new project.
    api_response = api_instance.projects_create_project(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectProject**](ProjectProject.md)| The project to create. | 

### Return type

[**ProjectProject**](ProjectProject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_delete_project**
> object projects_delete_project(name)

Deletes the specified project.

### Example
```python
from __future__ import print_function
import time
import grafeas
from grafeas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = grafeas.ProjectsApi()
name = 'name_example' # str | The name of the project in the form of `projects/{PROJECT_ID}`.

try:
    # Deletes the specified project.
    api_response = api_instance.projects_delete_project(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_delete_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the project in the form of &#x60;projects/{PROJECT_ID}&#x60;. | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_get_project**
> ProjectProject projects_get_project(name)

Gets the specified project.

### Example
```python
from __future__ import print_function
import time
import grafeas
from grafeas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = grafeas.ProjectsApi()
name = 'name_example' # str | The name of the project in the form of `projects/{PROJECT_ID}`.

try:
    # Gets the specified project.
    api_response = api_instance.projects_get_project(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the project in the form of &#x60;projects/{PROJECT_ID}&#x60;. | 

### Return type

[**ProjectProject**](ProjectProject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_list_projects**
> ProjectListProjectsResponse projects_list_projects(filter=filter, page_size=page_size, page_token=page_token)

Lists projects.

### Example
```python
from __future__ import print_function
import time
import grafeas
from grafeas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = grafeas.ProjectsApi()
filter = 'filter_example' # str | The filter expression. (optional)
page_size = 56 # int | Number of projects to return in the list. (optional)
page_token = 'page_token_example' # str | Token to provide to skip to a particular spot in the list. (optional)

try:
    # Lists projects.
    api_response = api_instance.projects_list_projects(filter=filter, page_size=page_size, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_list_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| The filter expression. | [optional] 
 **page_size** | **int**| Number of projects to return in the list. | [optional] 
 **page_token** | **str**| Token to provide to skip to a particular spot in the list. | [optional] 

### Return type

[**ProjectListProjectsResponse**](ProjectListProjectsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

