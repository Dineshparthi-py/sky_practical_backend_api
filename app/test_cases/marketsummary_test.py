import pytest


@pytest.mark.parametrize("username, password", [("admin_001", "admin_001@12345"), ("manager_001", "manager_001@12345")])
def test_market_summary(client, username, password):
    # urls
    summaries_url = "/api/v1/marketsummary?market=btc-ltc"
    login_url = "/api/v1/login"

    # login testcase
    data = {'username': username, 'password': password}
    login_resp = client.post(login_url, json=data)
    out_result = login_resp.json

    # market summary testcase
    market_resp = client.get(summaries_url,
                             headers={'Authorization': "Bearer "+str(out_result['result']['auth_token'])})

    # login validation
    assert login_resp.status_code == 200, login_resp.text
    # market summaries api validate
    assert market_resp.status_code == 200, market_resp.text


@pytest.mark.parametrize("username, password", [("admin_001", "admin_001@12345"), ("manager_001", "manager_001@12345")])
def test_market_summary_without_params(client, username, password):
    # urls
    summaries_url = "/api/v1/marketsummary"
    login_url = "/api/v1/login"

    # login testcase
    data = {'username': username, 'password': password}
    login_resp = client.post(login_url, json=data)
    out_result = login_resp.json

    # market summary testcase without add payload
    market_resp = client.get(summaries_url,
                             headers={'Authorization': "Bearer "+str(out_result['result']['auth_token'])})
    out_result = market_resp.json

    # login validation
    assert login_resp.status_code == 200, login_resp.text
    # market summary api validate
    assert market_resp.status_code == 400, market_resp.text
    # makert summary validate without param
    assert out_result['detail'] == "Missing query parameter 'market'", market_resp.text


def test_market_summary_without_authtoken(client):
    # urls
    summaries_url = "/api/v1/marketsummary?market=btc-ltc"

    # market summary testcase
    market_resp = client.get(summaries_url)
    out_result = market_resp.json

    assert market_resp.status_code == 401, market_resp.text
    assert out_result['detail'] == "No authorization token provided", market_resp.text


@pytest.mark.parametrize("token", [("Bearer qsfsadfsdafe454gsdfgr5tyrgfsaewa34243"), ("vdsfgsdwe35refdffdfgh45t343r")])
def test_market_summary_invalid_token(client, token):
    # urls
    summaries_url = "/api/v1/marketsummary?market=btc-ltc"

    # market summary testcase
    market_resp = client.get(summaries_url, headers={'Authorization': token})
    out_result = market_resp.json

    # market summaries api validate
    assert market_resp.status_code == 401, market_resp.text
    assert out_result['detail'] == "Invalid authorization header", market_resp.text
