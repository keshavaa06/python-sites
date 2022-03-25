import logging
import pymysql
import json
from json import dumps
import os
import sys
import boto3
import siteiq_ram_util

class Site:

    def __init__(self):

        self.param_user_id_key = "userId"
        self.param_site_id_key = "siteId"
        self.param_site_number_key = "siteNumber"
        self.param_site_name_key = "siteName"
        self.param_filter_type_key = "filterType"
        self.param_page_offset_key = "pageOffset"
        self.param_page_limit_key = "pageLimit"
        self.param_sort_field_key = "sortField"
        self.param_sort_order_key = "sortOrder"
        self.param_record_count_key = "recordCount"
        self.param_total_records_key = "totalRecords"
        self.param_element_key = "element"
        self.param_code_key = "code"
        self.param_message_key = "message"
        self.param_value_key = "value"
        self.param_location_key = "location"
        self.param_result_key = "result"
        self.param_records_key = "records"
        self.param_info_key = "info"
        self.param_filter_key = "filter"
        self.http_status_code_bad_request = 400
        self.label_request_data_error = "Errors in the request."
        self.label_no_data_found = "No data found."
        self.label_data_found = "Data found."

        self.const_company_type_siteiq = "S"
        self.const_company_type_owner = "O"
        self.const_company_type_provider = "P"

        self._pcPortalSiteView = "CP-SIT-SVIW"#cp:customer portal , sit:site,sviw:site view
        self._pcConfigurationDeviceView = "AT-DVC-DVIW"#module, feature, action, at:configuration, dvc:device, dviw: device view

    def open_db_connection(self):
        self.db_con = siteiq_ram_util.get_db_connection(host='localhost',user='root',passwd='1234',database='kmart',time_out=5,cursor=pymysql.cursor.DictCursor)
        #self.db_con=pymysql.connect(host='localhost',user='root',passwd='1234',database='kmart',cursor=pymysql.cursor.DictCursor)
        print('connected to db with object: ',self.db_con)


site = Site()
site.open_db_connection()
#     def close_db_connection(self):
#         general_util.close_db_connection(self.db_con)
#         logger.info(
#             "INFO: Site [sites] Database <" + database + "> Connection Closed")
#
#     # /sites GET
#     def get_sites(self, event):
#         logger.info(
#             "INFO: Site [sites] get_sites()")
#
#         self.open_db_connection()
#
#         identity_user_object = general_util.get_user_identity(
#             self.db_con, event)
#         identity_user_site_view_privilege_status = False
#         identity_user_device_view_privilege_status = False
#
#         if (identity_user_object is not None):
#             identity_user_site_view_privilege_status = general_util.is_part_access_privileged(
#                 self.db_con, self._pcPortalSiteView, identity_user_object.get('user_id'))
#
#             identity_user_device_view_privilege_status = general_util.is_part_access_privileged(
#                 self.db_con, self._pcConfigurationDeviceView, identity_user_object.get('user_id'))
#
#         if (identity_user_object is not None and (identity_user_site_view_privilege_status == True or identity_user_device_view_privilege_status == True)):
#
#             identity_user_id = int(identity_user_object.get('user_id'))
#
#             param_page_offset_value = None
#             param_page_limit_value = None
#             param_sort_field_value = None
#             param_sort_order_value = None
#             param_site_status_value = 1
#
#             if (event['queryStringParameters']):
#                 query_params = event['queryStringParameters']
#
#                 param_page_offset_value, param_page_limit_value, param_sort_field_value, param_sort_order_value = general_util.get_list_query_param_values(
#                     query_params)
#
#             try:
#
#                 sites_total_count = 0
#                 where_condition = " AND 1=2 "
#                 response_info_filter = {}
#
#                 where_condition = (
#                     """ AND b.active_status = 1 AND b.user_id = {0} """).format(identity_user_id)
#                 response_info_filter.update(
#                     {self.param_user_id_key: identity_user_id})
#
#                 where_condition += (" AND a.site_status = {0}").format(
#                     param_site_status_value)
#
#                 cursor = self.db_con.cursor()
#                 sql_count_query = """SELECT COUNT(a.site_id) as site_count FROM site a, user_site b WHERE a.site_id = b.site_id """
#                 sql_count_query = sql_count_query + where_condition
#                 cursor.execute(sql_count_query)
#                 sites_total_count = cursor.fetchone()['site_count']
#                 cursor.close()
#
#                 cursor = self.db_con.cursor()
#                 sql_get_query = (
#                     """SELECT a.site_id, a.site_name, a.site_number FROM site a, user_site b WHERE a.site_id = b.site_id """)
#                 sql_get_query = sql_get_query + where_condition
#
#                 if (param_sort_field_value is None):
#                     param_sort_field_value = "siteName"
#
#                 if (param_sort_order_value is None):
#                     param_sort_order_value = 1
#
#                 if (param_sort_field_value == "siteName"):
#                     param_sort_field_value_col = "a.site_name"
#                 else:
#                     param_sort_field_value_col = "a.site_id"
#                     param_sort_field_value = "siteId"
#
#                 if (param_sort_order_value == -1):
#                     param_sort_order_value_dir = "DESC"
#                 else:
#                     param_sort_order_value_dir = "ASC"
#                     param_sort_order_value = 1
#
#                 sql_get_query = sql_get_query + " ORDER BY " + \
#                     param_sort_field_value_col + " " + param_sort_order_value_dir + " "
#
#                 if (param_page_offset_value is not None and param_page_limit_value is not None):
#                     record_start = param_page_offset_value * param_page_limit_value
#                     record_count = param_page_limit_value
#                     sql_get_query = sql_get_query + " LIMIT " + \
#                         str(record_start) + "," + str(record_count)
#
#                 cursor.execute(sql_get_query)
#                 sites_result = cursor.fetchall()
#                 cursor.close()
#
#                 sites = []
#                 response_message = self.label_no_data_found
#
#                 response_info = {
#                     self.param_record_count_key: len(sites_result),
#                     self.param_total_records_key: sites_total_count,
#                     self.param_page_offset_key: param_page_offset_value,
#                     self.param_page_limit_key: param_page_limit_value,
#                     self.param_sort_field_key: param_sort_field_value,
#                     self.param_sort_order_key: param_sort_order_value,
#                     self.param_filter_key: response_info_filter
#                 }
#
#                 if sites_total_count > 0 and len(sites_result) > 0:
#
#                     response_message = self.label_data_found
#
#                     for row in sites_result:
#
#                         record = {
#                             self.param_site_id_key: row['site_id'],
#                             self.param_site_name_key: row['site_name'],
#                             self.param_site_number_key: row['site_number']
#                         }
#                         sites.append(record)
#
#                 response_data = {
#                     self.param_message_key: response_message,
#                     self.param_records_key: sites,
#                     self.param_info_key: response_info
#                 }
#
#                 self.close_db_connection()
#                 return general_util.get_success_gzip_response(response_data)
#
#             except Exception as e:
#                 self.close_db_connection()
#                 logger.error(
#                     "ERROR: Unexpected error in Site [sites] get_sites()")
#                 logger.error(e)
#                 return general_util.get_general_failure_response()
#
#         else:
#             self.close_db_connection()
#             logger.error(
#                 "ERROR: Unauthorized Access in Site [sites] get_sites()")
#             return general_util.get_unauthorized_access_response()
#
#
# def lambda_handler(event, context):
#
#     http_method = event["httpMethod"] # http_method = 'GET'
#     site = Site()
#
#     # /sites GET
#     if http_method == "GET":
#         return site.get_sites(event)
#
#     else:
#         return general_util.get_http_method_invalid_response()
#
#
# event_json ={
#    "A":"45678932145678/zm/cf",
#    "B":1644335071,
#    "B1":"{\"NozzleActivated\":\"true\",\"Totalizer\":\"true\",\"ATC\":\"true\",\"PushToStart\":\"false\",\"PushToStop\":\"false\",\"VaporVac\":\"false\",\"PresetType\":\"11\",\"UnitOfMeasure\":\"12\",\"UnitType\":\"13\",\"Version\":\"P03040\",\"WM\":{\"Flow\":[{\"N\":\"6\",\"G\":\"10\"},{\"N\":\"5\",\"G\":\"10\"},{\"N\":\"4\",\"G\":\"10\"},{\"N\":\"3\",\"G\":\"10\"},{\"N\":\"2\",\"G\":\"10\"},{\"N\":\"1\",\"G\":\"10\"}],\"Blend\":[{\"N\":\"6\",\"G\":\"100\"},{\"N\":\"5\",\"G\":\"0\"},{\"N\":\"4\",\"G\":\"0\"},{\"N\":\"2\",\"G\":\"67\"},{\"N\":\"3\",\"G\":\"0\"},{\"N\":\"1\",\"G\":\"100\"}],\"Cal\":[{\"CF\":\"0\",\"M\":\"8\"},{\"CF\":\"1047\",\"M\":\"4\"},{\"CF\":\"1048\",\"M\":\"5\"},{\"CF\":\"1047\",\"M\":\"1\"}],\"ppul2\":[{\"N\":\"6\",\"G\":\"7.899\"},{\"N\":\"5\",\"G\":\"8.889\"},{\"N\":\"4\",\"G\":\"5.559\"},{\"N\":\"3\",\"G\":\"3.459\"},{\"N\":\"2\",\"G\":\"2.349\"},{\"N\":\"1\",\"G\":\"1.239\"}],\"ppul1\":[{\"N\":\"6\",\"G\":\"7.899\"},{\"N\":\"5\",\"G\":\"8.889\"},{\"N\":\"4\",\"G\":\"5.559\"},{\"N\":\"3\",\"G\":\"3.459\"},{\"N\":\"2\",\"G\":\"2.349\"},{\"N\":\"1\",\"G\":\"1.239\"}]}}",
#    "httpMethod":"GET"
# }
# lambda_handler(event_json,context)# calling lambda_handler method