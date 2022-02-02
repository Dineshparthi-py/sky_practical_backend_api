"""
 * File Name: security_helper.py
 * Description: This file helps to handle http bearer(token auth)
 * Author: Dineshkumar Dhayalan
 * Author Email: dineshkumar.dhayalan@ltts.com
"""

from app import SECRET_KEY, AUTH_TOKEN_EXPIRY_SECONDS

import jwt
import datetime


def encode_auth_token(uid):
    """
    Method to encode jwt token
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=AUTH_TOKEN_EXPIRY_SECONDS),
            'unique_id': uid}
        encoded_token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return {"status": True, "result": encoded_token}
    except Exception as e:
        return {"status": False}


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
    except Exception as e:
        return {"status": False}
