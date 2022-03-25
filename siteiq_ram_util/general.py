from datetime import datetime
import dateutil.tz
import pymysql


# Output:
#   datetime
# Get Current UTC Timestamp
# Example: get_current_utc_timestamp() => 2021-01-14 14:17:32
def get_current_utc_timestamp():
    current_utc = datetime.utcnow()
    timestamp_format = "%Y-%m-%d %H:%M:%S %Z%z"
    return current_utc.strftime(timestamp_format)


# Input:
#   timezone : string value of timezone
# Output:
#   datetime
# Get Current Timestamp based on input timezone
# Example: get_current_tz_timestamp("America/Chicago") => 2021-01-14 08:19:01.042804-06:00
def get_current_tz_timestamp(timezone):
    if (timezone is not None):
        try:
            time_zone = dateutil.tz.gettz(timezone)
            datetime_value = datetime.now(tz=time_zone)
            return datetime_value
        except Exception as e:
            raise Exception(e)

    else:
        return None


# Input:
#   timezone : string value of timezone
#   timestamp_format: output timestamp format
# Output:
#   string
# Get Current Timestamp based on input timezone and return string value based on input timestamp_format
# Example: get_current_tz_timestamp_string("America/Chicago", "%Y-%m-%d %H:%M:%S") => "2021-01-14 08:21:45"
def get_current_tz_timestamp_string(timezone, timestamp_format):
    if (timezone is not None and timestamp_format is not None):
        try:
            time_zone = dateutil.tz.gettz(timezone)
            datetime_value = datetime.now(tz=time_zone)
            datetime_string = datetime_value.strftime(timestamp_format)
            return datetime_string
        except Exception as e:
            raise Exception(e)

    else:
        return None


# Input:
#   timezone : string value of timezone
#   timestamp_format :  input timestamp format
#   timestamp :  string value
# Output:
#   datetime
# Formats the input string timestamp based on timestamp_format with timezone to output datetime
# Example: get_tz_timestamp("America/Chicago", "%Y-%m-%d %H:%M:%S", "2021-01-02 09:54:40") => 2021-01-02 09:54:40-06:00
def get_tz_timestamp(timezone, timestamp_format, timestamp):
    if (timezone is not None and timestamp_format is not None and timestamp is not None):
        try:
            time_zone = dateutil.tz.gettz(timezone)
            datetime_obj = datetime.strptime(timestamp, timestamp_format)
            datetime_value = datetime(year=datetime_obj.year, month=datetime_obj.month, day=datetime_obj.day,
                                      hour=datetime_obj.hour, minute=datetime_obj.minute, second=datetime_obj.second, tzinfo=time_zone)
            return datetime_value
        except Exception as e:
            raise Exception(e)

    else:
        return None


# Input:
#   timezone : string value of timezone
#   timestamp_format :  output string timestamp format
#   timestamp :  datetime value
# Output:
#   string
# Formats the input timestamp to output string timestamp based on input timestamp_format with timezone
# Example: get_tz_timestamp_string("America/Chicago", "%Y-%m-%d %H:%M:%S %Z", 2021-01-02 09:54:40) => "2021-01-02 09:54:40 CST"
def get_tz_timestamp_string(timezone, timestamp_format, timestamp):
    if (timezone is not None and timestamp_format is not None and timestamp is not None):
        try:
            time_zone = dateutil.tz.gettz(timezone)
            if (isinstance(timestamp, datetime) == True):
                datetime_obj = timestamp
                datetime_value = datetime(year=datetime_obj.year, month=datetime_obj.month, day=datetime_obj.day,
                                          hour=datetime_obj.hour, minute=datetime_obj.minute, second=datetime_obj.second, tzinfo=time_zone)
                datetime_string = datetime_value.strftime(timestamp_format)
                return datetime_string
            else:
                return None
        except Exception as e:
            raise Exception(e)
    else:
        return None


# Input:
#   timestamp : datetime value
#   source_timezone :  string value of source timezone
#   target_timezone :  string value of target timezone
# Output:
#   datetime object
# Converts a timestamp of source timezone to target timezone
# Example: get_timestamp_tz_conversion(2021-01-02 09:54:40, "UTC", "America/Chicago") => 2021-01-02 03:54:40-06:00
def get_timestamp_tz_conversion(timestamp, source_timezone, target_timezone):
    if (timestamp is not None and source_timezone is not None and target_timezone is not None):
        try:
            source_time_zone = dateutil.tz.gettz(source_timezone)
            target_time_zone = dateutil.tz.gettz(target_timezone)
            if (isinstance(timestamp, datetime) == True):
                datetime_obj = timestamp
                datetime_obj = datetime_obj.replace(tzinfo=source_time_zone)
                datetime_value = datetime_obj.astimezone(target_time_zone)
                return datetime_value
            else:
                return None
        except Exception as e:
            raise Exception(e)

    else:
        return None


# Input
#   timestamp : string value
#   timestamp_format :  string value with the format of input timestamp
# Output:
#   datetime object
# Converts a string timestamp with a input timestamp_format to datetime object
# Example: get_timestamp("2021-01-02 03:54:40", "%Y-%m-%d %H:%M:%S") => 2021-01-02 03:54:40
def get_timestamp(timestamp, timestamp_format):
    if (timestamp is not None and timestamp_format is not None):
        try:
            datetime_obj = datetime.strptime(timestamp, timestamp_format)
            return datetime_obj
        except Exception as e:
            raise Exception(e)
    else:
        return None


# Input
#   timestamp : datetime value
#   timestamp_format :  string value with the format of output value
# Output:
#   string
# Converts a datetime timestamp value to a string value based on the input timestamp_format
# Example: get_timestamp_string(2021-01-02 03:54:40-06:00, "%Y-%m-%d %H:%M") => "2021-01-02 03:54"
def get_timestamp_string(timestamp, timestamp_format):
    if (timestamp is not None and timestamp_format is not None):
        try:
            if (isinstance(timestamp, datetime) == True):
                datetime_obj = timestamp
                datetime_value = datetime(year=datetime_obj.year, month=datetime_obj.month, day=datetime_obj.day,
                                          hour=datetime_obj.hour, minute=datetime_obj.minute, second=datetime_obj.second)
                datetime_string = datetime_value.strftime(timestamp_format)
                return datetime_string
            else:
                return None
        except Exception as e:
            raise Exception(e)
    else:
        return None


def get_db_connection(rdshost, username, password, database, timeout, cursor=None):
    try:
        if (cursor is not None):
            db_con = pymysql.connect(
                rdshost, user=username, passwd=password, db=database, connect_timeout=5, cursorclass=cursor)
        else:
            db_con = pymysql.connect(
                rdshost, user=username, passwd=password, db=database, connect_timeout=timeout)

        return db_con
    except Exception as e:
        raise Exception(e)


def close_db_connection(db_con):
    if db_con is not None and db_con.open:
        db_con.close()
