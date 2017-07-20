# swagger_client.AdvancedPoliciesApi

All URIs are relative to *https://apis.wso2.com/api/am/admin/v0.11*

Method | HTTP request | Description
------------- | ------------- | -------------
[**throttling_policies_advanced_get**](AdvancedPoliciesApi.md#throttling_policies_advanced_get) | **GET** /throttling/policies/advanced | Get all Advanced level throttle policies
[**throttling_policies_advanced_policy_id_delete**](AdvancedPoliciesApi.md#throttling_policies_advanced_policy_id_delete) | **DELETE** /throttling/policies/advanced/{policyId} | Delete an Advanced level throttle policy
[**throttling_policies_advanced_policy_id_get**](AdvancedPoliciesApi.md#throttling_policies_advanced_policy_id_get) | **GET** /throttling/policies/advanced/{policyId} | Retrieve an Advanced Policy
[**throttling_policies_advanced_policy_id_put**](AdvancedPoliciesApi.md#throttling_policies_advanced_policy_id_put) | **PUT** /throttling/policies/advanced/{policyId} | Update an Advanced level throttle policy
[**throttling_policies_advanced_post**](AdvancedPoliciesApi.md#throttling_policies_advanced_post) | **POST** /throttling/policies/advanced | Add an Advanced level throttle policy


# **throttling_policies_advanced_get**
> AdvancedThrottlePolicyList throttling_policies_advanced_get(accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)

Get all Advanced level throttle policies

Get all Advanced level throttle policies 

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
api_instance = swagger_client.AdvancedPoliciesApi()
accept = 'JSON' # str | Media types acceptable for the response. Default is JSON.  (optional) (default to JSON)
if_none_match = 'if_none_match_example' # str | Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  (optional)
if_modified_since = 'if_modified_since_example' # str | Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource.  (optional)

try: 
    # Get all Advanced level throttle policies
    api_response = api_instance.throttling_policies_advanced_get(accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvancedPoliciesApi->throttling_policies_advanced_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Media types acceptable for the response. Default is JSON.  | [optional] [default to JSON]
 **if_none_match** | **str**| Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  | [optional] 
 **if_modified_since** | **str**| Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource.  | [optional] 

### Return type

[**AdvancedThrottlePolicyList**](AdvancedThrottlePolicyList.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **throttling_policies_advanced_policy_id_delete**
> throttling_policies_advanced_policy_id_delete(policy_id, if_match=if_match, if_unmodified_since=if_unmodified_since)

Delete an Advanced level throttle policy

Delete an Advanced level throttle policy 

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
api_instance = swagger_client.AdvancedPoliciesApi()
policy_id = 'policy_id_example' # str | Thorttle policy UUID 
if_match = 'if_match_example' # str | Validator for conditional requests; based on ETag.  (optional)
if_unmodified_since = 'if_unmodified_since_example' # str | Validator for conditional requests; based on Last Modified header.  (optional)

try: 
    # Delete an Advanced level throttle policy
    api_instance.throttling_policies_advanced_policy_id_delete(policy_id, if_match=if_match, if_unmodified_since=if_unmodified_since)
except ApiException as e:
    print("Exception when calling AdvancedPoliciesApi->throttling_policies_advanced_policy_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| Thorttle policy UUID  | 
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

# **throttling_policies_advanced_policy_id_get**
> GenericThrottlePolicy10 throttling_policies_advanced_policy_id_get(policy_id, if_none_match=if_none_match, if_modified_since=if_modified_since)

Retrieve an Advanced Policy

Retrieve a Advanced Policy providing the policy name. 

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
api_instance = swagger_client.AdvancedPoliciesApi()
policy_id = 'policy_id_example' # str | Thorttle policy UUID 
if_none_match = 'if_none_match_example' # str | Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  (optional)
if_modified_since = 'if_modified_since_example' # str | Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource.  (optional)

try: 
    # Retrieve an Advanced Policy
    api_response = api_instance.throttling_policies_advanced_policy_id_get(policy_id, if_none_match=if_none_match, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvancedPoliciesApi->throttling_policies_advanced_policy_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| Thorttle policy UUID  | 
 **if_none_match** | **str**| Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  | [optional] 
 **if_modified_since** | **str**| Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource.  | [optional] 

### Return type

[**GenericThrottlePolicy10**](GenericThrottlePolicy10.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **throttling_policies_advanced_policy_id_put**
> GenericThrottlePolicy10 throttling_policies_advanced_policy_id_put(policy_id, body, content_type, if_match=if_match, if_unmodified_since=if_unmodified_since)

Update an Advanced level throttle policy

Update an Advanced level throttle policy 

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
api_instance = swagger_client.AdvancedPoliciesApi()
policy_id = 'policy_id_example' # str | Thorttle policy UUID 
body = swagger_client.GenericThrottlePolicy11() # GenericThrottlePolicy11 | Policy object that needs to be modified 
content_type = 'JSON' # str | Media type of the entity in the body. Default is JSON.  (default to JSON)
if_match = 'if_match_example' # str | Validator for conditional requests; based on ETag.  (optional)
if_unmodified_since = 'if_unmodified_since_example' # str | Validator for conditional requests; based on Last Modified header.  (optional)

try: 
    # Update an Advanced level throttle policy
    api_response = api_instance.throttling_policies_advanced_policy_id_put(policy_id, body, content_type, if_match=if_match, if_unmodified_since=if_unmodified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvancedPoliciesApi->throttling_policies_advanced_policy_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| Thorttle policy UUID  | 
 **body** | [**GenericThrottlePolicy11**](GenericThrottlePolicy11.md)| Policy object that needs to be modified  | 
 **content_type** | **str**| Media type of the entity in the body. Default is JSON.  | [default to JSON]
 **if_match** | **str**| Validator for conditional requests; based on ETag.  | [optional] 
 **if_unmodified_since** | **str**| Validator for conditional requests; based on Last Modified header.  | [optional] 

### Return type

[**GenericThrottlePolicy10**](GenericThrottlePolicy10.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **throttling_policies_advanced_post**
> GenericThrottlePolicy10 throttling_policies_advanced_post(body, content_type)

Add an Advanced level throttle policy

Add an Advanced level throttle policy 

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
api_instance = swagger_client.AdvancedPoliciesApi()
body = swagger_client.GenericThrottlePolicy9() # GenericThrottlePolicy9 | Advanced level policy object that should to be added 
content_type = 'JSON' # str | Media type of the entity in the body. Default is JSON.  (default to JSON)

try: 
    # Add an Advanced level throttle policy
    api_response = api_instance.throttling_policies_advanced_post(body, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvancedPoliciesApi->throttling_policies_advanced_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GenericThrottlePolicy9**](GenericThrottlePolicy9.md)| Advanced level policy object that should to be added  | 
 **content_type** | **str**| Media type of the entity in the body. Default is JSON.  | [default to JSON]

### Return type

[**GenericThrottlePolicy10**](GenericThrottlePolicy10.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

