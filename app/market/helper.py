from app.CommonLib import helper

import requests


class BittrexRequests:

    def __init__(self, url=None):
        self.bittrex_api = url

    def get_data(self, payload={}):
        try:
            api_resp = requests.get(self.bittrex_api, params=payload)
            if api_resp.status_code != 200:
                details = "API URL is missmatch/ query param failed"
                return helper.response_json('failed', {}, details, 500)
            resp = api_resp.json()
            if resp['success'] is False:
                details = "Bittrex data fetching failed - Exception occurred " + resp['message']
                return helper.response_json('failed', {}, details, 500)
            return resp
        except Exception as e:
            details = "Unable to connect bittrex api - Exception occurred " + str(e)
            return helper.response_json('failed', {}, details, 500)
