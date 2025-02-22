import great_expectations as gx
import pandas as pd
from sqlalchemy import create_engine
from great_expectations.core.batch import BatchRequest

server_name = "DESKTOP-A6R8AFJ\\SQLEXPRESS01"
database_name = "Awesome"

connection_string = f"mssql+pyodbc://{server_name}/{database_name}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes&charset=utf8"

engine = create_engine(connection_string)
connection = engine.connect()

query = "SELECT TOP 10 * FROM [dbo].[sales]"

try:
    df = pd.read_sql(query, engine)
    print("Query Executed Successfully")
    print(df)
except Exception as e:
    print(f"Error Occurred: {e}")  # Use f-string for formatting the error message

# Initialize Great Expectations context without a specific path
context = gx.get_context()

# Create a DataFrame validator
validator = context.sources.pandas_default.read_dataframe(df)

# Add expectations
validator.expect_column_values_to_be_between(
    column="Boxes",
    min_value=10,
    max_value=10000
)

# Run validation
results = validator.validate()

print(results)

# python .\gx_data\connectTest.py