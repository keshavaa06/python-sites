import re
from datetime import datetime


def is_string(val):
    return isinstance(val, str)


def is_integer(val):
    if (isinstance(val, int)):
        return True
    else:
        int_val = None
        try:
            int_val = int(val)
        except:
            int_val = None
        if (int_val is not None):
            return True
        else:
            return False


def is_float(val):
    if (isinstance(val, float)):
        return True
    else:
        float_val = None
        try:
            float_val = float(val)
        except:
            float_val = None
        if (float_val is not None):
            return True
        else:
            return False


def is_boolean(val):
    return isinstance(val, bool)


def is_timestamp(val):
    return isinstance(val, datetime)


def is_list(list_val):
    return isinstance(list_val, list)


def is_list_integer(list_val):
    check_values = []
    false_positions = []
    for i, x in enumerate(list_val):
        if isinstance(x, int):
            check_values.append(isinstance(x, int))
        else:
            check_values.append(isinstance(x, int))
            false_positions.append(i)
    if all(check_values):
        return all(check_values), None
    else:
        return all(check_values), false_positions

    # return all(isinstance(x, int) for x in list_val)


def is_list_float(list_val):
    check_values = []
    false_positions = []
    for i, x in enumerate(list_val):
        if isinstance(x, float):
            check_values.append(isinstance(x, float))
        else:
            check_values.append(isinstance(x, float))
            false_positions.append(i)
    if all(check_values):
        return all(check_values), None
    else:
        return all(check_values), false_positions

    # return all(isinstance(x, float) for x in list_val)


def is_list_string(list_val):
    check_values = []
    false_positions = []
    for i, x in enumerate(list_val):
        if isinstance(x, str):
            check_values.append(isinstance(x, str))
        else:
            check_values.append(isinstance(x, str))
            false_positions.append(i)
    if all(check_values):
        return all(check_values), None
    else:
        return all(check_values), false_positions

    # return all(isinstance(x, str) for x in list_val)


def is_list_boolean(list_val):
    check_values = []
    false_positions = []
    for i, x in enumerate(list_val):
        if isinstance(x, bool):
            check_values.append(isinstance(x, bool))
        else:
            check_values.append(isinstance(x, bool))
            false_positions.append(i)
    if all(check_values):
        return all(check_values), None
    else:
        return all(check_values), false_positions

    # return all(isinstance(x, bool) for x in list_val)


def is_valid_username(username):
    username_pattern = re.compile(r'^[a-zA-Z][\w,.]*[a-zA-Z0-9]$')
    if 3 <= len(username) <= 30:
        if username_pattern.search(username):
            return True
        else:
            return False
    else:
        return False


def is_valid_password(password):
    # password_pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,30}$")
    password_pattern = re.compile(
        r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~])[A-Za-z\d!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]{8,30}$")
    if (password_pattern.search(password)):
        return True
    else:
        return False


def is_valid_email(email):
    email_pattern = re.compile(
        r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$")
    if (email_pattern.search(email)):
        return True
    else:
        return False


def get_validation_error(error_messages, error_code, element_name, element_value):
    param_element_key = "element"
    param_code_key = "code"
    param_message_key = "message"
    param_value_key = "value"
    param_location_key = "location"
    param_location_value = "body"

    error_message = error_messages.get(error_code)
    if (element_name is not None and element_value is not None):
        if (error_message.find("<" + element_name + ">") >= 0):
            error_message = error_message.replace(
                "<" + element_name + ">", element_value)
    error = {param_element_key: element_name, param_code_key: error_code, param_message_key: error_message,
             param_value_key: element_value, param_location_key: param_location_value}
    return error
