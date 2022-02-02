"""
 * File Name: __init__.py
 * Description: configure base setup
 * Author: Dineshkumar Dhayalan
 * Author Email: dineshkumar.dhayalan@ltts.com
"""

import os

# auth config
SECRET_KEY = os.getenv('SECRET_KEY', 'sky_api_key')
AUTH_TOKEN_EXPIRY_SECONDS = 14400

# bittrex api config
BITTREX_MARKET_SUMMARIES_API = "https://api.bittrex.com/api/v1.1/public/getmarketsummaries"
BITTREX_MARKET_SUMMARY_API = "https://api.bittrex.com/api/v1.1/public/getmarketsummary"
