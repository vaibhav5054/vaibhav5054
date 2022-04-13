# Lab 10 - Create functions to automate our query execution and response
# Prepare and Execute Query
def query_executor(query_cursor, query_name):
    print("---")
    query_sql = query_name
    print("Query: " + str(query_sql))
    query_cursor.execute(query_sql)
    return query_cursor


# Get the Response to SQL query
def query_response(query_cursor, fetch_type, fetch_amount=3):
    print("---")
    if fetch_type == "fetchall":
        all_rows = query_cursor.fetchall()
        for query_row in all_rows:
            print(query_row)
    elif fetch_type == "fetchmany":
        all_rows = query_cursor.fetchmany(fetch_amount)
        for query_row in all_rows:
            print(query_row)
    elif fetch_type == "fetchone":
        all_rows = query_cursor.fetchone()
        print(all_rows)
    else:
        all_rows = query_cursor.fetc
    return all_rows
