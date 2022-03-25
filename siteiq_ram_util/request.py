import re


def get_body_param_value(body, key):
    return_value = None
    if (body is not None and key is not None):
        if (key in body):
            val = body[key]
            if (isinstance(val, str)):
                return_value = val.strip()
            elif (isinstance(val, int)):
                return_value = val
            elif (isinstance(val, float)):
                return_value = val
            elif (isinstance(val, bool)):
                return_value = val
            else:
                return_value = val
    return return_value


def get_list_query_param_values(query_params):

    param_page_offset_key = "pageOffset"
    param_page_limit_key = "pageLimit"
    param_sort_field_key = "sortField"
    param_sort_order_key = "sortOrder"

    param_page_offset_value = None
    param_page_limit_value = None
    param_sort_field_value = None
    param_sort_order_value = None

    if (param_page_offset_key in query_params and param_page_limit_key in query_params):
        try:
            param_page_offset_value = int(
                query_params[param_page_offset_key])
            param_page_limit_value = int(
                query_params[param_page_limit_key])
        except:
            param_page_offset_value = None
            param_page_limit_value = None

    if (param_sort_field_key in query_params):
        try:
            pattern = re.compile(r"^[a-zA-Z0-9_-]+$")
            if (pattern.search(query_params[param_sort_field_key])):
                param_sort_field_value = str(
                    query_params[param_sort_field_key])
            else:
                param_sort_field_value = None
        except:
            param_sort_field_value = None
    if (param_sort_order_key in query_params):
        try:
            param_sort_order_value = int(
                query_params[param_sort_order_key])
        except:
            param_sort_order_value = None

    return param_page_offset_value, param_page_limit_value, param_sort_field_value, param_sort_order_value


def get_authorizer_claims(event):
    authorizer_claims = None
    if (event is not None and 'requestContext' in event and 'authorizer' in event['requestContext'] and 'claims' in event['requestContext']['authorizer']):
        authorizer_claims = event['requestContext']['authorizer']['claims']
    return authorizer_claims


def get_authorizer_sub(event):
    authorizer_sub = None
    if (event is not None and 'requestContext' in event and 'authorizer' in event['requestContext'] and 'claims' in event['requestContext']['authorizer'] and 'sub' in event['requestContext']['authorizer']['claims']):
        authorizer_sub = event['requestContext']['authorizer']['claims']['sub']
    return authorizer_sub


def get_query_string_parameter_value(event, key):
    return_value = None
    if (event is not None and key is not None and 'queryStringParameters' in event):
        if (event['queryStringParameters'] is not None and key in event['queryStringParameters'] and event['queryStringParameters'][key] is not None and event['queryStringParameters'][key] != ""):
            val = event['queryStringParameters'][key]
            if (isinstance(val, str)):
                return_value = val.strip()
            elif (isinstance(val, int)):
                return_value = val
            elif (isinstance(val, float)):
                return_value = val
            elif (isinstance(val, bool)):
                return_value = val
            else:
                return_value = val
    return return_value


def get_path_parameter_value(event, key):
    return_value = None
    if (event is not None and key is not None and 'pathParameters' in event):
        if (key in event['pathParameters']):
            val = event['pathParameters'][key]
            if (isinstance(val, str)):
                return_value = val.strip()
            elif (isinstance(val, int)):
                return_value = val
            elif (isinstance(val, float)):
                return_value = val
            elif (isinstance(val, bool)):
                return_value = val
            else:
                return_value = val
    return return_value
