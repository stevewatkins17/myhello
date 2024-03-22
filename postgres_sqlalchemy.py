import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# Database connection parameters
db_user = 'postgres'
db_password = 'postgres'
db_host = 'localhost'
db_port = '5432'
db_name = 'postgres'

# Database connection URL
db_url = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

# Create SQLAlchemy engine
engine = create_engine(db_url)

# Define metadata
metadata = MetaData()

# Define user table
users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('age', Integer)
)

# Create the user table in the database
metadata.create_all(engine)

# Insert a row into the user table
insert_query = users.insert().values(name='John', age=30)
conn = engine.connect()
conn.execute(insert_query)

# Query the user table
select_query = users.select()
result = conn.execute(select_query)

# Fetch the results and convert to a Pandas DataFrame
df = pd.DataFrame(result.fetchall(), columns=result.keys())

# Close the database connection
conn.close()

# Print the DataFrame
print(df)
