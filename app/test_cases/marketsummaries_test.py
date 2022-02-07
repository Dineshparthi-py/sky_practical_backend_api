import pytest
import requests


@pytest.mark.parametrize("username, password", [("admin_001", "admin_001@12345"), ("manager_001", "manager_001@12345")])
def test_market_summaries(market_url, username, password):
    # urls
    summaries_url = market_url + "/marketsummaries"
    login_url = market_url + "/login"

    # login testcase
    data = {'username': username, 'password': password}
    login_resp = requests.post(login_url, json=data)
    out_result = login_resp.json()

    # market summaries testcase
    market_resp = requests.get(summaries_url,
                               headers={'Authorization': "Bearer "+str(out_result['result']['auth_token'])})

    # login validation
    assert login_resp.status_code == 200, login_resp.text
    # market summaries api validate
    assert market_resp.status_code == 200, market_resp.text


def test_market_summaries_without_authtoken(market_url):
    # urls
    summaries_url = market_url + "/marketsummaries"

    # market summaries testcase
    market_resp = requests.get(summaries_url)
    out_result = market_resp.json()

    assert market_resp.status_code == 401, market_resp.text
    assert out_result['detail'] == "No authorization token provided", market_resp.text


@pytest.mark.parametrize("token", [("Bearer qsfsadfsdafe454gsdfgr5tyrgfsaewa34243"), ("vdsfgsdwe35refdffdfgh45t343r")])
def test_market_summaries_invalid_token(market_url, token):
    # urls
    summaries_url = market_url + "/marketsummaries"

    # market summaries testcase
    market_resp = requests.get(summaries_url, headers={'Authorization': token})
    out_result = market_resp.json()

    # market summaries api validate
    assert market_resp.status_code == 401, market_resp.text
    assert out_result['detail'] == "Invalid authorization header", market_resp.text


