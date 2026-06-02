import streamlit as st
from utils.pdf_parser import extract_text_from_pdf

if "scan_history" not in st.session_state:
    st.session_state.scan_history=[]

st.set_page_config(
    page_title="Verification",
    page_icon="🛡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# -------- Session --------

if "user_input" not in st.session_state:
    st.session_state.user_input=""

if "website_url" not in st.session_state:
    st.session_state.website_url=""

# -------- CSS --------

st.markdown("""
<style>

#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

.stApp{
background:
linear-gradient(
180deg,
#080c14,
#050811
);
}

/* remove anchor link icon */
a.anchor-link{
display:none !important;
}

/* heading */

.main-title{
text-align:center;
font-size:58px;
font-weight:700;
color:white;

line-height:1.2;

margin-top:20px;
margin-bottom:10px;
}

.sub-title{

text-align:center;

color:#a4a8b2;

font-size:18px;

margin-bottom:30px;
}
            
.status-pill{

width:240px;

margin:auto;

margin-top:18px;

margin-bottom:25px;

padding:10px 18px;

text-align:center;

font-size:15px;

font-weight:600;

color:#19f589;

background:rgba(25,245,137,.08);

border:1px solid rgba(25,245,137,.18);

border-radius:999px;

box-shadow:
0 0 18px rgba(
25,245,137,.08
);

}

/* floating card */

.verify-card{

width:850px;

margin:auto;

margin-top:20px;

padding:30px;

background:
rgba(15,20,30,.95);

border-radius:30px;

border:1px solid rgba(
0,255,150,.08
);

box-shadow:

0 20px 60px rgba(
0,0,0,.45),

0 0 30px rgba(
0,255,140,.08);

}

/* top empty bar */

.glow-bar{

height:70px;

border-radius:35px;

background:
rgba(255,255,255,.02);

border:
1px solid rgba(
0,255,150,.12
);

margin-bottom:20px;

transition:.4s;
}

.glow-bar:hover{

transform:translateY(-2px);

box-shadow:

0 0 25px rgba(
0,255,150,.25);

}

/* checkbox pill cards */

.stCheckbox{

background:
rgba(255,255,255,.03);

padding:16px;

border-radius:20px;

border:
1px solid rgba(
255,255,255,.08
);

text-align:center;

transition:.3s;

min-height:72px;

display:flex;

align-items:center;

justify-content:center;

backdrop-filter:blur(12px);

}

.stCheckbox:hover{

transform:
translateY(-4px);

border:
1px solid #19f589;

box-shadow:

0 0 25px rgba(
25,245,137,.18
);

}

/* checked becomes green */

.stCheckbox:has(input:checked){

background:
linear-gradient(
135deg,
rgba(25,245,137,.15),
rgba(25,245,137,.05)
);

border:
1px solid #19f589;

box-shadow:

0 0 25px rgba(
25,245,137,.25
);

}

/* upload box */

[data-testid=
"stFileUploader"]{

border:
2px dashed rgba(
255,255,255,.15
);

padding:25px;

border-radius:20px;

background:
rgba(255,255,255,.02);

}

/* run button */

.stButton>button{

width:100%;

height:58px;

background:
linear-gradient(
90deg,
#1de782,
#13c66d
);

border:none;

border-radius:16px;

font-size:18px;

font-weight:700;

color:white;

box-shadow:

0 0 25px
rgba(
29,231,130,.4);

transition:.3s;
}

.stButton>button:hover{

transform:
scale(1.02);

}

</style>
""",unsafe_allow_html=True)

st.markdown("""

<div class='main-title'>
Start Your Verification
</div>

<div class='sub-title'>
Upload internship evidence and let
YEScape perform a complete trust analysis.
</div>

<div class='status-pill'>
🟢 AI Verification Ready
</div>

""",unsafe_allow_html=True)


st.markdown(
"<div class='glow-bar'></div>",
unsafe_allow_html=True
)



# ---------- top checkboxes ----------

col1,col2,col3=st.columns(3)

with col1:
    add_url=st.checkbox(
        "🌐 Add URL"
    )

with col2:
    add_pdf=st.checkbox(
        "📄 Upload PDF"
    )

with col3:
    add_text=st.checkbox(
        "📝 Paste Text"
    )


# default values

url=""
text=""
manual_text=False
pdf_text=""
uploaded_file=None


# ---------- URL ----------

if add_url:

    url=st.text_input(
        "Company Website URL"
    )


# ---------- PDF ----------

if add_pdf:

    uploaded_file=st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if uploaded_file:

        pdf_text=extract_text_from_pdf(
            uploaded_file
        )


# ---------- TEXT ----------

if add_text:

    manual_text=True

    text=st.text_area(
        "Paste Internship Text"
    )


# combine all text inputs

combined_text=(
    text+"\n"+pdf_text
)


# save session

st.session_state.user_input=combined_text

st.session_state.website_url=url



# ---------- BUTTON ----------

if st.button(
    "RUN AI VERIFICATION"
):

    if(
        combined_text.strip()==""
        and
        url.strip()==""
    ):

        st.warning(
            "Select and provide at least one input"
        )

    else:

        st.session_state.url=url

        st.session_state.text=text


        if uploaded_file:

            st.session_state.pdf_name=uploaded_file.name

            pdf_text=extract_text_from_pdf(
                uploaded_file
            )

            st.session_state.text=(

                st.session_state.get(
                "text",""
                )

                +

                "\n"

                +

                pdf_text

            )

        else:

            st.session_state.pdf_name=""


        # -------------------------
        # SAVE SCAN HISTORY
        # -------------------------

        preview=""

        if url.strip()!="":

            preview=url.strip()

        elif text.strip()!="":

            preview=text.strip()[:60]

        elif uploaded_file:

            preview=uploaded_file.name

        else:

            preview="Internship Scan"


        preview=preview.replace("*","")


        new_scan={

            "title":preview,
            "status":"SAFE"

        }


        already_exists=False

        for item in st.session_state.scan_history:

            existing_title = item.get(
                "title",
                item.get(
                    "text",
                    ""
                )
            )

            if existing_title == preview:

                already_exists=True
                break


        if not already_exists:

            st.session_state.scan_history.insert(
                0,
                new_scan
            )


        st.session_state.scan_history=(
            st.session_state.scan_history[:5]
        )

        st.session_state.manual_text = manual_text

        st.switch_page(
            "pages/2_Research.py"
        )

# -------------------------
# RECENT SCANS
# -------------------------

st.markdown("""

<div style="
font-size:22px;
font-weight:700;
margin-top:40px;
margin-bottom:18px;
color:white;
">
🕘 Recent Activity
</div>

""", unsafe_allow_html=True)


history = st.session_state.get(
    "scan_history",
    []
)

# latest first
history = history[::-1]


for item in history[:5]:

    # safe title detection

    if "title" in item and item["title"].strip()!="":

        title=item["title"]

    elif "text" in item and item["text"].strip()!="":

        title=item["text"][:60]

    else:

        continue


    score=item.get(
        "score",
        70
    )

    # DOT COLOR

    if score >= 80:

        dot = "#19f589"

    elif score >= 60:

        dot = "#facc15"

    else:

        dot = "#ff4b5c"


    st.markdown(f"""

<div style="
padding:18px 20px;
box-shadow:
0 0 18px rgba(
255,255,255,.02);
border-radius:18px;
background:rgba(255,255,255,.03);
border:1px solid rgba(255,255,255,.06);
margin-bottom:14px;
display:flex;
justify-content:space-between;
align-items:center;
">

<div style="
color:white;
font-size:16px;
font-weight:500;
overflow:hidden;
">
{title}
</div>

<div style="
width:14px;
height:14px;
border-radius:50%;
background:{dot};
box-shadow:0 0 14px {dot};
flex-shrink:0;
">
</div>

</div>

""", unsafe_allow_html=True)