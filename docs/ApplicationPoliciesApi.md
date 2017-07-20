# swagger_client.ApplicationPoliciesApi

All URIs are relative to *https://apis.wso2.com/api/am/admin/v0.11*

Method | HTTP request | Description
------------- | ------------- | -------------
[**throttling_policies_application_get**](ApplicationPoliciesApi.md#throttling_policies_application_get) | **GET** /throttling/policies/application | Get all Application level throttle policies
[**throttling_policies_application_policy_id_delete**](ApplicationPoliciesApi.md#throttling_policies_application_policy_id_delete) | **DELETE** /throttling/policies/application/{policyId} | Delete an Application level throttle policy
[**throttling_policies_application_policy_id_get**](ApplicationPoliciesApi.md#throttling_policies_application_policy_id_get) | **GET** /throttling/policies/application/{policyId} | Retrieve an Application Policy
[**throttling_policies_application_policy_id_put**](ApplicationPoliciesApi.md#throttling_policies_application_policy_id_put) | **PUT** /throttling/policies/application/{policyId} | Update an Application level throttle policy
[**throttling_policies_application_post**](ApplicationPoliciesApi.md#throttling_policies_application_post) | **POST** /throttling/policies/application | Add an Application level throttle policy


# **throttling_policies_application_get**
> ApplicationLevelThrottlePolicyList throttling_policies_application_get(accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)

Get all Application level throttle policies

Get all Application level throttle policies 

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
api_instance = swagger_client.ApplicationPoliciesApi()
accept = 'JSON' # str | Media types acceptable for the response. Default is JSON.  (optional) (default to JSON)
if_none_match = 'if_none_match_example' # str | Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  (optional)
if_modified_since = 'if_modified_since_example' # str | Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource.  (optional)

try: 
    # Get all Application level throttle policies
    api_response = api_instance.throttling_policies_application_get(accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationPoliciesApi->throttling_policies_application_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Media types acceptable for the response. Default is JSON.  | [optional] [default to JSON]
 **if_none_match** | **str**| Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  | [optional] 
 **if_modified_since** | **str**| Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource.  | [optional] 

### Return type

[**ApplicationLevelThrottlePolicyList**](ApplicationLevelThrottlePolicyList.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **throttling_policies_application_policy_id_delete**
> throttling_policies_application_policy_id_delete(policy_id, if_match=if_match, if_unmodified_since=if_unmodified_since)

Delete an Application level throttle policy

Delete an Application level throttle policy 

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
api_instance = swagger_client.ApplicationPoliciesApi()
policy_id = 'policy_id_example' # str | Thorttle policy UUID 
if_match = 'if_match_example' # str | Validator for conditional requests; based on ETag.  (optional)
if_unmodified_since = 'if_unmodified_since_example' # str | Validator for conditional requests; based on Last Modified header.  (optional)

try: 
    # Delete an Application level throttle policy
    api_instance.throttling_policies_application_policy_id_delete(policy_id, if_match=if_match, if_unmodified_since=if_unmodified_since)
except ApiException as e:
    print("Exception when calling ApplicationPoliciesApi->throttling_policies_application_policy_id_delete: %s\n" % e)
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

# **throttling_policies_application_policy_id_get**
> GenericThrottlePolicy throttling_policies_application_policy_id_get(policy_id, if_none_match=if_none_match, if_modified_since=if_modified_since)

Retrieve an Application Policy

Retrieve an Application Policy providing the policy name. 

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
api_instance = swagger_client.ApplicationPoliciesApi()
policy_id = 'policy_id_example' # str | Thorttle policy UUID 
if_none_match = 'if_none_match_example' # str | Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  (optional)
if_modified_since = 'if_modified_since_example' # str | Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource.  (optional)

try: 
    # Retrieve an Application Policy
    api_response = api_instance.throttling_policies_application_policy_id_get(policy_id, if_none_match=if_none_match, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationPoliciesApi->throttling_policies_application_policy_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| Thorttle policy UUID  | 
 **if_none_match** | **str**| Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  | [optional] 
 **if_modified_since** | **str**| Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource.  | [optional] 

### Return type

[**GenericThrottlePolicy**](GenericThrottlePolicy.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **throttling_policies_application_policy_id_put**
> GenericThrottlePolicy throttling_policies_application_policy_id_put(policy_id, body, content_type, if_match=if_match, if_unmodified_since=if_unmodified_since)

Update an Application level throttle policy

Update an Application level throttle policy 

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
api_instance = swagger_client.ApplicationPoliciesApi()
policy_id = 'policy_id_example' # str | Thorttle policy UUID 
body = swagger_client.GenericThrottlePolicy2() # GenericThrottlePolicy2 | Policy object that needs to be modified 
content_type = 'JSON' # str | Media type of the entity in the body. Default is JSON.  (default to JSON)
if_match = 'if_match_example' # str | Validator for conditional requests; based on ETag.  (optional)
if_unmodified_since = 'if_unmodified_since_example' # str | Validator for conditional requests; based on Last Modified header.  (optional)

try: 
    # Update an Application level throttle policy
    api_response = api_instance.throttling_policies_application_policy_id_put(policy_id, body, content_type, if_match=if_match, if_unmodified_since=if_unmodified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationPoliciesApi->throttling_policies_application_policy_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| Thorttle policy UUID  | 
 **body** | [**GenericThrottlePolicy2**](GenericThrottlePolicy2.md)| Policy object that needs to be modified  | 
 **content_type** | **str**| Media type of the entity in the body. Default is JSON.  | [default to JSON]
 **if_match** | **str**| Validator for conditional requests; based on ETag.  | [optional] 
 **if_unmodified_since** | **str**| Validator for conditional requests; based on Last Modified header.  | [optional] 

### Return type

[**GenericThrottlePolicy**](GenericThrottlePolicy.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **throttling_policies_application_post**
> GenericThrottlePolicy throttling_policies_application_post(body, content_type)

Add an Application level throttle policy

Add an Application level throttle policy 

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
api_instance = swagger_client.ApplicationPoliciesApi()
body = swagger_client.GenericThrottlePolicy1() # GenericThrottlePolicy1 | Application level policy object that should to be added 
content_type = 'JSON' # str | Media type of the entity in the body. Default is JSON.  (default to JSON)

try: 
    # Add an Application level throttle policy
    api_response = api_instance.throttling_policies_application_post(body, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationPoliciesApi->throttling_policies_application_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GenericThrottlePolicy1**](GenericThrottlePolicy1.md)| Application level policy object that should to be added  | 
 **content_type** | **str**| Media type of the entity in the body. Default is JSON.  | [default to JSON]

### Return type

[**GenericThrottlePolicy**](GenericThrottlePolicy.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

