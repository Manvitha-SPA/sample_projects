import streamlit as st
from pymongo import MongoClient
import pandas as pd

st.title('Data obtained from the MongoDB')
# st.prompt()
@st.cache_resource
def init_connection():
    # cli = MongoClient('mongodb+srv://bmanvitha2001:CRGQVOiYvQjNWmI2@samplecluster.77pjmuv.mongodb.net/')
    cli=MongoClient('mongodb+srv://bmanvitha2001:CRGQVOiYvQjNWmI2@mongocluster.wcswblu.mongodb.net/')
    return cli

client = init_connection()
# db = client.sample
db=client.Ecourts_db

@st.cache_data(ttl=600)
def get_universities():
    # collection = db['work1'].find({})    
    collection = db['ecourts'].find({})
    return pd.DataFrame(collection)

universities = get_universities()
st.write(universities)
