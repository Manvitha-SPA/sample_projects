import streamlit as st
import requests
import pandas as pd
# from .find import main
# df = pd.read_csv(r"C:\Users\S P A_LPT_000\Desktop\chatbotsample\bot\filtered_medquad.csv")
 
# input_data=''
# def search_from_sample_data(input_data):
#     # Check if the user's question matches any data in the 'question' column
#     matching_row = df[df['question'].str.lower() == input_data.lower()]
 
#     if not matching_row.empty:
#         # Retrieve the corresponding 'answer' column data
#         matching_answer = matching_row['answer'].values[0]
#         print(f"Answer: {matching_answer}")
#         output = str(matching_answer)  # Convert the output to a string
#         return output
#     else:
#         print("No matching data found for the given question.")
#         return 'no data'


# input_data=''



import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import spacy
from transformers import pipeline
# from .streamlit import input_text

# st.title('HEALTHCARE BOT')
st.markdown(
    "<h1 style='text-align: center;'>HEALTHCARE BOT</h1>",
    unsafe_allow_html=True,
)



def load_dataset(file_path):
    df = pd.read_csv(file_path)
    columns_to_keep = ['question', 'answer']
    df = df[columns_to_keep]
    return df

def preprocess_answers(df):
    answers = []

    for i in range(0, len(df)):
        if isinstance(df['answer'][i], str):
            review = re.sub('[^a-zA-Z.]', ' ', df['answer'][i])
            review = review.lower()
            review = review.split()
            review = ' '.join(review)
            answers.append(review)
        else:
            answers.append('')

    return [answer.lower() for answer in answers]

def extract_keywords_from_input(user_input, nlp):
    doc = nlp(user_input)
    keywords = [token.lemma_ for token in doc if token.is_alpha and token.pos_ in ['NOUN', 'ADJ', 'VERB']]
    return keywords

def calculate_probabilities(keywords, tokenized_answers):
    probabilities = {
        i: sum(keyword in answer for keyword in keywords) / (len(keywords) + len(set(keywords) & set(answer)))
        for i, answer in enumerate(tokenized_answers)
    }
    return probabilities

# def generate_response(ordered_answers):

#     full_text =ordered_answers
    
#     # Print or use the full text as needed
#     return full_text


def main(input_text):
    # Load dataset
    file_path = r'C:\Users\S P A_LPT_000\Desktop\medicalbot\medical-bot\medquad.csv'
    df = load_dataset(file_path)

    # Preprocess answers
    knowledge_base = preprocess_answers(df)

    # Initialize SpaCy model
    nlp = spacy.load("en_core_web_sm")

    # User input
    user_input =input_text

    if not user_input.strip():
        print("User input is empty. Please provide a valid input.")
    else:
        # Extract keywords
        keywords = extract_keywords_from_input(user_input, nlp)

        # print(f"User Input: {user_input}")
        # print(f"Extracted Keywords: {keywords}")

        # Tokenize the answers without removing stopwords
        tokenized_answers = [word_tokenize(answer.lower()) for answer in knowledge_base]

        # Calculate probabilities
        probabilities = calculate_probabilities(keywords, tokenized_answers)

        # Sort answers based on probabilities
        ordered_answers = [knowledge_base[i] for i in sorted(probabilities, key=probabilities.get, reverse=True)]

        # Set threshold for displaying sentences

        threshold = 0.45

    ord=str(ordered_answers[0])
    # Example usage
    # input_text = ord

    output_summary = bart_summarization(ord)

    # Generate and display response
    # result = generate_response(output)
    return output_summary
    

        
def bart_summarization(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=200, min_length=150, length_penalty=2.0, num_beams=4, early_stopping=True)
    return summary[0]['summary_text']




 
input_text = st.text_input("Search the topic you want").lower()
 
if st.button("Search"):
    response = requests.post("http://localhost:8000/question", json = {"question": input_text})
    if response.status_code == 200:
        output = main(input_text)
        st.write(output.capitalize())
    else:
        st.write("something went wrong") 




