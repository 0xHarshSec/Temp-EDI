# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WUYVGUWMa3zYZ8ZHkUBD-LHwU7onjIDY
"""


import streamlit as st
import fitz
'''import spacy'''


# Load the NLP model
'''nlp = spacy.load("en_core_web_sm")'''


# Define a function to extract text from a PDF file
def extract_text(pdf_file):
    doc = fitz.open(pdf_file)
    text = ""
    for page in doc:
        text += page.getText()
    return text


# Define the Streamlit app
def app():
    st.title("PDF Text Summarizer")

    # Allow the user to upload a PDF file
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    # If a file was uploaded, extract the text and summarize it
    if uploaded_file is not None:
        st.write("Extracting text from PDF file...")
        text = extract_text(uploaded_file)
        st.write("Summarizing text...")

        # Process the text with the NLP model and extract the summary
        '''doc = nlp(text)
        sentences = [sent for sent in doc.sents]
        num_sentences = len(sentences)
        num_summary_sentences = int(num_sentences * 0.2)  # 20% summary length
        summary_sentences = sentences[:num_summary_sentences]
        summary_text = " ".join(str(sent) for sent in summary_sentences)'''

        # Display the original text and the summary
        st.subheader("Original Text")
        st.write(text)
        '''st.subheader("Summary")
        st.write(summary_text)'''


# Run the app
app()
