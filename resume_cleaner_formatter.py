from docx import Document

def create_clean_resume(input_path):
    # Create a new Word document
    doc = Document()

    # Add CTI-styled heading
    doc.add_heading("Ron Burgos", level=0)
    doc.add_paragraph("Construction Project Manager | 25+ Years Experience")

    # Add some placeholder formatting (replace with real parsing later)
    doc.add_heading("Summary", level=1)
    doc.add_paragraph(
        "Seasoned construction leader with deep expertise in HVAC-R, plumbing, electrical systems, "
        "roofing, and facilities management. Proven success managing multimillion-dollar projects "
        "in healthcare, corrections, education, and industrial sectors."
    )

    doc.add_heading("Core Competencies", level=1)
    doc.add_paragraph(
        "- Project Management\n"
        "- MEP Coordination\n"
        "- Budgeting & Estimation\n"
        "- OSHA & Code Compliance\n"
        "- Vendor Relations\n"
        "- Team Supervision"
    )

    doc.add_heading("Experience", level=1)
    doc.add_paragraph("Senior Site Manager – ICONERGY (Denver, CO) – 2019–2024")
    doc.add_paragraph("• Led multimillion-dollar energy retrofitting and infrastructure upgrades across U.S. facilities.")
    doc.add_paragraph("• Supervised large teams and ensured compliance with federal, state, and city codes.")

    # Add more sections here...

    return doc
