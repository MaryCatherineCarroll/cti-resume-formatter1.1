import streamlit as st
from resume_cleaner_formatter import create_clean_resume

st.set_page_config(page_title="CTI Resume Formatter", layout="centered")
st.title("CTI Resume Formatter")
st.markdown("Upload a resume to generate a clean formatted version.")

uploaded = st.file_uploader("Upload resume (.pdf, .docx, .txt)", type=["pdf", "docx", "txt"])
if uploaded:
    st.success("File uploaded — click below to generate.")
    if st.button("Generate Clean Resume"):
        doc = create_clean_resume()
        doc.save("Formatted_Resume.docx")
        with open("Formatted_Resume.docx", "rb") as f:
            st.download_button("Download here 👇", f, "Formatted_Resume.docx")
