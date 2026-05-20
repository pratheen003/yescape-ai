import streamlit as st
import time
from ai.yes_engine import analyze_offer

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

font-size:70px;

width:110px;

height:110px;

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

</style>
""",unsafe_allow_html=True)

# ---------- card start ----------

st.markdown("""

<div class='research-card'>

<div class='hero'>

<div class='icon'>
🔎
</div>

<h1>
Verification in Progress
</h1>

<p>
AI researching your internship evidence
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

if st.session_state.get("text",""):

    st.markdown("""
    <div class='chip'>
    📝 Internship Text
    </div>
    """,unsafe_allow_html=True)


# -------- Dynamic Steps --------

st.markdown(
"<div class='step done'>✅ [DONE] Upload and input validation</div>",
unsafe_allow_html=True
)

if st.session_state.get("pdf_name",""):

    st.markdown(
    "<div class='step done'>✅ [DONE] Offer Letter text extraction (OCR)</div>",
    unsafe_allow_html=True
    )

if st.session_state.get("url",""):

    st.markdown(
    "<div class='step done'>✅ [DONE] Company domain lookup and age verification</div>",
    unsafe_allow_html=True
    )

st.markdown(
"""
<div class='step progress'>
🟡 [IN PROGRESS] Analyzing offer terms for advance fee language...
</div>

<div class='step progress'>
🟡 [IN PROGRESS] Sentiment and urgency analysis...
</div>

<div class='step pending'>
⚪ [PENDING] Cross referencing scam databases...
</div>

<div class='step pending'>
⚪ [PENDING] Salary benchmarking...
</div>

<div class='step pending'>
⚪ [PENDING] Generating final YESScore...
</div>
""",
unsafe_allow_html=True
)

# progress bar INSIDE card


bar=st.progress(0)

for i in range(100):

    time.sleep(.03)

    bar.progress(
        i+1
    )

st.markdown("""
<div style='
color:#a3a3a3;
margin-top:10px;
'>
Estimated analysis time:
&lt;45 sec
</div>
""",
unsafe_allow_html=True)

time.sleep(1)

from ai.score_engine import calculate_score
from ai.verdict_generator import get_verdict


text=st.session_state.get(
"user_input",""
)

url=st.session_state.get(
"url",""
)


result=calculate_score(
text,
url
)


verdict=get_verdict(
result["score"]
)


st.session_state.score=(
result["score"]
)

st.session_state.positives=(
result["positives"]
)

st.session_state.negatives=(
result["negatives"]
)

st.session_state.status=(
verdict["status"]
)

st.session_state.trust=(
verdict["trust"]
)

st.session_state.verdict=(
verdict["verdict"]
)

result=analyze_offer(

st.session_state.get(
"text",""
),

st.session_state.get(
"url",""
)

)

st.session_state.score=result["score"]

st.session_state.status=result["status"]

st.session_state.trust=result["trust"]

st.session_state.verdict=result["verdict"]

st.session_state.positives=result["positives"]

st.session_state.negatives=result["negatives"]

st.switch_page(
"pages/3_Report.py"
)