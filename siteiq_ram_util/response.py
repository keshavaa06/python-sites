import json
import base64
from io import BytesIO
import gzip


def get_general_failure_response():
    data = {
        'message': 'There was an error on the server and the request could not be completed.',
        'errors': [
            {'code': 'E00101', 'message': 'An error has occurred.'}
        ]
    }
    return {
        'statusCode': 500,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(data),
        'isBase64Encoded': 'false'
    }


def get_db_connection_failure_response():
    data = {
        'message': 'There was an error on the server and the request could not be completed.',
        'errors': [
            {'code': 'E00102', 'message': 'Database connection failure.'}
        ]
    }
    return {
        'statusCode': 500,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(data),
        'isBase64Encoded': 'false'
    }


def get_db_operation_failure_response():
    data = {
        'message': 'There was an error on the server and the request could not be completed.',
        'errors': [
            {'code': 'E00103', 'message': 'Database operation failed.'}
        ]
    }
    return {
        'statusCode': 500,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(data),
        'isBase64Encoded': 'false'
    }


def get_http_method_invalid_response():
    data = {
        'message': 'There was an error on the server and the request could not be completed.',
        'errors': [
            {'code': 'E00105', 'message': 'Requested method is not supported.'}
        ]
    }
    return {
        'statusCode': 405,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(data),
        'isBase64Encoded': 'false'
    }


def get_request_body_missing_response():
    data = {
        'message': 'Invalid request.',
        'errors': [
            {'code': 'E00106', 'message': 'Request does not contain body.'}
        ]
    }
    return {
        'statusCode': 400,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(data),
        'isBase64Encoded': 'false'
    }


def get_request_path_param_invalid_response():
    data = {
        'message': 'Invalid request.',
        'errors': [
            {'code': 'E00107',
                'message': 'Request path parameter is either missing or invalid.'}
        ]
    }
    return {
        'statusCode': 400,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(data),
        'isBase64Encoded': 'false'
    }


def get_request_query_param_invalid_response():
    data = {
        'message': 'Invalid request.',
        'errors': [
            {'code': 'E00108',
                'message': 'Request query parameter is either missing or invalid.'}
        ]
    }
    return {
        'statusCode': 400,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(data),
        'isBase64Encoded': 'false'
    }


def get_object_not_found_response():
    data = {
        'message': 'Object not Found.',
        'errors': [
            {'code': 'E00104', 'message': 'No data found.'}
        ]
    }
    return {
        'statusCode': 404,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(data),
        'isBase64Encoded': 'false'
    }


def get_unauthorized_access_response():
    data = {
        'message': 'Unauthorized access.',
        'errors': [
            {'code': 'E00111', 'message': 'Unauthorized access to the resource.'}
        ]
    }
    return {
        'statusCode': 401,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(data),
        'isBase64Encoded': 'false'
    }


def get_failure_response(code, message, errors):
    data = {
        'message': message,
        'errors': errors
    }
    return {
        'statusCode': code,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(data),
        'isBase64Encoded': 'false'
    }


def get_success_response(data):
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(data),
        'isBase64Encoded': 'false'
    }


def get_success_gzip_response(data):
    compressed = BytesIO()
    with gzip.GzipFile(fileobj=compressed, mode='w') as f:
        json_response = json.dumps(data)
        f.write(json_response.encode('utf-8'))
    compressed_encode_data = base64.b64encode(
        compressed.getvalue()).decode('ascii')
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Content-Encoding': 'gzip',
            'Access-Control-Allow-Origin': '*'
        },
        'body': compressed_encode_data,
        'isBase64Encoded': 'true',
    }
