import streamlit as st
from pypdf import PdfReader

from utils.analyzer import (
    detect_skills,
    suggest_roles,
    get_missing_skills
)


st.set_page_config(
    page_title="Resume Analyzer",
    page_icon="📄"
)

st.title("📄 Resume Analyzer")
st.write(
    "Upload your resume and get an instant analysis of "
    "your skills and suitable job roles."
)


uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)


if uploaded_file is not None:

    st.success("Resume uploaded successfully! ✅")

    reader = PdfReader(uploaded_file)

    resume_text = ""

    for page in reader.pages:
        text = page.extract_text()

        if text:
            resume_text += text + "\n"


    if resume_text.strip():

        # Detect skills
        detected_skills = detect_skills(resume_text)

        st.subheader("🔍 Detected Skills")

        if detected_skills:
            st.write(", ".join(detected_skills))
        else:
            st.warning("No matching skills were detected.")


        # Suggest job roles
        suggested_roles = suggest_roles(detected_skills)

        st.subheader("💼 Suggested Job Roles")

        for role, score in suggested_roles:

            st.write(
                f"**{role}** — {score}% skill match"
            )

            missing_skills = get_missing_skills(
                detected_skills,
                role
            )

            if missing_skills:

                st.write(
                    "⚠️ Missing skills: "
                    + ", ".join(missing_skills)
                )

            else:

                st.success(
                    "You have all the required skills for this role! ✅"
                )


    else:

        st.error(
            "Could not extract text from this PDF. "
            "Please upload a text-based PDF."
        )