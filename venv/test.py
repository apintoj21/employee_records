import psycopg2

conn = psycopg2.connect("host=localhost dbname=emp_db user=postgres password=ajp-21")
cur = conn.cursor()
cur.execute("""
    CREATE TABLE emp_rec(
    Emp_id integer PRIMARY KEY,
    First_Name text,
    Last_Name text,
    Gender text,
    E_Mail text,
    Date_of_Birth date,
    Date_of_Joining	date,
    Department text,
    Salary numeric,
    City text,
    State text,
    Zip integer,
    Region text,
    User_Name text,
    Password text
)
""")
conn.commit()
