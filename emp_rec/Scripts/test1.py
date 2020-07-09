import psycopg2

try:
    connection = psycopg2.connect("host=localhost dbname=emp_db user=postgres password=ajp-21")

    cursor = connection.cursor()
    postgreSQL_select_Query = "select * from emp_rec"

    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from emp_rec table using cursor.fetchall")
    emp_records = cursor.fetchall()

    print("Print each row and it's columns values")
    for row in emp_records:
        print("Emp_id = ", row[0], )
        print("First_Name = ", row[1], )
        print("Last_Name  = ", row[2], "\n")

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    # closing database connection.
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")