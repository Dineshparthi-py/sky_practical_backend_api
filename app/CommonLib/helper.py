# Response to Json
def response_json(status, result, detail, code):
    """
    Method to generate response json
    """
    return_response = {'status': status, 'result': result, 'detail': detail, 'status_code': code}
    return return_response
