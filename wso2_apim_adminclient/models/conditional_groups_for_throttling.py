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


class ConditionalGroupsForThrottling(object):
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
        'description': 'str',
        'conditions': 'list[ConditionsUsedForThrottling]',
        'limit': 'ApplicationLevelThrottlePolicyListDefaultLimit'
    }

    attribute_map = {
        'description': 'description',
        'conditions': 'conditions',
        'limit': 'limit'
    }

    def __init__(self, description=None, conditions=None, limit=None):
        """
        ConditionalGroupsForThrottling - a model defined in Swagger
        """

        self._description = None
        self._conditions = None
        self._limit = None

        if description is not None:
          self.description = description
        self.conditions = conditions
        if limit is not None:
          self.limit = limit

    @property
    def description(self):
        """
        Gets the description of this ConditionalGroupsForThrottling.

        :return: The description of this ConditionalGroupsForThrottling.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ConditionalGroupsForThrottling.

        :param description: The description of this ConditionalGroupsForThrottling.
        :type: str
        """

        self._description = description

    @property
    def conditions(self):
        """
        Gets the conditions of this ConditionalGroupsForThrottling.

        :return: The conditions of this ConditionalGroupsForThrottling.
        :rtype: list[ConditionsUsedForThrottling]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """
        Sets the conditions of this ConditionalGroupsForThrottling.

        :param conditions: The conditions of this ConditionalGroupsForThrottling.
        :type: list[ConditionsUsedForThrottling]
        """
        if conditions is None:
            raise ValueError("Invalid value for `conditions`, must not be `None`")

        self._conditions = conditions

    @property
    def limit(self):
        """
        Gets the limit of this ConditionalGroupsForThrottling.

        :return: The limit of this ConditionalGroupsForThrottling.
        :rtype: ApplicationLevelThrottlePolicyListDefaultLimit
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this ConditionalGroupsForThrottling.

        :param limit: The limit of this ConditionalGroupsForThrottling.
        :type: ApplicationLevelThrottlePolicyListDefaultLimit
        """

        self._limit = limit

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
        if not isinstance(other, ConditionalGroupsForThrottling):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
