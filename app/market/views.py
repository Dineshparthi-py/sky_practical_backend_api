from app.CommonLib import helper
from app.CommonLib import security_helper as security
from app.market.helper import BittrexRequests
from app import BITTREX_MARKET_SUMMARIES_API, BITTREX_MARKET_SUMMARY_API


@security.TokenOperations.token_required
def get_all_market_summaries():
    """
    retrieve all market summaries without any queries
    :return:
    """
    try:
        resp = BittrexRequests(BITTREX_MARKET_SUMMARIES_API).get_data()
        # response - failed
        if resp.get('status') is not None:
            return helper.response_jsonify(resp), 500

        return helper.response_json('success', {"items": resp['result']}, "fetched all market summaries successfully",
                                    200), 200
    except Exception as e:
        details = "Market summaries api unable to read data - Exception occurred " + str(e)
        return helper.response_json('failed', {}, details, 500), 500


@security.TokenOperations.token_required
def get_market_summary(market):
    """
    retrieve market summary with market query
    :param market:
    :return:
    """
    try:
        payload = {"market": market}
        resp = BittrexRequests(BITTREX_MARKET_SUMMARY_API).get_data(payload=payload)
        # response - failed
        if resp.get('status') is not None:
            return helper.response_jsonify(resp), 500

        return helper.response_json('success', {"items": resp['result']}, "fetched market summary successfully",
                                    200), 200
    except Exception as e:
        details = "Market summary api unable to read data - Exception occurred " + str(e)
        return helper.response_json('failed', {}, details, 500), 500
