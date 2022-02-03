from app.CommonLib import helper
from app.CommonLib import security_helper as security


@security.token_required()
def get_all_market_summaries():
    """
    retrieve all market summaries without any queries
    :return:
    """
    try:
        pass
        # code here
        # return helper.response_json('success', {"datas": []}, "fetched all market summaries successfully", 500)
    except Exception as e:
        details = "All market summaries api unable to read data - Exception occurred" + str(e)
        return helper.response_json('failed', {}, details, 500)


@security.token_required()
def get_market_summary(market):
    """
    retrieve market summary with market query
    :return:
    """
    try:
        # code here
        return helper.response_json('success', {"datas": []}, "fetched market summary successfully", 500)
    except Exception as e:
        details = "All market summaries api unable to read data - Exception occurred" + str(e)
        return helper.response_json('failed', {}, details, 500)
