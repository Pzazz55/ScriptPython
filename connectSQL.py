import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
import great_expectations as ge
from great_expectations.dataset import PandasDataset

# Function to create a trusted connection to SQL Server using SQLAlchemy
def connect_sql_server(server, database):
    # Connection string for SQLAlchemy using pyodbc for SQL Server
    connection_string = f"mssql+pyodbc://@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server;TrustServerCertificate=yes"
    engine = create_engine(connection_string)
    return engine

# Function to load data from SQL Server into a pandas DataFrame
def load_sql_data(engine, query):
    # Use the SQLAlchemy engine to execute the query and load the data into a pandas DataFrame
    df = pd.read_sql(query, engine)
    return df

# Convert pandas DataFrame to Great Expectations dataset
def create_ge_dataset(df):
    ge_df = ge.from_pandas(df)  # Create a Great Expectations dataframe from pandas DataFrame
    return ge_df

# Define data quality expectations
def define_expectations(ge_df):
    # Example expectations on the DataFrame columns:
    ge_df.expect_column_values_to_be_in_set("column_name", ["value1", "value2"])  # Check if values are in a predefined set
    ge_df.expect_column_values_to_be_in_type_list("another_column", ["str", "int"])  # Check column data types
    ge_df.expect_column_values_to_not_be_null("column_name")  # Ensure no nulls
    ge_df.expect_column_mean_to_be_between("numeric_column", 0, 100)  # Check numeric column within a range
    return ge_df

# Function to check the data quality
def check_data_quality(server, database, query):
    # Establish connection to SQL Server using SQLAlchemy engine
    engine = connect_sql_server(server, database)
    
    # Load the data from SQL Server
    df = load_sql_data(engine, query)
    
    # Create a Great Expectations dataset
    ge_df = create_ge_dataset(df)
    
    # Define data quality expectations
    ge_df = define_expectations(ge_df)
    
    # Run the validation and get the results
    results = ge_df.validate()
    
    # Display the validation results
    print("Validation Results:")
    print(results)

    # Check for any failed expectations
    failed_expectations = [result for result in results["results"] if not result["success"]]
    
    if failed_expectations:
        print("\nFailed Expectations:")
        for failed in failed_expectations:
            print(failed)
    else:
        print("\nAll Expectations Passed!")

if __name__ == "__main__":
    # Set the connection parameters (update these with your server and database information)
    server = 'your_sql_server_name_or_ip'
    database = 'your_database_name'
    
    # Define your SQL query to fetch data (e.g., selecting a table or running a custom query)
    query = "SELECT * FROM your_table_name"
    
    # Check data quality
    check_data_quality(server, database, query)