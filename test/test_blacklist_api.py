# coding: utf-8

"""
    WSO2 API Manager - Admin

    This document specifies a **RESTful API** for WSO2 **API Manager** - Admin Portal.  It is written with [swagger 2](http://swagger.io/). 

    OpenAPI spec version: 0.11.0
    Contact: architecture@wso2.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import wso2_apim_adminclient
from wso2_apim_adminclient.rest import ApiException
from wso2_apim_adminclient.apis.blacklist_api import BlacklistApi


class TestBlacklistApi(unittest.TestCase):
    """ BlacklistApi unit test stubs """

    def setUp(self):
        self.api = wso2_apim_adminclient.apis.blacklist_api.BlacklistApi()

    def tearDown(self):
        pass

    def test_throttling_blacklist_condition_id_delete(self):
        """
        Test case for throttling_blacklist_condition_id_delete

        Delete a Blocking condition
        """
        pass

    def test_throttling_blacklist_condition_id_get(self):
        """
        Test case for throttling_blacklist_condition_id_get

        Retrieve a Blocking Condition
        """
        pass

    def test_throttling_blacklist_get(self):
        """
        Test case for throttling_blacklist_get

        Get all blocking condtions
        """
        pass

    def test_throttling_blacklist_post(self):
        """
        Test case for throttling_blacklist_post

        Add a Blocking condition
        """
        pass


if __name__ == '__main__':
    unittest.main()
