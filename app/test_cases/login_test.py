from app.CommonLib.security_helper import TokenOperations

import pytest


@pytest.mark.parametrize("username, password", [("admin_001", "admin_001@12345"), ("manager_001", "manager_001@12345")])
def test_login_valid(client, username, password):
    # urls
    url = "/api/v1/login"

    data = {'username': username, 'password': password}
    resp = client.post(url, json=data)
    out_result = resp.json
    auth_username = TokenOperations.decode_token(out_result['result']['auth_token'])['result']['username']

    # api response
    assert resp.status_code == 200, resp.text
    # auth token validation
    assert auth_username == username, resp.text


@pytest.mark.parametrize("username", [("admin_001"), ("manager_001")])
def test_login_no_password(client, username):
    # urls
    url = "/api/v1/login"

    data = {'username': username}
    resp = client.post(url, json=data)

    # chech password validation
    assert resp.status_code == 400, resp.text


def test_login_no_username(client):
    # urls
    url = "/api/v1/login"

    data = {}
    resp = client.post(url, json=data)

    # check username validation
    assert resp.status_code == 400, resp.text


@pytest.mark.parametrize("username, password", [("admin_00", "admin_001@12345"), ("manager_001", "manager_00@12345")])
def test_login_incorrect(client, username, password):
    # urls
    url = "/api/v1/login"

    data = {'username': username, 'password': password}
    resp = client.post(url, json=data)
    out_result = resp.json

    # server error
    assert resp.status_code == 500, resp.text
    # username/password check
    assert out_result['detail'] == "Incorrect username/password", resp.text

