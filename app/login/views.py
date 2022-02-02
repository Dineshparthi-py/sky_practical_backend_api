from app.CommonLib import helper
from app.CommonLib.security_helper import encode_auth_token

import json
import connexion


def login():
    """
    this file helps to check username and password to login and generate auth token.
    Note: here using json file to stored login details, so this login function will not check any dbs.
    :param username:
    :param password:
    :return:
    """
    try:
        username, password = None, None
        if connexion.request.is_json:
            body = connexion.request.get_json()
            username = body.get('username')
            password = body.get('password')

        # read json
        json_file = open("app/login/sample_login_credentials.json", 'r')
        json_data = json.load(json_file)
        check_login = [{'name': username, 'pwd': password} for data in json_data
                       if data.get('username') == username and data.get('password') == password]

        # check authenticate
        if not check_login:
            details = "Password Incorrect"
            return helper.response_json('failed', {}, details, 500), 500

        # generate token
        token = encode_auth_token(username)
        if token['status'] is False:
            details = "Token generate failure"
            return helper.response_json('failed', {}, details, 500), 500
        token = {"auth_token": token['result']}

        return helper.response_json('success', token, "fetched market summary successfully", 200)
    except Exception as e:
        details = "Login is failure - Exception occurred" + str(e)
        return helper.response_json('failed', {}, details, 500), 500
