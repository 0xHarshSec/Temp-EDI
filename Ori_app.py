import pandas as pd
import numpy as np
import nltk
global text_input
import streamlit as st
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords





data = "A random paragraph can also be an excellent way for a writer to tackle writers' block. Writing block can often happen due to being stuck with a current project that the writer is trying to complete. By inserting a completely random paragraph from which to begin, it can take down some of the issues that may have been causing the writers' block in the first place."


def solve(text):
    stopwords1 = set(stopwords.words("english"))
    words = word_tokenize(text)
    freqTable = {}
    for word in words:
        word = word.lower()
        if word in stopwords1:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1

    sentences = sent_tokenize(text)
    sentenceValue = {}
    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else:
                    sentenceValue[sentence] = freq

    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]

    average = int(sumValues / len(sentenceValue))

    summary = ''
    for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
            summary += " " + sentence

    return summary


# Text Similarity percentage calculator

from difflib import SequenceMatcher



from PIL import Image
import streamlit as st
import PyPDF2
st.set_page_config(page_title="My Streamlit App", page_icon=":guardsman:", layout="wide")
# Add image
image = Image.open("cool text summarizer.png")
st.image(image, caption="Summariser", width=300)


# Set page header
st.title("PDF Text Extractor and Summariser")

# Display file upload widget
file = st.file_uploader("Upload a PDF file", type=["pdf"])

# Get text input from user



# If user uploaded a file
if file is not None:

    # Open the uploaded file in read-binary mode
    pdf_reader = PyPDF2.PdfReader(file, strict=False)

    # Initialize empty string to store text content of PDF
    text = ""

    # Iterate over all pages in the PDF
    for i in range(len(pdf_reader.pages)):
        # Get the text content of the current page and add it to the overall string
        text += pdf_reader.pages[i].extract_text()

        st.write(solve(text))
        a = solve(text)


        def text_similarity(str1, str2):
            # calculate the similarity ratio using SequenceMatcher
            similarity_ratio = SequenceMatcher(None, str1, str2).ratio()
            # return the percentage similarity by multiplying by 100
            return similarity_ratio * 100


        # example usage

        # Get text input from user
        text_input = st.text_area("Enter text here for similarity rating:")

        # Display the text input
        st.write("You entered:", text_input)

        string1 = text_input
        string2 = a
        similarity = text_similarity(string1, string2)
        st.write(f"The similarity between the two strings is {similarity}%")

