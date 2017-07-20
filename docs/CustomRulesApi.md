# swagger_client.CustomRulesApi

All URIs are relative to *https://apis.wso2.com/api/am/admin/v0.11*

Method | HTTP request | Description
------------- | ------------- | -------------
[**throttling_policies_custom_get**](CustomRulesApi.md#throttling_policies_custom_get) | **GET** /throttling/policies/custom | Get all Custom Rules
[**throttling_policies_custom_post**](CustomRulesApi.md#throttling_policies_custom_post) | **POST** /throttling/policies/custom | Add a Custom Rule
[**throttling_policies_custom_rule_id_delete**](CustomRulesApi.md#throttling_policies_custom_rule_id_delete) | **DELETE** /throttling/policies/custom/{ruleId} | Delete a Custom Rule
[**throttling_policies_custom_rule_id_get**](CustomRulesApi.md#throttling_policies_custom_rule_id_get) | **GET** /throttling/policies/custom/{ruleId} | Retrieve a Custom Rule
[**throttling_policies_custom_rule_id_put**](CustomRulesApi.md#throttling_policies_custom_rule_id_put) | **PUT** /throttling/policies/custom/{ruleId} | Update a Custom Rule


# **throttling_policies_custom_get**
> CustomRuleList throttling_policies_custom_get(accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)

Get all Custom Rules

Get all Custom Rules 

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
api_instance = swagger_client.CustomRulesApi()
accept = 'JSON' # str | Media types acceptable for the response. Default is JSON.  (optional) (default to JSON)
if_none_match = 'if_none_match_example' # str | Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  (optional)
if_modified_since = 'if_modified_since_example' # str | Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource.  (optional)

try: 
    # Get all Custom Rules
    api_response = api_instance.throttling_policies_custom_get(accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomRulesApi->throttling_policies_custom_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Media types acceptable for the response. Default is JSON.  | [optional] [default to JSON]
 **if_none_match** | **str**| Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  | [optional] 
 **if_modified_since** | **str**| Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource.  | [optional] 

### Return type

[**CustomRuleList**](CustomRuleList.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **throttling_policies_custom_post**
> GenericThrottlePolicy6 throttling_policies_custom_post(body, content_type)

Add a Custom Rule

Add a Custom Rule 

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
api_instance = swagger_client.CustomRulesApi()
body = swagger_client.GenericThrottlePolicy7() # GenericThrottlePolicy7 | Custom Rule object that should to be added 
content_type = 'JSON' # str | Media type of the entity in the body. Default is JSON.  (default to JSON)

try: 
    # Add a Custom Rule
    api_response = api_instance.throttling_policies_custom_post(body, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomRulesApi->throttling_policies_custom_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GenericThrottlePolicy7**](GenericThrottlePolicy7.md)| Custom Rule object that should to be added  | 
 **content_type** | **str**| Media type of the entity in the body. Default is JSON.  | [default to JSON]

### Return type

[**GenericThrottlePolicy6**](GenericThrottlePolicy6.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **throttling_policies_custom_rule_id_delete**
> throttling_policies_custom_rule_id_delete(rule_id, if_match=if_match, if_unmodified_since=if_unmodified_since)

Delete a Custom Rule

Delete a Custom Rule 

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
api_instance = swagger_client.CustomRulesApi()
rule_id = 'rule_id_example' # str | Custom rule UUID 
if_match = 'if_match_example' # str | Validator for conditional requests; based on ETag.  (optional)
if_unmodified_since = 'if_unmodified_since_example' # str | Validator for conditional requests; based on Last Modified header.  (optional)

try: 
    # Delete a Custom Rule
    api_instance.throttling_policies_custom_rule_id_delete(rule_id, if_match=if_match, if_unmodified_since=if_unmodified_since)
except ApiException as e:
    print("Exception when calling CustomRulesApi->throttling_policies_custom_rule_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| Custom rule UUID  | 
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

# **throttling_policies_custom_rule_id_get**
> GenericThrottlePolicy6 throttling_policies_custom_rule_id_get(rule_id, if_none_match=if_none_match, if_modified_since=if_modified_since)

Retrieve a Custom Rule

Retrieve a Custom Rule providing the policy name. 

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
api_instance = swagger_client.CustomRulesApi()
rule_id = 'rule_id_example' # str | Custom rule UUID 
if_none_match = 'if_none_match_example' # str | Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  (optional)
if_modified_since = 'if_modified_since_example' # str | Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource.  (optional)

try: 
    # Retrieve a Custom Rule
    api_response = api_instance.throttling_policies_custom_rule_id_get(rule_id, if_none_match=if_none_match, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomRulesApi->throttling_policies_custom_rule_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| Custom rule UUID  | 
 **if_none_match** | **str**| Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  | [optional] 
 **if_modified_since** | **str**| Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource.  | [optional] 

### Return type

[**GenericThrottlePolicy6**](GenericThrottlePolicy6.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **throttling_policies_custom_rule_id_put**
> GenericThrottlePolicy6 throttling_policies_custom_rule_id_put(rule_id, body, content_type, if_match=if_match, if_unmodified_since=if_unmodified_since)

Update a Custom Rule

Update a Custom Rule 

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
api_instance = swagger_client.CustomRulesApi()
rule_id = 'rule_id_example' # str | Custom rule UUID 
body = swagger_client.GenericThrottlePolicy8() # GenericThrottlePolicy8 | Policy object that needs to be modified 
content_type = 'JSON' # str | Media type of the entity in the body. Default is JSON.  (default to JSON)
if_match = 'if_match_example' # str | Validator for conditional requests; based on ETag.  (optional)
if_unmodified_since = 'if_unmodified_since_example' # str | Validator for conditional requests; based on Last Modified header.  (optional)

try: 
    # Update a Custom Rule
    api_response = api_instance.throttling_policies_custom_rule_id_put(rule_id, body, content_type, if_match=if_match, if_unmodified_since=if_unmodified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomRulesApi->throttling_policies_custom_rule_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| Custom rule UUID  | 
 **body** | [**GenericThrottlePolicy8**](GenericThrottlePolicy8.md)| Policy object that needs to be modified  | 
 **content_type** | **str**| Media type of the entity in the body. Default is JSON.  | [default to JSON]
 **if_match** | **str**| Validator for conditional requests; based on ETag.  | [optional] 
 **if_unmodified_since** | **str**| Validator for conditional requests; based on Last Modified header.  | [optional] 

### Return type

[**GenericThrottlePolicy6**](GenericThrottlePolicy6.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

