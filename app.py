import streamlit as st
from resume_cleaner_formatter import create_clean_resume

st.set_page_config(page_title="CTI Resume Formatter", layout="centered")

st.title("CTI Resume Formatter")
st.markdown("Upload a resume (PDF, DOCX, or TXT) and get a formatted, branded version.")

uploaded_file = st.file_uploader("Choose a resume file", type=["pdf", "docx", "txt"])


if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        from PyPDF2 import PdfReader
        reader = PdfReader(uploaded_file)
        resume_text = "\n".join([page.extract_text() for page in reader.pages])
    elif uploaded_file.type == "text/plain":
        resume_text = uploaded_file.read().decode("utf-8")
    else:
        from docx import Document
        doc = Document(uploaded_file)
        resume_text = "\n".join([para.text for para in doc.paragraphs])

    st.success("Resume uploaded and extracted. Generating formatted version...")
    formatted_doc = create_clean_resume()
    output_path = "/mnt/data/Formatted_Resume.docx"
    formatted_doc.save(output_path)

    with open(output_path, "rb") as f:
        st.download_button("Download Formatted Resume", f, file_name="Formatted_Resume.docx")