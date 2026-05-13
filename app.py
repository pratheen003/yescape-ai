import streamlit as st

from backend.scoring import calculate_yescore
from utils.pdf_parser import extract_text_from_pdf

st.set_page_config(
    page_title="YESCAPE AI",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ YESCAPE AI")
st.subheader("AI Internship Scam Detection System")

st.write("Analyze internship descriptions and offer letters using AI-powered trust scoring.")

input_option = st.radio(
    "Choose Input Type",
    ["Paste Text", "Upload PDF"]
)

user_input = ""

if input_option == "Paste Text":

    user_input = st.text_area(
        "Paste Internship Description or Offer Text"
    )

elif input_option == "Upload PDF":

    uploaded_file = st.file_uploader(
        "Upload Offer Letter PDF",
        type=["pdf"]
    )

    if uploaded_file is not None:

        user_input = extract_text_from_pdf(uploaded_file)

        st.subheader("Extracted Text Preview")

        st.text_area(
            "PDF Content",
            user_input,
            height=200
        )

if st.button("Analyze Internship"):

    if user_input.strip() == "":
        st.warning("Please provide internship text or upload PDF.")

    else:

        result = calculate_yescore(user_input)

        st.markdown(
            f"""
            ## YEScore: :{result['color']}[{result['score']}/100]
            ### Status: :{result['color']}[{result['status']}]
            """
        )

        st.subheader("Detection Reasons")

        if result["reasons"]:

            for reason in result["reasons"]:
                st.write(f"⚠️ {reason}")

        else:
            st.success("No major scam signals detected.")