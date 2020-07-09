import psycopg2

def getMobileDetails(mobileID):
    try:
        connection = psycopg2.connect("host=localhost dbname=emp_db user=postgres password=ajp-21")

        print("Using Python variable in PostgreSQL select Query")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from emp_rec where emp_id = %s"

        cursor.execute(postgreSQL_select_Query, (mobileID,))
        emp_records = cursor.fetchall()
        for row in emp_records:
            print("Emp_id = ", row[0], )
            print("First_Name = ", row[1])
            print("Last_Name  = ", row[2])

    except (Exception, psycopg2.Error) as error:
        print("Error fetching data from PostgreSQL table", error)

    finally:
        # closing database connection
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed \n")

getMobileDetails(2)
getMobileDetails(3)