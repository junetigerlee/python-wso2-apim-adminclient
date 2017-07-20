# swagger_client.MediationIndividualApi

All URIs are relative to *https://apis.wso2.com/api/am/admin/v0.11*

Method | HTTP request | Description
------------- | ------------- | -------------
[**policies_mediation_mediation_policy_id_delete**](MediationIndividualApi.md#policies_mediation_mediation_policy_id_delete) | **DELETE** /policies/mediation/{mediationPolicyId} | Delete an API
[**policies_mediation_mediation_policy_id_get**](MediationIndividualApi.md#policies_mediation_mediation_policy_id_get) | **GET** /policies/mediation/{mediationPolicyId} | Get a global mediation squence
[**policies_mediation_mediation_policy_id_put**](MediationIndividualApi.md#policies_mediation_mediation_policy_id_put) | **PUT** /policies/mediation/{mediationPolicyId} | Update an mediation policy


# **policies_mediation_mediation_policy_id_delete**
> policies_mediation_mediation_policy_id_delete(mediation_policy_id, if_match=if_match, if_unmodified_since=if_unmodified_since)

Delete an API

This operation can be used to delete an existing API proving the Id of the API. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.MediationIndividualApi()
mediation_policy_id = 'mediation_policy_id_example' # str | Mediation policy Id 
if_match = 'if_match_example' # str | Validator for conditional requests; based on ETag.  (optional)
if_unmodified_since = 'if_unmodified_since_example' # str | Validator for conditional requests; based on Last Modified header.  (optional)

try: 
    # Delete an API
    api_instance.policies_mediation_mediation_policy_id_delete(mediation_policy_id, if_match=if_match, if_unmodified_since=if_unmodified_since)
except ApiException as e:
    print("Exception when calling MediationIndividualApi->policies_mediation_mediation_policy_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mediation_policy_id** | **str**| Mediation policy Id  | 
 **if_match** | **str**| Validator for conditional requests; based on ETag.  | [optional] 
 **if_unmodified_since** | **str**| Validator for conditional requests; based on Last Modified header.  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policies_mediation_mediation_policy_id_get**
> Mediation2 policies_mediation_mediation_policy_id_get(mediation_policy_id, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)

Get a global mediation squence

This operation can be used to retrieve a particular global mediation policy. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.MediationIndividualApi()
mediation_policy_id = 'mediation_policy_id_example' # str | Mediation policy Id 
accept = 'JSON' # str | Media types acceptable for the response. Default is JSON.  (optional) (default to JSON)
if_none_match = 'if_none_match_example' # str | Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  (optional)
if_modified_since = 'if_modified_since_example' # str | Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource.  (optional)

try: 
    # Get a global mediation squence
    api_response = api_instance.policies_mediation_mediation_policy_id_get(mediation_policy_id, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediationIndividualApi->policies_mediation_mediation_policy_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mediation_policy_id** | **str**| Mediation policy Id  | 
 **accept** | **str**| Media types acceptable for the response. Default is JSON.  | [optional] [default to JSON]
 **if_none_match** | **str**| Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  | [optional] 
 **if_modified_since** | **str**| Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource.  | [optional] 

### Return type

[**Mediation2**](Mediation2.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policies_mediation_mediation_policy_id_put**
> Mediation2 policies_mediation_mediation_policy_id_put(mediation_policy_id, body, content_type, if_match=if_match, if_unmodified_since=if_unmodified_since)

Update an mediation policy

This operation can be used to update an existing API. But the properties `name`, `version`, `context`, `provider`, `state` will not be changed by this operation. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.MediationIndividualApi()
mediation_policy_id = 'mediation_policy_id_example' # str | Mediation policy Id 
body = swagger_client.Mediation3() # Mediation3 | Mediation policy object that needs to be added 
content_type = 'JSON' # str | Media type of the entity in the body. Default is JSON.  (default to JSON)
if_match = 'if_match_example' # str | Validator for conditional requests; based on ETag.  (optional)
if_unmodified_since = 'if_unmodified_since_example' # str | Validator for conditional requests; based on Last Modified header.  (optional)

try: 
    # Update an mediation policy
    api_response = api_instance.policies_mediation_mediation_policy_id_put(mediation_policy_id, body, content_type, if_match=if_match, if_unmodified_since=if_unmodified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediationIndividualApi->policies_mediation_mediation_policy_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mediation_policy_id** | **str**| Mediation policy Id  | 
 **body** | [**Mediation3**](Mediation3.md)| Mediation policy object that needs to be added  | 
 **content_type** | **str**| Media type of the entity in the body. Default is JSON.  | [default to JSON]
 **if_match** | **str**| Validator for conditional requests; based on ETag.  | [optional] 
 **if_unmodified_since** | **str**| Validator for conditional requests; based on Last Modified header.  | [optional] 

### Return type

[**Mediation2**](Mediation2.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

