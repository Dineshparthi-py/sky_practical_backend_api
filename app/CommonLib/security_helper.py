"""
 * File Name: security_helper.py
 * Description: This file helps to handle http bearer(token auth)
 * Author: Dineshkumar Dhayalan
 * Author Email: dineshkumar.dhayalan@ltts.com
"""

from app import SECRET_KEY, AUTH_TOKEN_EXPIRY_SECONDS
from app.CommonLib import helper

import jwt
import datetime
from flask import request
from functools import wraps


class TokenOperations:

    @staticmethod
    def encode_auth_token(username):
        """
        Method to encode jwt token
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=AUTH_TOKEN_EXPIRY_SECONDS),
                'username': username}
            encoded_token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
            return {"status": True, "result": encoded_token}
        except jwt.PyJWTError:
            return {"status": False}

    @staticmethod
    def decode_token(auth_token=None):
        """
        Method to decode jwt token
        """
        try:
            if auth_token:
                usr_data = jwt.decode(auth_token, SECRET_KEY, algorithms='HS256')
                return {"status": True, "result": usr_data}
            else:
                return {"status": False}
        except jwt.DecodeError:
            return {"status": False}

    def token_required(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                token_header = request.headers.get('Authorization')
                token = token_header.split(" ", 1)[1]
            except Exception as e:
                detail = "Unable to fetch access token : Exception occurred -" + str(e)
                return helper.response_json('failed', {}, detail, 500), 500
            if not token:
                detail = "Access token is missing"
                return helper.response_json('failed', {}, detail, 500), 500
            # Decode token
            try:
                result = jwt.decode(token, SECRET_KEY, algorithms='HS256')
                is_valid_token = True if result["username"] else False
            except jwt.ExpiredSignatureError:
                detail = "Token expired, Please sign in again"
                return helper.response_json('failed', {}, detail, 401), 401
            except jwt.InvalidTokenError:
                detail = "Access token invalid"
                return helper.response_json('failed', {}, detail, 401), 401
            except Exception as e:
                detail = "Access token error : Exception occurred -" + str(e)
                return helper.response_json('failed', {}, detail, 500), 500
            return f(*args, **kwargs)
        return wrapper





