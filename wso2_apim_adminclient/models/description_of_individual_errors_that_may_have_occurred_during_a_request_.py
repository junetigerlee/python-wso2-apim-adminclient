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


class DescriptionOfIndividualErrorsThatMayHaveOccurredDuringARequest_(object):
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
        'code': 'str',
        'message': 'str'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message'
    }

    def __init__(self, code=None, message=None):
        """
        DescriptionOfIndividualErrorsThatMayHaveOccurredDuringARequest_ - a model defined in Swagger
        """

        self._code = None
        self._message = None

        self.code = code
        self.message = message

    @property
    def code(self):
        """
        Gets the code of this DescriptionOfIndividualErrorsThatMayHaveOccurredDuringARequest_.

        :return: The code of this DescriptionOfIndividualErrorsThatMayHaveOccurredDuringARequest_.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this DescriptionOfIndividualErrorsThatMayHaveOccurredDuringARequest_.

        :param code: The code of this DescriptionOfIndividualErrorsThatMayHaveOccurredDuringARequest_.
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")

        self._code = code

    @property
    def message(self):
        """
        Gets the message of this DescriptionOfIndividualErrorsThatMayHaveOccurredDuringARequest_.
        Description about individual errors occurred 

        :return: The message of this DescriptionOfIndividualErrorsThatMayHaveOccurredDuringARequest_.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this DescriptionOfIndividualErrorsThatMayHaveOccurredDuringARequest_.
        Description about individual errors occurred 

        :param message: The message of this DescriptionOfIndividualErrorsThatMayHaveOccurredDuringARequest_.
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")

        self._message = message

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
        if not isinstance(other, DescriptionOfIndividualErrorsThatMayHaveOccurredDuringARequest_):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
