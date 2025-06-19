import streamlit as st
from resume_cleaner_formatter import create_clean_resume

st.set_page_config(page_title="CTI Resume Formatter", layout="centered")

st.title("CTI Resume Formatter")
st.markdown("Upload a resume to generate a clean, CTI-branded version.")

uploaded = st.file_uploader("Upload resume (.pdf, .docx, .txt)", type=["pdf", "docx", "txt"])

if uploaded:
    st.success("File uploaded successfully.")
    if st.button("Generate Clean Resume"):
        doc = create_clean_resume()
        output_path = "Formatted_Resume.docx"
        doc.save(output_path)
        with open(output_path, "rb") as f:
            st.download_button("📥 Download Formatted Resume", f, file_name="Formatted_Resume.docx")
