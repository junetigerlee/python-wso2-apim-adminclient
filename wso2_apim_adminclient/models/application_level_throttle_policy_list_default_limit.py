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


class ApplicationLevelThrottlePolicyListDefaultLimit(object):
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
        'type': 'str',
        'time_unit': 'str',
        'unit_time': 'int'
    }

    attribute_map = {
        'type': 'type',
        'time_unit': 'timeUnit',
        'unit_time': 'unitTime'
    }

    def __init__(self, type=None, time_unit=None, unit_time=None):
        """
        ApplicationLevelThrottlePolicyListDefaultLimit - a model defined in Swagger
        """

        self._type = None
        self._time_unit = None
        self._unit_time = None

        self.type = type
        self.time_unit = time_unit
        self.unit_time = unit_time

    @property
    def type(self):
        """
        Gets the type of this ApplicationLevelThrottlePolicyListDefaultLimit.

        :return: The type of this ApplicationLevelThrottlePolicyListDefaultLimit.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ApplicationLevelThrottlePolicyListDefaultLimit.

        :param type: The type of this ApplicationLevelThrottlePolicyListDefaultLimit.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")
        allowed_values = ["RequestCountLimit", "BandwidthLimit"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def time_unit(self):
        """
        Gets the time_unit of this ApplicationLevelThrottlePolicyListDefaultLimit.

        :return: The time_unit of this ApplicationLevelThrottlePolicyListDefaultLimit.
        :rtype: str
        """
        return self._time_unit

    @time_unit.setter
    def time_unit(self, time_unit):
        """
        Sets the time_unit of this ApplicationLevelThrottlePolicyListDefaultLimit.

        :param time_unit: The time_unit of this ApplicationLevelThrottlePolicyListDefaultLimit.
        :type: str
        """
        if time_unit is None:
            raise ValueError("Invalid value for `time_unit`, must not be `None`")

        self._time_unit = time_unit

    @property
    def unit_time(self):
        """
        Gets the unit_time of this ApplicationLevelThrottlePolicyListDefaultLimit.

        :return: The unit_time of this ApplicationLevelThrottlePolicyListDefaultLimit.
        :rtype: int
        """
        return self._unit_time

    @unit_time.setter
    def unit_time(self, unit_time):
        """
        Sets the unit_time of this ApplicationLevelThrottlePolicyListDefaultLimit.

        :param unit_time: The unit_time of this ApplicationLevelThrottlePolicyListDefaultLimit.
        :type: int
        """
        if unit_time is None:
            raise ValueError("Invalid value for `unit_time`, must not be `None`")

        self._unit_time = unit_time

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
        if not isinstance(other, ApplicationLevelThrottlePolicyListDefaultLimit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
