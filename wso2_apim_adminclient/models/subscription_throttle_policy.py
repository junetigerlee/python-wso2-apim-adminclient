# coding: utf-8

"""
    WSO2 API Manager - Admin

    This document specifies a **RESTful API** for WSO2 **API Manager** - Admin Portal.  It is written with [swagger 2](http://swagger.io/). 

    OpenAPI spec version: 0.11.0
    Contact: architecture@wso2.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SubscriptionThrottlePolicy(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'policy_id': 'str',
        'policy_name': 'str',
        'display_name': 'str',
        'description': 'str',
        'is_deployed': 'bool',
        'default_limit': 'ApplicationLevelThrottlePolicyListDefaultLimit',
        'rate_limit_count': 'int',
        'rate_limit_time_unit': 'str',
        'custom_attributes': 'list[NameValuePair]',
        'stop_on_quota_reach': 'bool',
        'billing_plan': 'str'
    }

    attribute_map = {
        'policy_id': 'policyId',
        'policy_name': 'policyName',
        'display_name': 'displayName',
        'description': 'description',
        'is_deployed': 'isDeployed',
        'default_limit': 'defaultLimit',
        'rate_limit_count': 'rateLimitCount',
        'rate_limit_time_unit': 'rateLimitTimeUnit',
        'custom_attributes': 'customAttributes',
        'stop_on_quota_reach': 'stopOnQuotaReach',
        'billing_plan': 'billingPlan'
    }

    def __init__(self, policy_id=None, policy_name=None, display_name=None, description=None, is_deployed=False, default_limit=None, rate_limit_count=None, rate_limit_time_unit=None, custom_attributes=None, stop_on_quota_reach=False, billing_plan=None):
        """
        SubscriptionThrottlePolicy - a model defined in Swagger
        """

        self._policy_id = None
        self._policy_name = None
        self._display_name = None
        self._description = None
        self._is_deployed = None
        self._default_limit = None
        self._rate_limit_count = None
        self._rate_limit_time_unit = None
        self._custom_attributes = None
        self._stop_on_quota_reach = None
        self._billing_plan = None

        if policy_id is not None:
          self.policy_id = policy_id
        self.policy_name = policy_name
        if display_name is not None:
          self.display_name = display_name
        if description is not None:
          self.description = description
        if is_deployed is not None:
          self.is_deployed = is_deployed
        if default_limit is not None:
          self.default_limit = default_limit
        if rate_limit_count is not None:
          self.rate_limit_count = rate_limit_count
        if rate_limit_time_unit is not None:
          self.rate_limit_time_unit = rate_limit_time_unit
        if custom_attributes is not None:
          self.custom_attributes = custom_attributes
        if stop_on_quota_reach is not None:
          self.stop_on_quota_reach = stop_on_quota_reach
        if billing_plan is not None:
          self.billing_plan = billing_plan

    @property
    def policy_id(self):
        """
        Gets the policy_id of this SubscriptionThrottlePolicy.

        :return: The policy_id of this SubscriptionThrottlePolicy.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """
        Sets the policy_id of this SubscriptionThrottlePolicy.

        :param policy_id: The policy_id of this SubscriptionThrottlePolicy.
        :type: str
        """

        self._policy_id = policy_id

    @property
    def policy_name(self):
        """
        Gets the policy_name of this SubscriptionThrottlePolicy.

        :return: The policy_name of this SubscriptionThrottlePolicy.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """
        Sets the policy_name of this SubscriptionThrottlePolicy.

        :param policy_name: The policy_name of this SubscriptionThrottlePolicy.
        :type: str
        """
        if policy_name is None:
            raise ValueError("Invalid value for `policy_name`, must not be `None`")

        self._policy_name = policy_name

    @property
    def display_name(self):
        """
        Gets the display_name of this SubscriptionThrottlePolicy.

        :return: The display_name of this SubscriptionThrottlePolicy.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SubscriptionThrottlePolicy.

        :param display_name: The display_name of this SubscriptionThrottlePolicy.
        :type: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this SubscriptionThrottlePolicy.

        :return: The description of this SubscriptionThrottlePolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SubscriptionThrottlePolicy.

        :param description: The description of this SubscriptionThrottlePolicy.
        :type: str
        """

        self._description = description

    @property
    def is_deployed(self):
        """
        Gets the is_deployed of this SubscriptionThrottlePolicy.

        :return: The is_deployed of this SubscriptionThrottlePolicy.
        :rtype: bool
        """
        return self._is_deployed

    @is_deployed.setter
    def is_deployed(self, is_deployed):
        """
        Sets the is_deployed of this SubscriptionThrottlePolicy.

        :param is_deployed: The is_deployed of this SubscriptionThrottlePolicy.
        :type: bool
        """

        self._is_deployed = is_deployed

    @property
    def default_limit(self):
        """
        Gets the default_limit of this SubscriptionThrottlePolicy.

        :return: The default_limit of this SubscriptionThrottlePolicy.
        :rtype: ApplicationLevelThrottlePolicyListDefaultLimit
        """
        return self._default_limit

    @default_limit.setter
    def default_limit(self, default_limit):
        """
        Sets the default_limit of this SubscriptionThrottlePolicy.

        :param default_limit: The default_limit of this SubscriptionThrottlePolicy.
        :type: ApplicationLevelThrottlePolicyListDefaultLimit
        """

        self._default_limit = default_limit

    @property
    def rate_limit_count(self):
        """
        Gets the rate_limit_count of this SubscriptionThrottlePolicy.

        :return: The rate_limit_count of this SubscriptionThrottlePolicy.
        :rtype: int
        """
        return self._rate_limit_count

    @rate_limit_count.setter
    def rate_limit_count(self, rate_limit_count):
        """
        Sets the rate_limit_count of this SubscriptionThrottlePolicy.

        :param rate_limit_count: The rate_limit_count of this SubscriptionThrottlePolicy.
        :type: int
        """

        self._rate_limit_count = rate_limit_count

    @property
    def rate_limit_time_unit(self):
        """
        Gets the rate_limit_time_unit of this SubscriptionThrottlePolicy.

        :return: The rate_limit_time_unit of this SubscriptionThrottlePolicy.
        :rtype: str
        """
        return self._rate_limit_time_unit

    @rate_limit_time_unit.setter
    def rate_limit_time_unit(self, rate_limit_time_unit):
        """
        Sets the rate_limit_time_unit of this SubscriptionThrottlePolicy.

        :param rate_limit_time_unit: The rate_limit_time_unit of this SubscriptionThrottlePolicy.
        :type: str
        """

        self._rate_limit_time_unit = rate_limit_time_unit

    @property
    def custom_attributes(self):
        """
        Gets the custom_attributes of this SubscriptionThrottlePolicy.
        Custom attributes added to the Subscription Throttle policy 

        :return: The custom_attributes of this SubscriptionThrottlePolicy.
        :rtype: list[NameValuePair]
        """
        return self._custom_attributes

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        """
        Sets the custom_attributes of this SubscriptionThrottlePolicy.
        Custom attributes added to the Subscription Throttle policy 

        :param custom_attributes: The custom_attributes of this SubscriptionThrottlePolicy.
        :type: list[NameValuePair]
        """

        self._custom_attributes = custom_attributes

    @property
    def stop_on_quota_reach(self):
        """
        Gets the stop_on_quota_reach of this SubscriptionThrottlePolicy.

        :return: The stop_on_quota_reach of this SubscriptionThrottlePolicy.
        :rtype: bool
        """
        return self._stop_on_quota_reach

    @stop_on_quota_reach.setter
    def stop_on_quota_reach(self, stop_on_quota_reach):
        """
        Sets the stop_on_quota_reach of this SubscriptionThrottlePolicy.

        :param stop_on_quota_reach: The stop_on_quota_reach of this SubscriptionThrottlePolicy.
        :type: bool
        """

        self._stop_on_quota_reach = stop_on_quota_reach

    @property
    def billing_plan(self):
        """
        Gets the billing_plan of this SubscriptionThrottlePolicy.

        :return: The billing_plan of this SubscriptionThrottlePolicy.
        :rtype: str
        """
        return self._billing_plan

    @billing_plan.setter
    def billing_plan(self, billing_plan):
        """
        Sets the billing_plan of this SubscriptionThrottlePolicy.

        :param billing_plan: The billing_plan of this SubscriptionThrottlePolicy.
        :type: str
        """

        self._billing_plan = billing_plan

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, SubscriptionThrottlePolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
