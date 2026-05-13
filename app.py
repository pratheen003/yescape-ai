import streamlit as st
from utils.website_checker import analyze_website
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

st.subheader("Choose Input Method")

paste_text = st.checkbox("Paste Internship Text")
upload_pdf = st.checkbox("Upload Offer Letter PDF")

user_input = ""

if paste_text:

    text_input = st.text_area(
        "Paste Internship Description or Offer Text"
    )

    user_input += text_input + "\n"

if upload_pdf:

    uploaded_file = st.file_uploader(
        "Upload Offer Letter PDF",
        type=["pdf"]
    )

    if uploaded_file is not None:

        pdf_text = extract_text_from_pdf(uploaded_file)

        user_input += pdf_text

        st.subheader("Extracted PDF Text Preview")

        st.text_area(
            "PDF Content",
            pdf_text,
            height=200
        )
st.subheader("Provide Any Internship Information")

website_url = st.text_input(
    "Company Website URL"
)
user_input = ""

if paste_text == "Paste Text":

    user_input = st.text_area(
        "Paste Internship Description or Offer Text"
    )

elif upload_pdf == "Upload PDF":

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

    if (
    user_input.strip() == ""
    and website_url.strip() == ""
):
        st.warning("Please provide internship text or upload PDF.")

    else:

        website_results = None

        if website_url.strip() != "":
            website_results = analyze_website(website_url)

        result = calculate_yescore(
             user_input,
            website_results
        )

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