"""
 * File Name: views.py
 * Description: Used to get the last 24 hour summary of all active markets and specific market.
 * Author: Dineshkumar Dhayalan
 * Author Email: dineshkumar.dhayalan@ltts.com
"""
from app.CommonLib import helper
from app.CommonLib.security_helper import TokenOperations as security
from app.market.helper import BittrexRequests
from app import BITTREX_MARKET_SUMMARIES_API, BITTREX_MARKET_SUMMARY_API


@security.token_required
def get_all_market_summaries():
    """
    Used to get the last 24 hour summary of all active markets.
    :return: response object (json)
    """
    try:
        resp = BittrexRequests(BITTREX_MARKET_SUMMARIES_API).get_data()
        # response - failed
        if resp.get('status') is not None:
            return helper.response_jsonify(resp)

        return helper.response('success', {"items": resp['result']}, "fetched all market summaries successfully", 200)
    except Exception as e:
        details = "Market summaries api unable to read data - Exception occurred " + str(e)
        return helper.response('failed', {}, details, 500)


@security.token_required
def get_market_summary(market):
    """
    Used to get the last 24 hour summary of a specific market.
    :param market: market name like btc-ltc pass to payload
    :return: response object (json)
    """
    try:
        payload = {"market": market}
        resp = BittrexRequests(BITTREX_MARKET_SUMMARY_API).get_data(payload=payload)
        # response - failed
        if resp.get('status') is not None:
            return helper.response_jsonify(resp)

        return helper.response('success', {"items": resp['result']}, "fetched market summary successfully", 200)
    except Exception as e:
        details = "Market summary api unable to read data - Exception occurred " + str(e)
        return helper.response('failed', {}, details, 500)
