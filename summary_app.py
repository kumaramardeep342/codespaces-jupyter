import os
import streamlit as st
import google.generativeai as genai
from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain_google_genai import GoogleGenerativeAI

def generate_response(txt, api_key):
    # Configure the API key
    os.environ['GOOGLE_API_KEY'] = api_key
    genai.configure(api_key=api_key)

    # Instantiate the LLM model
    llm = GoogleGenerativeAI(model="gemini-pro", temperature=0)
    
    # Split text
    text_splitter = CharacterTextSplitter()
    texts = text_splitter.split_text(txt)
    
    # Create multiple documents
    docs = [Document(page_content=t) for t in texts]
    
    # Text summarization
    chain = load_summarize_chain(llm, chain_type='map_reduce')
    return chain.run(docs)

# Page title
st.set_page_config(page_title='🔍 Text Summarization App')
st.title('🔍 Gemini Text Summarization App')

# Text input
txt_input = st.text_area('Enter your text', '', height=200)

# Form to accept user's text input for summarization
result = []
with st.form('summarize_form', clear_on_submit=True):
    gemini_api_key = st.text_input('Google AI API Key', type='password', disabled=not txt_input)
    submitted = st.form_submit_button('Submit')
    if submitted and gemini_api_key:
        with st.spinner('Calculating...'):
            try:
                response = generate_response(txt_input, gemini_api_key)
                result.append(response)
            except Exception as e:
                st.error(f"An error occurred: {e}")

if len(result):
    st.info(response)

# Instructions for getting a Gemini API key
st.subheader("Get a Google AI API key")
st.write("""
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click on `Create API Key`
3. Copy the generated API key
""")