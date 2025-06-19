import streamlit as st
from resume_cleaner_formatter import create_clean_resume
import tempfile
import os

st.set_page_config(
    page_title="CTI Resume Formatter",
    layout="centered"
)

# ---- PAGE HEADER ----
st.title("CTI Resume Formatter")
st.markdown("Upload a resume (PDF, DOCX, or TXT) to generate a clean, CTI-formatted version.")

# ---- FILE UPLOADER ----
uploaded_file = st.file_uploader("Choose a resume file", type=["pdf", "docx", "txt"])

if uploaded_file is not None:
    st.success("Resume uploaded successfully!")

    # Optional: show filename
    st.write(f"**File:** `{uploaded_file.name}`")

    # ---- GENERATE FORMATTED VERSION ----
    if st.button("Generate Formatted Resume"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[-1]) as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        # Process resume
        formatted_resume = create_clean_resume(tmp_path)

        # Save to file
        output_path = "CTI_Formatted_Resume.docx"
        formatted_resume.save(output_path)

        # Download button
        with open(output_path, "rb") as f:
            st.download_button(
                label="📄 Download CTI-Formatted Resume",
                data=f,
                file_name="CTI_Formatted_Resume.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
