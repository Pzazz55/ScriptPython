import great_expectations as gx
import pandas as pd
from sqlalchemy import create_engine
from great_expectations.core.batch import BatchRequest

# Connection string to the SQL Server
server_name = "DESKTOP-A6R8AFJ\\SQLEXPRESS01"
database_name = "Awesome"
connection_string = f"mssql+pyodbc://{server_name}/{database_name}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes&charset=utf8"

# Create SQLAlchemy engine and connect
engine = create_engine(connection_string)
connection = engine.connect()

# SQL query to fetch data
query = "SELECT TOP 10 * FROM [dbo].[sales]"

# Execute query and load data into DataFrame
try:
    df = pd.read_sql(query, engine)
    print("Query Executed Successfully")
    print(df)
except Exception as e:
    print(f"Error Occurred: {e}")

# Initialize Great Expectations context with the project path
# Ensure that the path points to your Great Expectations project directory
context = gx.data_context.DataContext("D:/Aryabhat/ScriptPython/great_expectations")

# Create a BatchRequest
batch_request = BatchRequest(
    datasource_name="pandas",  # Default datasource name for pandas dataframes
    data_connector_name="default_inferred_data_connector",  # Inferred data connector
    data_asset_name="sales_data",  # Name of the data asset (just an example name)
    batch_identifiers={"default_identifier_name": "default_identifier_value"}  # Optional identifiers
)

# Create a Batch (this will wrap the dataframe as a batch)
batch = context.get_batch(batch_request)

# Create a Validator for the batch
validator = context.get_validator(batch)

# Add expectations to the validator
validator.expect_column_values_to_be_between(
    column="Boxes", 
    min_value=10, 
    max_value=10000
)

# Run validation and print results
results = validator.validate()
print(results)

# python .\gx_data\connectGX_1-3-7.py