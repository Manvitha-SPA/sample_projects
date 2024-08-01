from pydantic import BaseModel
# from .streamlit import input_text


class Question(BaseModel):
    question : str

