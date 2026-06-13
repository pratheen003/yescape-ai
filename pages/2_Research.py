import streamlit as st
import time
from ai.yes_engine import analyze_offer
from ai.research_summary import generate_research_summary
from utils.website_checker import analyze_website

st.set_page_config(
    page_title="Research",
    page_icon="🔍",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------- CSS ----------------

st.markdown("""
<style>

#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

.stApp{
background:
linear-gradient(
180deg,
#060b14,
#02050c
);
}
            
a.anchor-link{
display:none !important;
}

/* main card */

.research-card{

width:780px;

margin:auto;

padding:30px;

background:
rgba(15,20,30,.95);

border-radius:30px;

border:1px solid rgba(
0,255,150,.08
);

box-shadow:
0 0 30px rgba(
0,255,150,.08);

}

/* smaller top card */

.hero{

padding:20px;

margin-bottom:25px;

text-align:center;
}

.hero h1{

font-size:34px;

color:white;

margin-bottom:8px;

}

.hero p{

color:#a4a8b2;
font-size:18px;
}

/* search icon */

.icon{

font-size:55px;

width:120px;

height:120px;

background:
linear-gradient(
145deg,
rgba(29,231,130,.15),
rgba(20,198,109,.05)
);

backdrop-filter:blur(10px);

margin:auto;

border-radius:100%;

display:flex;

justify-content:center;

align-items:center;

border:5px solid #18d96b;

box-shadow:
0 0 25px rgba(
0,255,150,.35);

margin-bottom:20px;

}

/* chips */

.chip{

padding:14px;

border-radius:16px;

background:
rgba(255,255,255,.04);

margin-top:10px;

color:#56a8ff;

font-size:18px;

}

/* progress */

.bar{

height:15px;

background:
rgba(255,255,255,.08);

border-radius:30px;

overflow:hidden;

margin-top:30px;

}

.fill{

height:100%;

width:70%;

background:
linear-gradient(
90deg,
#18d96b,
#14d6a0
);

border-radius:30px;

}

.step{

font-size:18px;
margin-top:15px;

}

.done{

color:#22c55e;

}

.progress{

color:#facc15;

}

.pending{

color:#c4c4d8;

}
            

@media (max-width:768px){

.research-card{
    padding:20px;
}

.research-icon{
    font-size:24px;
}

}

</style>
""",unsafe_allow_html=True)

# ---------- card start ----------

st.markdown("""

<div class='research-card'>

<div class='hero'>

<div class='icon'>
🔍
</div>

<h1>
YESCAPE Investigation Engine
</h1>

<p>
AI is validating company trust,
offer legitimacy and scam indicators
</p>

</div>

""",unsafe_allow_html=True)


# ---------- input chips ----------

st.markdown("""

<br>

""",unsafe_allow_html=True)

if st.session_state.get("url",""):

    st.markdown("""
    <div class='chip'>
    🔗 Website URL
    </div>
    """,unsafe_allow_html=True)

if st.session_state.get("pdf_name",""):

    st.markdown(f"""
    <div class='chip'>
    📄 {st.session_state.pdf_name}
    </div>
    """,unsafe_allow_html=True)

if st.session_state.get(
    "manual_text",
    False
):

    st.markdown("""
    <div class='chip'>
    📝 Internship Text
    </div>
    """,unsafe_allow_html=True)

# -------- Dynamic Steps --------

st.markdown(
"""
<div class='step done'>
✅ Input validation completed
</div>
""",
unsafe_allow_html=True
)

if st.session_state.get("pdf_name",""):

    st.markdown(
    """
    <div class='step done'>
    ✅ Offer letter successfully parsed
    </div>
    """,
    unsafe_allow_html=True
    )

if st.session_state.get("url",""):

    st.markdown(
    """
    <div class='step done'>
    ✅ Company website identified
    </div>
    """,
    unsafe_allow_html=True
    )

st.markdown(
"""
<div class='step progress'>
🟡 Scam pattern detection running...
</div>

<div class='step progress'>
🟡 Trust score calculation running...
</div>

<div class='step pending'>
⚪ Cross referencing scam databases...
</div>

<div class='step pending'>
⚪ Final YES Score generation
</div>
""",
unsafe_allow_html=True
)

# progress bar INSIDE card

st.markdown("""

<br>

""",unsafe_allow_html=True)

bar=st.progress(0)

for i in range(100):

    time.sleep(.01)

    bar.progress(
        i+1
    )

st.markdown("""
<div style="
padding:18px;
border-radius:18px;
background:rgba(255,255,255,.03);
border:1px solid rgba(0,255,150,.08);
margin-top:20px;
margin-bottom:20px;
">

<div style="
font-size:18px;
font-weight:600;
color:white;
margin-bottom:10px;
">
AI Investigation Summary
</div>

<div style="color:#a4a8b2;">
• Company legitimacy checks<br>
• Domain trust validation<br>
• Scam phrase detection<br>
• Urgency analysis<br>
• YES Score generation
</div>

</div>
""",unsafe_allow_html=True)


st.markdown("""
<div style='
color:#a3a3a3;
margin-top:10px;
'>
AI Confidence Engine Active

Estimated completion:
10-20 seconds
</div>
""",
unsafe_allow_html=True)

from ai.score_engine import calculate_score
from ai.verdict_generator import get_verdict


text=st.session_state.get(
"user_input",""
)

url=st.session_state.get(
"url",""
)

research = generate_research_summary(
    text,
    url
)


st.session_state.company=(
research["company"]
)

st.session_state.company_status=(
research["company_status"]
)

st.session_state.domain_reputation=(
research["domain_reputation"]
)

result=analyze_offer(

st.session_state.get(
"text",""
),

st.session_state.get(
"url",""
)

)

st.session_state.reasoning = (
    result["reasoning"]
)

st.session_state.confidence_data = (
    result["confidence_data"]
)

st.session_state.trust_data = (
    result["trust_data"]
)

st.session_state.domain_age = (
    result["domain_age"]
)

st.session_state.https_status = (
    result["https_status"]
)

st.session_state.score=result["score"]

st.session_state.status=result["status"]

st.session_state.trust=result["trust"]

st.session_state.verdict=result["verdict"]

st.session_state.positives=result["positives"]

st.session_state.negatives=result["negatives"]

if "history" not in st.session_state:

    st.session_state.history=[]


history_item={

"score":result["score"],

"status":result["status"],

"verdict":result["verdict"],

"url":st.session_state.get(
"url",
""
),

"pdf":st.session_state.get(
"pdf_name",
""
)

}


st.session_state.history.insert(
0,
history_item
)


st.session_state.history=(
st.session_state.history[:5]
)

st.switch_page(
"pages/3_Report.py"
)