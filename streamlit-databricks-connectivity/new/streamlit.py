import streamlit as st
import requests

# Streamlit UI to collect data
st.title("Send Data to Databricks via FastAPI")

data_input = st.text_input("Enter data to send:")

if st.button("Send"):
    if data_input:
        try:
            response = requests.post("http://localhost:8000/send-data", json={"data": data_input})
            if response.status_code == 200:
                st.success("Data sent successfully!")
            else:
                st.error(f"Failed to send data: {response.json()['detail']}")
        except requests.exceptions.RequestException as e:
            st.error(f"Error sending data: {str(e)}")
    else:
        st.warning("Please enter some data to send.")
