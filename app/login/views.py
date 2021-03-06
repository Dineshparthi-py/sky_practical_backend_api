"""
 * File Name: views.py
 * Description: Used to login application and generate auth token help of JWT
 * Author: Dineshkumar Dhayalan
 * Author Email: dineshkumar.dhayalan@ltts.com
"""
from app.CommonLib import helper
from app.CommonLib.security_helper import TokenOperations

import json
import connexion


def login():
    """
    This file helps to check username and password to login and generate auth token.
    Note: here using json file to stored login details, so this login function will not check any dbs.
    :param username: unique identification from user details
    :param password: passcode from user details
    :return: Api response object (json)
    """
    try:
        username, password = None, None
        if connexion.request.is_json:
            body = connexion.request.get_json()
            username = body.get('username')
            password = body.get('password')

        if username in (None, ''):
            details = "Login is failed - Missing username"
            return helper.response('failed', {}, details, 400)

        if password in (None, ''):
            details = "Login is failed - Missing password"
            return helper.response('failed', {}, details, 400)

        # read json
        json_file = open("app/login/sample_login_credentials.json", 'r')
        json_data = json.load(json_file)
        check_login = [{'name': username, 'pwd': password} for data in json_data
                       if data.get('username') == username and data.get('password') == password]

        # check authenticate
        if not check_login:
            details = "Incorrect username/password"
            return helper.response('failed', {}, details, 500)

        # generate token
        token = TokenOperations.encode_auth_token(username)
        if token['status'] is False:
            details = "Access token failed"
            return helper.response('failed', {}, details, 500)
        token = {"auth_token": token['result']}

        return helper.response('success', token, "logged in successfully", 200)
    except Exception as e:
        details = "Login failed - Exception occurred " + str(e)
        return helper.response('failed', {}, details, 500)
