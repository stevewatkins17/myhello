from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
#import os

# Define the SQL Server connection string
server_name = "localhost"
database_name = "AdventureWorksLT2022"
path_to_sql_script = "AdventureWorks.sql"
connection_string = f"mssql+pyodbc://@{server_name}/{database_name}?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server"

# Create the engine
engine = create_engine(connection_string, echo=True)

# Define a function to read the SQL script from file
def read_sql_script(file_path):
    with open(file_path, "r") as file:
        return file.read()

# Define a function to execute the SQL script
def execute_sql_script(script, session):
    session.execute(text(script))

# Define the main function
def main():
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Read the SQL script from file
    sql_script = read_sql_script(path_to_sql_script)

    # Execute the SQL script
    execute_sql_script(sql_script, session)

    # Commit the transaction
    session.commit()

    # Close the session
    session.close()

if __name__ == "__main__":
    main()
