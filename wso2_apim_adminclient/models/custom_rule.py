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


class CustomRule(object):
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
        'siddhi_query': 'str',
        'key_template': 'str'
    }

    attribute_map = {
        'policy_id': 'policyId',
        'policy_name': 'policyName',
        'display_name': 'displayName',
        'description': 'description',
        'is_deployed': 'isDeployed',
        'siddhi_query': 'siddhiQuery',
        'key_template': 'keyTemplate'
    }

    def __init__(self, policy_id=None, policy_name=None, display_name=None, description=None, is_deployed=False, siddhi_query=None, key_template=None):
        """
        CustomRule - a model defined in Swagger
        """

        self._policy_id = None
        self._policy_name = None
        self._display_name = None
        self._description = None
        self._is_deployed = None
        self._siddhi_query = None
        self._key_template = None

        if policy_id is not None:
          self.policy_id = policy_id
        self.policy_name = policy_name
        if display_name is not None:
          self.display_name = display_name
        if description is not None:
          self.description = description
        if is_deployed is not None:
          self.is_deployed = is_deployed
        if siddhi_query is not None:
          self.siddhi_query = siddhi_query
        if key_template is not None:
          self.key_template = key_template

    @property
    def policy_id(self):
        """
        Gets the policy_id of this CustomRule.

        :return: The policy_id of this CustomRule.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """
        Sets the policy_id of this CustomRule.

        :param policy_id: The policy_id of this CustomRule.
        :type: str
        """

        self._policy_id = policy_id

    @property
    def policy_name(self):
        """
        Gets the policy_name of this CustomRule.

        :return: The policy_name of this CustomRule.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """
        Sets the policy_name of this CustomRule.

        :param policy_name: The policy_name of this CustomRule.
        :type: str
        """
        if policy_name is None:
            raise ValueError("Invalid value for `policy_name`, must not be `None`")

        self._policy_name = policy_name

    @property
    def display_name(self):
        """
        Gets the display_name of this CustomRule.

        :return: The display_name of this CustomRule.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CustomRule.

        :param display_name: The display_name of this CustomRule.
        :type: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CustomRule.

        :return: The description of this CustomRule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CustomRule.

        :param description: The description of this CustomRule.
        :type: str
        """

        self._description = description

    @property
    def is_deployed(self):
        """
        Gets the is_deployed of this CustomRule.

        :return: The is_deployed of this CustomRule.
        :rtype: bool
        """
        return self._is_deployed

    @is_deployed.setter
    def is_deployed(self, is_deployed):
        """
        Sets the is_deployed of this CustomRule.

        :param is_deployed: The is_deployed of this CustomRule.
        :type: bool
        """

        self._is_deployed = is_deployed

    @property
    def siddhi_query(self):
        """
        Gets the siddhi_query of this CustomRule.

        :return: The siddhi_query of this CustomRule.
        :rtype: str
        """
        return self._siddhi_query

    @siddhi_query.setter
    def siddhi_query(self, siddhi_query):
        """
        Sets the siddhi_query of this CustomRule.

        :param siddhi_query: The siddhi_query of this CustomRule.
        :type: str
        """

        self._siddhi_query = siddhi_query

    @property
    def key_template(self):
        """
        Gets the key_template of this CustomRule.

        :return: The key_template of this CustomRule.
        :rtype: str
        """
        return self._key_template

    @key_template.setter
    def key_template(self, key_template):
        """
        Sets the key_template of this CustomRule.

        :param key_template: The key_template of this CustomRule.
        :type: str
        """

        self._key_template = key_template

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
        if not isinstance(other, CustomRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
