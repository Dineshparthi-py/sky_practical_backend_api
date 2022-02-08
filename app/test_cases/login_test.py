from app.CommonLib.security_helper import TokenOperations

import pytest
import requests


@pytest.mark.parametrize("username, password", [("admin_001", "admin_001@12345"), ("manager_001", "manager_001@12345")])
def test_login_valid(market_url, username, password):
    # urls
    url = market_url + "/login"

    data = {'username': username, 'password': password}
    resp = requests.post(url, json=data)
    out_result = resp.json()
    auth_username = TokenOperations.decode_token(out_result['result']['auth_token'])['result']['username']

    # api response
    assert resp.status_code == 200, resp.text
    # auth token validation
    assert auth_username == username, resp.text


@pytest.mark.parametrize("username", [("admin_001"), ("manager_001")])
def test_login_no_password(market_url, username):
    # urls
    url = market_url + "/login"

    data = {'username': username}
    resp = requests.post(url, json=data)

    # chech password validation
    assert resp.status_code == 400, resp.text


def test_login_no_username(market_url):
    # urls
    url = market_url + "/login"

    data = {}
    resp = requests.post(url, json=data)

    # check username validation
    assert resp.status_code == 400, resp.text


@pytest.mark.parametrize("username, password", [("admin_00", "admin_001@12345"), ("manager_001", "manager_00@12345")])
def test_login_incorrect(market_url, username, password):
    # urls
    url = market_url + "/login"

    data = {'username': username, 'password': password}
    resp = requests.post(url, json=data)
    out_result = resp.json()

    # server error
    assert resp.status_code == 500, resp.text
    # username/password check
    assert out_result['detail'] == "Username/Password Incorrect", resp.text



