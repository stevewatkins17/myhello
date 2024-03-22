import psycopg2
import pandas as pd

# PostgreSQL connection parameters
host = "localhost"
port = 5432
database = "postgres"
user = "postgres"
password = "postgres"

# Connect to the PostgreSQL database
try:
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )
    print("Connected to the PostgreSQL database successfully")
except psycopg2.Error as e:
    print("Error: Could not connect to the PostgreSQL database")
    print(e)
    exit()

# Query metadata
query = """
    SELECT table_schema, table_name
    FROM information_schema.tables
    WHERE table_schema NOT IN ('pg_catalog', 'information_schema')
    ORDER BY table_schema, table_name
"""

# Execute the query
try:
    df = pd.read_sql_query(query, conn)
    print("Query executed successfully")
    print("Results:")
    print(df)
except psycopg2.Error as e:
    print("Error: Could not execute the query")
    print(e)

# Close the database connection
conn.close()
