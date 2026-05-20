import streamlit as st

st.set_page_config(
    page_title="YESScore Report",
    page_icon="🛡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# -------------------------
# INPUT DATA
# -------------------------

url = st.session_state.get("url","")
pdf = st.session_state.get("pdf_name","")
text = st.session_state.get("text","")

combined=(text+" "+url).lower()


# -------------------------
# SCORE ENGINE
# -------------------------

score=40

if url:
    score+=20

if pdf:
    score+=30

if text:
    score+=10


scam_words=[

"pay registration fee",
"certificate fee",
"urgent joining",
"pay now",
"limited slots",
"guaranteed internship"

]

for word in scam_words:

    if word in combined:

        score-=20


score=max(
0,
min(score,100)
)


# -------------------------
# STATUS
# -------------------------

if score>=80:

    trust="SAFE"

    glow="#1de782"

    verdict="AI found strong legitimacy indicators."

    trustline="HIGH TRUST"

elif score>=60:

    trust="CAUTION"

    glow="#facc15"

    verdict="Mixed signals detected."

    trustline="MEDIUM TRUST"

elif score>=40:

    trust="RISKY"

    glow="#ff8c00"

    verdict="Multiple suspicious indicators detected."

    trustline="LOW TRUST"

else:

    trust="SCAM ALERT"

    glow="#ef4444"

    verdict="High probability of internship scam."

    trustline="VERY LOW TRUST"



confidence=min(
95,
score+10
)


# -------------------------
# CSS
# -------------------------

st.markdown(f"""
<style>

#MainMenu{{visibility:hidden;}}
footer{{visibility:hidden;}}
header{{visibility:hidden;}}

.stApp{{
background:
linear-gradient(
180deg,
#080c14,
#050811
);
}}

.card{{
width:760px;
margin:auto;
padding:25px;
border-radius:30px;
background:
rgba(15,20,30,.95);

border:1px solid rgba(
255,255,255,.05
);

box-shadow:
0 0 30px {glow};

margin-top:25px;
}}

.scorebox{{

text-align:center;

padding:15px;

}}

.score{{

font-size:70px;

font-weight:700;

color:{glow};

}}

.tag{{

color:{glow};

font-size:24px;

font-weight:700;

}}

.small{{

color:#a4a8b2;

font-size:15px;

}}

.subcard{{

padding:20px;

border-radius:20px;

background:
rgba(255,255,255,.03);

min-height:220px;

}}

.green{{
border-left:4px solid #1de782;
}}

.red{{
border-left:4px solid #ef4444;
}}

</style>
""",unsafe_allow_html=True)


# -------- SCORE CARD --------

score=st.session_state.get(
"score",
50
)

status=st.session_state.get(
"status",
"UNKNOWN"
)

trust=st.session_state.get(
"trust",
"MEDIUM"
)

verdict=st.session_state.get(
"verdict",
"No analysis"
)

score_color="#1de782"
glow="rgba(29,231,130,.45)"

st.markdown(f"""
<style>

.score-card{{
background:#09111f;
border-radius:28px;
padding:25px 35px;
display:flex;
align-items:center;
justify-content:space-between;
gap:30px;

border:1px solid {score_color};

box-shadow:
0 0 40px {glow};

margin-top:15px;
margin-bottom:18px;
}}

.left-zone{{
display:flex;
align-items:center;
gap:25px;
}}

.gauge-wrap{{
position:relative;
width:130px;
height:80px;
}}

.gauge{{
width:130px;
height:65px;

border:
10px solid {score_color};

border-bottom:none;

border-radius:
130px 130px 0 0;

box-shadow:
0 0 25px {glow};
}}

.score-right{{
display:flex;
flex-direction:column;
}}

.score-num{{
font-size:55px;
font-weight:800;
color:{score_color};
line-height:1;
}}

.score-text{{
font-size:16px;
color:#9ca3af;
margin-top:8px;
}}

.status{{
font-size:24px;
font-weight:700;
color:{score_color};

margin-top:8px;
}}

.verdict-box{{
max-width:300px;
}}

.verdict-title{{
font-size:17px;
font-weight:700;
color:white;
margin-bottom:10px;
}}

.verdict-text{{
color:#aab1be;
font-size:15px;
line-height:1.6;
}}

</style>


<div class='score-card'>

<div class='left-zone'>

<div class='gauge-wrap'>
<div class='gauge'></div>
</div>

<div class='score-right'>

<div class='score-num'>
{score}/100
</div>

<div class='status'>
{status}
</div>

<div class='score-text'>
{trust}
</div>

</div>

</div>


<div class='verdict-box'>

<div class='verdict-title'>
AI Verdict
</div>

<div class='verdict-text'>
{verdict}
</div>

</div>

</div>

""",unsafe_allow_html=True)

# -------------------------
# GET USER INPUT DATA
# -------------------------

user_text = st.session_state.get(
    "text",
    ""
)

url_text = st.session_state.get(
    "url",
    ""
)

pdf_name = st.session_state.get(
    "pdf_name",
    ""
)

# -------------------------
# DETECT SIGNALS
# -------------------------

positive=[]
negative=[]

text_data = (user_text + " " + url_text).lower()

# Positive signals

if "company" in text_data:
    positive.append(
    "Professional contact structure detected"
    )

if "internship" in text_data:
    positive.append(
    "Detailed internship description found"
    )

if "@" in text_data:
    positive.append(
    "Email/contact information available"
    )


# Risk signals

risky_words=[
"registration fee",
"payment",
"urgent",
"immediate joining",
"training fee",
"deposit"
]

for word in risky_words:

    if word in text_data:

        negative.append(
        f"Detected risky terms: {word}"
        )


if "urgent" in text_data:

    negative.append(
    "Urgency wording: urgent"
    )


# fallback

if len(positive)==0:

    positive.append(
    "No major positive indicators found"
    )


if len(negative)==0:

    negative.append(
    "No risk indicators detected"
    )

# -------------------------
# SIGNALS
# -------------------------

positives = st.session_state.get("positives", [])
negatives = st.session_state.get("negatives", [])

if len(positives)==0:
    positives=["No major positive indicators found"]

if len(negatives)==0:
    negatives=["No risk indicators detected"]


positive_html=""

for item in positives:

    positive_html += f"""
    <p style="
    color:white;
    font-size:18px;
    margin:12px 0;
    ">
    ✔ {item}
    </p>
    """


negative_html=""

for item in negatives:

    negative_html += f"""
    <p style="
    color:white;
    font-size:18px;
    margin:12px 0;
    ">
    ⚠ {item}
    </p>
    """


col1,col2=st.columns(2)


with col1:

    st.markdown(f"""
    <div class="subcard green">

    <div style="
    font-size:30px;
    font-weight:700;
    margin-bottom:25px;
    ">

    🟢 Green Flags

    </div>

    {positive_html}

    </div>
    """,unsafe_allow_html=True)



with col2:

    st.markdown(f"""
    <div class="subcard red">

    <div style="
    font-size:30px;
    font-weight:700;
    margin-bottom:25px;
    ">

    🔴 Red Flags

    </div>

    {negative_html}

    </div>
    """,unsafe_allow_html=True)
# -------------------------
# AI ANALYSIS
# -------------------------

st.markdown("""

<br>

""",unsafe_allow_html=True)

st.markdown("""
<div class='card'>
<h3>
🤖 AI Analysis
</h3>
</div>
""",unsafe_allow_html=True)

st.markdown("""

<br>

""",unsafe_allow_html=True)

st.progress(
confidence/100
)

st.caption(
f"AI Confidence: {confidence}%"
)

st.info(
f"""
YESCAPE AI analyzed your internship using:

• company indicators

• language patterns

• payment wording

• urgency detection

• trust heuristics

Final verdict:

{verdict}
"""
)



# -------------------------
# BUTTONS
# -------------------------

c1,c2=st.columns(2)

with c1:

    st.button(
    "📄 Download Report"
    )

with c2:

    if st.button(
    "🔄 Scan Again"
    ):

        st.switch_page(
        "app.py"
        )