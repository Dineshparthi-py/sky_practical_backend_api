"""
 * File Name: helper.py
 * Description: Response Helper
 * Author: Dineshkumar Dhayalan
 * Author Email: dineshkumar.dhayalan@ltts.com
"""

from flask import jsonify


# Response to jsonify from arguments
def response(status, result, detail, code):
    """
    Method to generate response
    """
    return_response = jsonify({'status': status, 'result': result, 'detail': detail, 'status_code': code})
    return_response.status_code = code
    return return_response


# Response to jsonify from Json Object
def response_jsonify(response_obj):
    """
    Method to generate response
    """
    return_response = jsonify({'status': response_obj['status'], 'result': response_obj['result'],
                               'detail': response_obj['detail'], 'status_code': response_obj['status_code']})
    return_response.status_code = response_obj['status_code']
    return return_response


# Response to Json
def response_json(status, result, detail, code):
    """
    Method to generate response json
    """
    return_response = {'status': status, 'result': result, 'detail': detail, 'status_code': code}
    return return_response

