# swagger_client.SubscriptionPoliciesApi

All URIs are relative to *https://apis.wso2.com/api/am/admin/v0.11*

Method | HTTP request | Description
------------- | ------------- | -------------
[**throttling_policies_subscription_get**](SubscriptionPoliciesApi.md#throttling_policies_subscription_get) | **GET** /throttling/policies/subscription | Get all Subscription level throttle policies
[**throttling_policies_subscription_policy_id_delete**](SubscriptionPoliciesApi.md#throttling_policies_subscription_policy_id_delete) | **DELETE** /throttling/policies/subscription/{policyId} | Delete a Subscription level throttle policy
[**throttling_policies_subscription_policy_id_get**](SubscriptionPoliciesApi.md#throttling_policies_subscription_policy_id_get) | **GET** /throttling/policies/subscription/{policyId} | Retrieve a Subscription Policy
[**throttling_policies_subscription_policy_id_put**](SubscriptionPoliciesApi.md#throttling_policies_subscription_policy_id_put) | **PUT** /throttling/policies/subscription/{policyId} | Update a Subscription level throttle policy
[**throttling_policies_subscription_post**](SubscriptionPoliciesApi.md#throttling_policies_subscription_post) | **POST** /throttling/policies/subscription | Add a Subscription level throttle policy


# **throttling_policies_subscription_get**
> SubscriptionLevelThrottlePolicyList throttling_policies_subscription_get(accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)

Get all Subscription level throttle policies

Get all Subscription level throttle policies 

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
api_instance = swagger_client.SubscriptionPoliciesApi()
accept = 'JSON' # str | Media types acceptable for the response. Default is JSON.  (optional) (default to JSON)
if_none_match = 'if_none_match_example' # str | Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  (optional)
if_modified_since = 'if_modified_since_example' # str | Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource.  (optional)

try: 
    # Get all Subscription level throttle policies
    api_response = api_instance.throttling_policies_subscription_get(accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionPoliciesApi->throttling_policies_subscription_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Media types acceptable for the response. Default is JSON.  | [optional] [default to JSON]
 **if_none_match** | **str**| Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  | [optional] 
 **if_modified_since** | **str**| Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource.  | [optional] 

### Return type

[**SubscriptionLevelThrottlePolicyList**](SubscriptionLevelThrottlePolicyList.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **throttling_policies_subscription_policy_id_delete**
> throttling_policies_subscription_policy_id_delete(policy_id, if_match=if_match, if_unmodified_since=if_unmodified_since)

Delete a Subscription level throttle policy

Delete a Subscription level throttle policy 

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
api_instance = swagger_client.SubscriptionPoliciesApi()
policy_id = 'policy_id_example' # str | Thorttle policy UUID 
if_match = 'if_match_example' # str | Validator for conditional requests; based on ETag.  (optional)
if_unmodified_since = 'if_unmodified_since_example' # str | Validator for conditional requests; based on Last Modified header.  (optional)

try: 
    # Delete a Subscription level throttle policy
    api_instance.throttling_policies_subscription_policy_id_delete(policy_id, if_match=if_match, if_unmodified_since=if_unmodified_since)
except ApiException as e:
    print("Exception when calling SubscriptionPoliciesApi->throttling_policies_subscription_policy_id_delete: %s\n" % e)
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

# **throttling_policies_subscription_policy_id_get**
> GenericThrottlePolicy3 throttling_policies_subscription_policy_id_get(policy_id, if_none_match=if_none_match, if_modified_since=if_modified_since)

Retrieve a Subscription Policy

Retrieve a Subscription Policy providing the policy name. 

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
api_instance = swagger_client.SubscriptionPoliciesApi()
policy_id = 'policy_id_example' # str | Thorttle policy UUID 
if_none_match = 'if_none_match_example' # str | Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  (optional)
if_modified_since = 'if_modified_since_example' # str | Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource.  (optional)

try: 
    # Retrieve a Subscription Policy
    api_response = api_instance.throttling_policies_subscription_policy_id_get(policy_id, if_none_match=if_none_match, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionPoliciesApi->throttling_policies_subscription_policy_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| Thorttle policy UUID  | 
 **if_none_match** | **str**| Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  | [optional] 
 **if_modified_since** | **str**| Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource.  | [optional] 

### Return type

[**GenericThrottlePolicy3**](GenericThrottlePolicy3.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **throttling_policies_subscription_policy_id_put**
> GenericThrottlePolicy3 throttling_policies_subscription_policy_id_put(policy_id, body, content_type, if_match=if_match, if_unmodified_since=if_unmodified_since)

Update a Subscription level throttle policy

Update a Subscription level throttle policy 

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
api_instance = swagger_client.SubscriptionPoliciesApi()
policy_id = 'policy_id_example' # str | Thorttle policy UUID 
body = swagger_client.GenericThrottlePolicy5() # GenericThrottlePolicy5 | Policy object that needs to be modified 
content_type = 'JSON' # str | Media type of the entity in the body. Default is JSON.  (default to JSON)
if_match = 'if_match_example' # str | Validator for conditional requests; based on ETag.  (optional)
if_unmodified_since = 'if_unmodified_since_example' # str | Validator for conditional requests; based on Last Modified header.  (optional)

try: 
    # Update a Subscription level throttle policy
    api_response = api_instance.throttling_policies_subscription_policy_id_put(policy_id, body, content_type, if_match=if_match, if_unmodified_since=if_unmodified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionPoliciesApi->throttling_policies_subscription_policy_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| Thorttle policy UUID  | 
 **body** | [**GenericThrottlePolicy5**](GenericThrottlePolicy5.md)| Policy object that needs to be modified  | 
 **content_type** | **str**| Media type of the entity in the body. Default is JSON.  | [default to JSON]
 **if_match** | **str**| Validator for conditional requests; based on ETag.  | [optional] 
 **if_unmodified_since** | **str**| Validator for conditional requests; based on Last Modified header.  | [optional] 

### Return type

[**GenericThrottlePolicy3**](GenericThrottlePolicy3.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **throttling_policies_subscription_post**
> GenericThrottlePolicy3 throttling_policies_subscription_post(body, content_type)

Add a Subscription level throttle policy

Add a Subscription level throttle policy 

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
api_instance = swagger_client.SubscriptionPoliciesApi()
body = swagger_client.GenericThrottlePolicy4() # GenericThrottlePolicy4 | Subscripion level policy object that should to be added 
content_type = 'JSON' # str | Media type of the entity in the body. Default is JSON.  (default to JSON)

try: 
    # Add a Subscription level throttle policy
    api_response = api_instance.throttling_policies_subscription_post(body, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionPoliciesApi->throttling_policies_subscription_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GenericThrottlePolicy4**](GenericThrottlePolicy4.md)| Subscripion level policy object that should to be added  | 
 **content_type** | **str**| Media type of the entity in the body. Default is JSON.  | [default to JSON]

### Return type

[**GenericThrottlePolicy3**](GenericThrottlePolicy3.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

