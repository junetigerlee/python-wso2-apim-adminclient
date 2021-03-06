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


class IPCondition(object):
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
        'invert_condition': 'bool',
        'ip_condition_type': 'str',
        'specific_ip': 'str',
        'starting_ip': 'str',
        'ending_ip': 'str'
    }

    attribute_map = {
        'type': 'type',
        'invert_condition': 'invertCondition',
        'ip_condition_type': 'ipConditionType',
        'specific_ip': 'specificIP',
        'starting_ip': 'startingIP',
        'ending_ip': 'endingIP'
    }

    def __init__(self, type=None, invert_condition=False, ip_condition_type=None, specific_ip=None, starting_ip=None, ending_ip=None):
        """
        IPCondition - a model defined in Swagger
        """

        self._type = None
        self._invert_condition = None
        self._ip_condition_type = None
        self._specific_ip = None
        self._starting_ip = None
        self._ending_ip = None

        self.type = type
        if invert_condition is not None:
          self.invert_condition = invert_condition
        if ip_condition_type is not None:
          self.ip_condition_type = ip_condition_type
        if specific_ip is not None:
          self.specific_ip = specific_ip
        if starting_ip is not None:
          self.starting_ip = starting_ip
        if ending_ip is not None:
          self.ending_ip = ending_ip

    @property
    def type(self):
        """
        Gets the type of this IPCondition.

        :return: The type of this IPCondition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this IPCondition.

        :param type: The type of this IPCondition.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")
        allowed_values = ["HeaderCondition", "IPCondition", "JWTClaimsCondition", "QueryParameterCondition"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def invert_condition(self):
        """
        Gets the invert_condition of this IPCondition.

        :return: The invert_condition of this IPCondition.
        :rtype: bool
        """
        return self._invert_condition

    @invert_condition.setter
    def invert_condition(self, invert_condition):
        """
        Sets the invert_condition of this IPCondition.

        :param invert_condition: The invert_condition of this IPCondition.
        :type: bool
        """

        self._invert_condition = invert_condition

    @property
    def ip_condition_type(self):
        """
        Gets the ip_condition_type of this IPCondition.

        :return: The ip_condition_type of this IPCondition.
        :rtype: str
        """
        return self._ip_condition_type

    @ip_condition_type.setter
    def ip_condition_type(self, ip_condition_type):
        """
        Sets the ip_condition_type of this IPCondition.

        :param ip_condition_type: The ip_condition_type of this IPCondition.
        :type: str
        """
        allowed_values = ["IPRange", "IPSpecific"]
        if ip_condition_type not in allowed_values:
            raise ValueError(
                "Invalid value for `ip_condition_type` ({0}), must be one of {1}"
                .format(ip_condition_type, allowed_values)
            )

        self._ip_condition_type = ip_condition_type

    @property
    def specific_ip(self):
        """
        Gets the specific_ip of this IPCondition.

        :return: The specific_ip of this IPCondition.
        :rtype: str
        """
        return self._specific_ip

    @specific_ip.setter
    def specific_ip(self, specific_ip):
        """
        Sets the specific_ip of this IPCondition.

        :param specific_ip: The specific_ip of this IPCondition.
        :type: str
        """

        self._specific_ip = specific_ip

    @property
    def starting_ip(self):
        """
        Gets the starting_ip of this IPCondition.

        :return: The starting_ip of this IPCondition.
        :rtype: str
        """
        return self._starting_ip

    @starting_ip.setter
    def starting_ip(self, starting_ip):
        """
        Sets the starting_ip of this IPCondition.

        :param starting_ip: The starting_ip of this IPCondition.
        :type: str
        """

        self._starting_ip = starting_ip

    @property
    def ending_ip(self):
        """
        Gets the ending_ip of this IPCondition.

        :return: The ending_ip of this IPCondition.
        :rtype: str
        """
        return self._ending_ip

    @ending_ip.setter
    def ending_ip(self, ending_ip):
        """
        Sets the ending_ip of this IPCondition.

        :param ending_ip: The ending_ip of this IPCondition.
        :type: str
        """

        self._ending_ip = ending_ip

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
        if not isinstance(other, IPCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
