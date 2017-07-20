# SubscriptionThrottlePolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_id** | **str** |  | [optional] 
**policy_name** | **str** |  | 
**display_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**is_deployed** | **bool** |  | [optional] [default to False]
**default_limit** | [**ApplicationLevelThrottlePolicyListDefaultLimit**](ApplicationLevelThrottlePolicyListDefaultLimit.md) |  | [optional] 
**rate_limit_count** | **int** |  | [optional] 
**rate_limit_time_unit** | **str** |  | [optional] 
**custom_attributes** | [**list[NameValuePair]**](NameValuePair.md) | Custom attributes added to the Subscription Throttle policy  | [optional] 
**stop_on_quota_reach** | **bool** |  | [optional] [default to False]
**billing_plan** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


