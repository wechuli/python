import psycopg2

try:

    conn = psycopg2.connect(user="python_app",
                            password="secpassword",
                            host="127.0.0.1",
                            port="5432",
                            database="scrapy")
    cur = conn.cursor()
    # Print PostgreSQL Connection properties
    print(conn.get_dsn_parameters(), "\n")
    # Print PostgreSQL version
    cur.execute("SELECT version();")
    record = cur.fetchone()
    print("You are connected to - ", record, "\n")
except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    # closing database connection
    if(conn):
        cur.close()
        conn.close()
        print("PostgreSQL connection is closed")
