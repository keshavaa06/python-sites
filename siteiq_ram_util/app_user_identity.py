import pymysql


def get_user_identity(db_con, event):
    user_uuid = None
    if (event is not None and 'requestContext' in event and 'authorizer' in event['requestContext'] and 'claims' in event['requestContext']['authorizer'] and 'sub' in event['requestContext']['authorizer']['claims']):
        user_uuid = event['requestContext']['authorizer']['claims']['sub']
        # f71e99e6-e23c-4b1a-be60-26df918a12f8 (user_uuid in user_accout table)

    if (db_con is not None and user_uuid is not None):
        cursor = db_con.cursor()
        sql_query = """ CALL sp_GetUserIdentity(%s)""" # stored procedure, in mysql
        cursor.execute(sql_query, user_uuid)
        user_identity_result = cursor.fetchone()
        cursor.close()
        if (user_identity_result is not None):
            user_identity = {
                "user_id": user_identity_result['user_id'],
                "user_uuid": user_identity_result['user_uuid'],
                "username": user_identity_result['username'],
                "user_type": user_identity_result['user_type'],
                "person_name": user_identity_result['person_name'],
                "email": user_identity_result['email'],
                "mobile": user_identity_result['mobile'],
                "account_status": user_identity_result['account_status'],
                "login_status": user_identity_result['login_status'],
                "user_status": user_identity_result['user_status'],
                "user_role_id": user_identity_result['user_role_id'],
                "user_role_name": user_identity_result['user_role_name']
            }
            return user_identity
        else:
            return None
    else:
        return None


def get_user_organizations(db_con, user_id, info_type):

    if (db_con is not None and user_id is not None):
        cursor = db_con.cursor()
        sql_query = """ CALL sp_GetUserOrganizations(%s, %s)"""
        check_tuple = (user_id, info_type)
        cursor.execute(sql_query, check_tuple)
        user_organizations_result = cursor.fetchall()
        cursor.close()

        if (user_organizations_result is not None and len(user_organizations_result) > 0):
            user_organizations = []
            for row in user_organizations_result:
                if (info_type == "D"):
                    record = {
                        "organization_id": row['organization_id'],
                        "company_type": row['company_type'],
                        "entity_type": row['entity_type'],
                        "organization_name": row['organization_name'],
                        "root_id": row['root_id'],
                        "parent_id": row['parent_id'],
                        "organization_status": row['organization_status'],
                        "organization_treepath": row['organization_treepath']
                    }
                elif (info_type == "S"):
                    record = {
                        "organization_id": row['organization_id'],
                        "company_type": row['company_type'],
                        "entity_type": row['entity_type'],
                        "organization_name": row['organization_name'],
                    }
                else:
                    record = {
                        "organization_id": row['organization_id']
                    }

                user_organizations.append(record)

            return user_organizations
        else:
            return None
    else:
        return None


def get_user_organization_ids(db_con, user_id):

    if (db_con is not None and user_id is not None):
        cursor = db_con.cursor()
        sql_query = """ CALL sp_GetUserOrganizations(%s, %s)"""
        check_tuple = (user_id, 'I')
        cursor.execute(sql_query, check_tuple)
        user_organizations_result = cursor.fetchall()
        cursor.close()

        if (user_organizations_result is not None and len(user_organizations_result) > 0):
            user_organization_ids = []
            for row in user_organizations_result:
                user_organization_ids.append(row['organization_id'])

            return user_organization_ids
        else:
            return None
    else:
        return None


def is_part_access_privileged(db_con, part_code, user_id, role_id=None):

    if (db_con is not None and part_code is not None and user_id is not None):
        cursor = db_con.cursor()
        sql_query = """ CALL sp_GetPartAccessPrivilege(%s, %s, %s)"""
        check_tuple = (part_code, user_id, role_id)
        cursor.execute(sql_query, check_tuple)
        part_result = cursor.fetchone()
        cursor.close()

        if (part_result is not None and len(part_result) > 0):
            return True
        else:
            return False
    else:
        return False


def is_part_data_access_privileged(db_con, part_code, user_id, user_type, data_id):

    if (db_con is not None and part_code is not None and user_id is not None and user_type is not None and data_id is not None):

        cursor = db_con.cursor()
        sql_query = """ CALL sp_GetPartDataAccessPrivilege(%s, %s, %s, %s)"""
        check_tuple = (part_code, user_id, user_type, data_id)
        cursor.execute(sql_query, check_tuple)
        part_data_result = cursor.fetchone()
        cursor.close()

        if (part_data_result is not None and len(part_data_result) > 0):
            return True
        else:
            return False
    else:
        return False
