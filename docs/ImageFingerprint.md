# ImageFingerprint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**v1_name** | **str** | Required. The layer ID of the final layer in the Docker image&#39;s v1 representation. | [optional] 
**v2_blob** | **list[str]** | Required. The ordered list of v2 blobs that represent a given image. | [optional] 
**v2_name** | **str** | Output only. The name of the image&#39;s v2 blobs computed via:   [bottom] :&#x3D; v2_blob[bottom]   [N] :&#x3D; sha256(v2_blob[N] + \&quot; \&quot; + v2_name[N+1]) Only the name of the final blob is kept. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


