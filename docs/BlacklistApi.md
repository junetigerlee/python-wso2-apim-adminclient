# swagger_client.BlacklistApi

All URIs are relative to *https://apis.wso2.com/api/am/admin/v0.11*

Method | HTTP request | Description
------------- | ------------- | -------------
[**throttling_blacklist_condition_id_delete**](BlacklistApi.md#throttling_blacklist_condition_id_delete) | **DELETE** /throttling/blacklist/{conditionId} | Delete a Blocking condition
[**throttling_blacklist_condition_id_get**](BlacklistApi.md#throttling_blacklist_condition_id_get) | **GET** /throttling/blacklist/{conditionId} | Retrieve a Blocking Condition
[**throttling_blacklist_get**](BlacklistApi.md#throttling_blacklist_get) | **GET** /throttling/blacklist | Get all blocking condtions
[**throttling_blacklist_post**](BlacklistApi.md#throttling_blacklist_post) | **POST** /throttling/blacklist | Add a Blocking condition


# **throttling_blacklist_condition_id_delete**
> throttling_blacklist_condition_id_delete(condition_id, if_match=if_match, if_unmodified_since=if_unmodified_since)

Delete a Blocking condition

Delete a Blocking condition 

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
api_instance = swagger_client.BlacklistApi()
condition_id = 'condition_id_example' # str | Blocking condition identifier  
if_match = 'if_match_example' # str | Validator for conditional requests; based on ETag.  (optional)
if_unmodified_since = 'if_unmodified_since_example' # str | Validator for conditional requests; based on Last Modified header.  (optional)

try: 
    # Delete a Blocking condition
    api_instance.throttling_blacklist_condition_id_delete(condition_id, if_match=if_match, if_unmodified_since=if_unmodified_since)
except ApiException as e:
    print("Exception when calling BlacklistApi->throttling_blacklist_condition_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **condition_id** | **str**| Blocking condition identifier   | 
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

# **throttling_blacklist_condition_id_get**
> BlockingConditions throttling_blacklist_condition_id_get(condition_id, if_none_match=if_none_match, if_modified_since=if_modified_since)

Retrieve a Blocking Condition

Retrieve a Blocking Condition providing the condition Id 

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
api_instance = swagger_client.BlacklistApi()
condition_id = 'condition_id_example' # str | Blocking condition identifier  
if_none_match = 'if_none_match_example' # str | Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  (optional)
if_modified_since = 'if_modified_since_example' # str | Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource.  (optional)

try: 
    # Retrieve a Blocking Condition
    api_response = api_instance.throttling_blacklist_condition_id_get(condition_id, if_none_match=if_none_match, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlacklistApi->throttling_blacklist_condition_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **condition_id** | **str**| Blocking condition identifier   | 
 **if_none_match** | **str**| Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  | [optional] 
 **if_modified_since** | **str**| Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource.  | [optional] 

### Return type

[**BlockingConditions**](BlockingConditions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **throttling_blacklist_get**
> BlockingConditionsList throttling_blacklist_get(accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)

Get all blocking condtions

Get all blocking condtions 

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
api_instance = swagger_client.BlacklistApi()
accept = 'JSON' # str | Media types acceptable for the response. Default is JSON.  (optional) (default to JSON)
if_none_match = 'if_none_match_example' # str | Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  (optional)
if_modified_since = 'if_modified_since_example' # str | Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource.  (optional)

try: 
    # Get all blocking condtions
    api_response = api_instance.throttling_blacklist_get(accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlacklistApi->throttling_blacklist_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Media types acceptable for the response. Default is JSON.  | [optional] [default to JSON]
 **if_none_match** | **str**| Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  | [optional] 
 **if_modified_since** | **str**| Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource.  | [optional] 

### Return type

[**BlockingConditionsList**](BlockingConditionsList.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **throttling_blacklist_post**
> BlockingConditions throttling_blacklist_post(body, content_type)

Add a Blocking condition

Add a Blocking condition 

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
api_instance = swagger_client.BlacklistApi()
body = swagger_client.BlockingConditions1() # BlockingConditions1 | Blocking condition object that should to be added 
content_type = 'JSON' # str | Media type of the entity in the body. Default is JSON.  (default to JSON)

try: 
    # Add a Blocking condition
    api_response = api_instance.throttling_blacklist_post(body, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlacklistApi->throttling_blacklist_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BlockingConditions1**](BlockingConditions1.md)| Blocking condition object that should to be added  | 
 **content_type** | **str**| Media type of the entity in the body. Default is JSON.  | [default to JSON]

### Return type

[**BlockingConditions**](BlockingConditions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

