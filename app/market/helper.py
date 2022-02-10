"""
 * File Name: helper.py
 * Description: Get response from bittrex API
 * Author: Dineshkumar Dhayalan
 * Author Email: dineshkumar.dhayalan@ltts.com
"""
from app.CommonLib import helper

import requests


class BittrexRequests:
    """
    BittrexRequests class: call bittrex api and get response object
    """

    def __init__(self, url=None):
        self.bittrex_api = url

    def get_data(self, payload={}):
        """
        Fetch response from bittrex API and also handle API exception
        :param payload: sent params to bittrex api if required
        :return: response object (json)
        """
        try:
            # call bittrex API
            api_resp = requests.get(self.bittrex_api, params=payload)
            # validate status code
            if api_resp.status_code != 200:
                details = "Url is missmatch"
                return helper.response_json('failed', {}, details, 500)
            # bittrex api response
            resp = api_resp.json()
            if resp['success'] is False:
                details = "Bittrex data failed - Exception occurred " + resp['message']
                return helper.response_json('failed', {}, details, 500)
            return resp
        except Exception as e:
            details = "Unable to connect bittrex api - Exception occurred " + str(e)
            return helper.response_json('failed', {}, details, 500)
