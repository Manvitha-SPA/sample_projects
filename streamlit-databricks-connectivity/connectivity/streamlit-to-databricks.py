# import streamlit as st
# import pandas as pd
# import sqlalchemy
 
# # Set up a connection to the Databricks SQL Endpoint using SQLAlchemy
# # Replace with your own values for the JDBC/ODBC driver and endpoint URL
# engine = sqlalchemy.create_engine("databricks+odbc://<Driver Name>:<Host Name>:<Port Number>?Authentication=<Auth Type>")
 
# # Define a function to execute SQL queries and return the results as a Pandas dataframe
# def run_query(query):
#     with engine.connect() as con:
#         rs = con.execute(query)
#         df = pd.DataFrame(rs.fetchall(), columns=rs.keys())
#     return df
 
# # Example query to retrieve data from a Delta table
# query = "SELECT * FROM my_delta_table"
 
# # Call the function to execute the query and display the results in Streamlit
# result_df = run_query(query)
# st.dataframe(result_df)



import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Streamlit interface
st.title("Databricks and Streamlit Integration")
st.write("Connecting to Databricks using SQLAlchemy")

# Databricks connection details
server_hostname = 'databricks://community.cloud.databricks.com'
http_path = 'sql/protocolv1/o/707858319346869/0523-082518-9og7brrl'
# access_token = 'your-access-token'

# Creating the connection string
connection_string = (
    # f"databricks+pyodbc://token:{access_token}"
    f"@{server_hostname}:443"
    f"/default?HTTPPath={http_path}"
)

# Establishing connection
engine = create_engine(connection_string)
connection = engine.connect()

# Query Databricks
query = "SELECT * FROM your_table LIMIT 10"
df = pd.read_sql(query, connection)

# Display data in Streamlit
st.write("Data from Databricks:")
st.write(df)

# Close the connection
connection.close()
