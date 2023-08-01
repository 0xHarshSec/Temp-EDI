import streamlit as st
import PyPDF2

# Set page title
st.set_page_config(page_title="PDF Text Extractor")

# Set page header
st.title("PDF Text Extractor")

# Display file upload widget
file = st.file_uploader("Upload a PDF file", type=["pdf"])

# If user uploaded a file
if file is not None:

    # Open the uploaded file in read-binary mode
    pdf_reader = PyPDF2.PdfFileReader(file, strict=False)

    # Initialize empty string to store text content of PDF
    text = ""

    # Iterate over all pages in the PDF
    for i in range(pdf_reader.getNumPages()):
        # Get the text content of the current page and add it to the overall string
        text += pdf_reader.getPage(i).extractText()

    # Display the text content
    st.write(text)