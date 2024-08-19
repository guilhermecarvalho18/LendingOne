import os
import pandas as pd
from sqlalchemy import create_engine, text
from snowflake.sqlalchemy import URL
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get Snowflake connection details from environment variables
try:
    connection_url = URL(
        user=os.getenv('SNOWFLAKE_USER'),
        password=os.getenv('SNOWFLAKE_PASSWORD'),
        account=os.getenv('SNOWFLAKE_ACCOUNT'),
        warehouse=os.getenv('SNOWFLAKE_WAREHOUSE'),
        database=os.getenv('SNOWFLAKE_DATABASE'),
        schema=os.getenv('SNOWFLAKE_SCHEMA')
    )
    print("Connection to Snowflake succeeded.")
except Exception as e:
    print(f"Error connecting to Snowflake: {e}")
    raise

# Create SQLAlchemy engine
engine = create_engine(connection_url)

try:
    # Step 1: Create the table if it does not exist
    create_table_query = """
    CREATE TABLE IF NOT EXISTS MERGED_DATA (
        transaction_id INT,
        customer_name STRING,
        match_name STRING,
        amount DECIMAL(10, 2),
        transaction_date DATE,
        email STRING
    );
    """
    with engine.connect() as conn:
        conn.execute(text(create_table_query))
        print("Table MERGED_DATA created or already exists.")

    # Load the merged dataset (produced by data_merge.py)
    merged_table = pd.read_csv('data/merged_table.csv')

    # Clean the column names by stripping any leading or trailing whitespace and removing quotes
    merged_table.columns = merged_table.columns.str.strip().str.replace('"', '').str.replace(' ', '_')
    print("Column names after cleaning:", merged_table.columns.tolist())

    # Step 2: Upload the DataFrame to Snowflake
    merged_table.to_sql('MERGED_DATA', engine, index=False, if_exists='append')
    print(f"Successfully uploaded {len(merged_table)} rows into Snowflake.")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    engine.dispose()
    print("Connection closed.")
