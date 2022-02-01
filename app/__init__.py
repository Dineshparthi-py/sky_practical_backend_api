"""
 * File Name: __init__.py
 * Description: configure base setup
 * Author: Dineshkumar Dhayalan
 * Author Email: dineshkumar.dhayalan@ltts.com
"""

import os

SECRET_KEY = os.getenv('SECRET_KEY', 'sky_api_key')
AUTH_TOKEN_EXPIRY_SECONDS = 14400
