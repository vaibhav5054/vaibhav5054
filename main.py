# Import the library needed for connecting to SQLLite
import sqlite3
import sys
from contextlib import closing
import function

# Lab 10 - Open the SQL Connection and create a cursor
# You need a cursor later to execute the query
db_file = "sqlite.db"
try:
    db_con = sqlite3.connect(db_file)
except Exception as e:
    print("Not able to connect to the Database!")
    print("An error occurred!: ", str(e))
    sys.exit()
print("Database created and Successfully Connected to SQLite")

# Prepare and Execute Query 1: Select the version of SQL
try:
    with closing(db_con.cursor()) as cursor:
        query1 = "select sqlite_version();"
        print("---")
        print("Query: " + str(query1))
        cursor.execute(query1)
        row = cursor.fetchone()
        print("SQLite Database Version is: ", row)
except Exception as e:
    print("An error occurred!: ", str(e))

# Lab 10 - Prepare and Execute Query 2: Select Everything in the table
# Use the query_executor(cursor, query_name) function
try:
    with closing(db_con.cursor()) as cursor:
        query2 = "SELECT * FROM demo"
        cursor = function.query_executor(cursor, query2)
        function.query_response(cursor, "fetchmany", 5)
except Exception as e:
    print("An error occurred!: ", str(e))

# Prepare and Execute Query 3
try:
    with closing(db_con.cursor()) as cursor:
        query3 = "SELECT * FROM demo WHERE name='Chart'"
        cursor = function.query_executor(cursor, query3)
        function.query_response(cursor, "fetchall")
except Exception as e:
    print("An error occurred!: ", str(e))


# Prepare and Execute Query 4
try:
    with closing(db_con.cursor()) as cursor:
        query4 = "SELECT * FROM demo WHERE id > 10 and id < 13"
        cursor = function.query_executor(cursor, query4)
        all_rows = function.query_response(cursor, "fetchall")
        # Print out the number of rows selected
        print("There is/are " + str(len(all_rows)) + " row(s) selected")
        print("---")
except Exception as e:
    print("An error occurred!: ", str(e))

# Lab 10 - Get user input for Query 5
print("Look for a number between:")
small_num = int(input("small number: "))
big_num = int(input("and big number: "))

# Prepare and Execute Query 5
try:
    with closing(db_con.cursor()) as cursor:
        query5 = "SELECT * FROM demo WHERE id > ? and id < ?"
        # And a new argument to cursor.execute, instead of using the default
        cursor.execute(query5, (small_num, big_num))
        function.query_response(cursor, "fetchall")
except Exception as e:
    print("An error occurred!: ", str(e))

# Lab 10 - Extract each cell from all_rows using indices
try:
    with closing(db_con.cursor()) as cursor:
        query6 = "SELECT * FROM demo WHERE name='Chart'"
        cursor = function.query_executor(cursor, query6)
        row = function.query_response(cursor, "fetchone")
        print("ID: " + str(row[0]))
        print("Name: " + str(row[1]))
except Exception as e:
    print("An error occured!: ", str(e))

# Lab 10 - Insert into a table
# query7 = "insert into demo (id, name, hint) values('29', 'New name', 'New hint')"
# cursor = function.query_executor(cursor, query7)
# db_con.commit()

# Lab 10 - Update a table
try:
    with closing(db_con.cursor()) as cursor:
        query8 = "update demo set name = 'Newest name', hint = 'Newest hint' where id='25'"
        cursor = function.query_executor(cursor, query8)
        db_con.commit()
except Exception as e:
    print("An error occurred!: ", str(e))

# LAB EXERCISE PART 1: STRING INDEXING
db_con.row_factory = sqlite3.Row
try:
    with closing(db_con.cursor()) as cursor:
        query_q1 = "SELECT * FROM demo WHERE id > 14"
        cursor.execute(query_q1)
        row = cursor.fetchall()
        for i in range(len(row)):
            print("Names: ", str(row[i]['name']))
except Exception as e:
    print("An error occurred!: ", str(e))

# LAB EXERCISE PART 2: DELETE FIELD
try:
    with closing(db_con.cursor()) as cursor:
        query_q2 = "DELETE FROM demo WHERE id < ?"
        del_row = input("Which row id the you wants to delete?: ")
        cursor.execute(query_q2, del_row)
        num_rows = cursor.fetchall()
        print("Number of rows that were deleted were: " + str(cursor.rowcount))
except Exception as e:
    print("An error occurred!: ", str(e))

