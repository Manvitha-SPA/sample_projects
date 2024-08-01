# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from sqlalchemy import create_engine
# import pandas as pd

# app = FastAPI()

# # Define Pydantic models for request and response payloads
# class DataRequest(BaseModel):
#     data: str

# # Example SQLAlchemy engine setup (replace with your Databricks connection details)
# hostname = "community.cloud.databricks.com"
# port = 443
# databricks_token = "abc123"

# connection_str = (
#     f"Driver=Simba Spark ODBC Driver;"
#     f"Host={hostname};"
#     f"Port={port};"
#     "TransportMode=http;"
#     "SSL=1;"
#     "AuthMech=3;"
#     f"UID=token;"
#     f"PWD={databricks_token};"
# )

# engine = create_engine("mssql+pyodbc://", connect_args={'connection_string': connection_str})

# # Function to insert data into Databricks (replace with your actual logic)
# def insert_data_into_databricks(data: str):
#     try:
#         # Example SQL statement
#         query = f"INSERT INTO your_table (column_name) VALUES ('{data}')"
#         with engine.connect() as con:
#             con.execute(query)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error inserting data: {str(e)}")

# # FastAPI endpoint to receive data from Streamlit
# @app.post("/send-data")
# def send_data(data_request: DataRequest):
#     data = data_request.data
#     insert_data_into_databricks(data)
#     return {"message": "Data received and sent to Databricks"}

# # Optional endpoint to test if FastAPI server is running
# @app.get("/")
# def read_root():
#     return {"message": "FastAPI server is running"}

# # Run FastAPI server with uvicorn
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)
# 10/06/2024
#load the dataframe
from pyspark.sql.functions import *
from pyspark.sql import SparkSession
spark=SparkSession.builder.appName('Sample_session').getOrCreate()

simpleData = [("James","Sales","NY",90000,34,10000),
    ("Michael","Sales","NY",86000,56,20000),
    ("Robert","Sales","CA",81000,30,23000),
    ("Maria","Finance","CA",90000,24,23000),
    ("Raman","Finance","CA",99000,40,24000),
    ("Scott","Finance","NY",83000,36,19000),
    ("Jen","Finance","NY",79000,53,15000),
    ("Jeff","Marketing","CA",80000,25,18000),
    ("Kumar","Marketing","NY",91000,50,21000)
  ]

schema = ["Employee_name","Department","State","Salary","Age","Bonus"]
simpleData_df = spark.createDataFrame(data=simpleData, schema = schema)
simpleData_df.printSchema()
simpleData_df.show(truncate=False)