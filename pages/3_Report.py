import streamlit as st
from utils.report_generator import generate_report
from ai.verdict_generator import get_verdict


st.set_page_config(

page_title="YESScore Report",

page_icon="🛡",

layout="centered",

initial_sidebar_state="collapsed"

)

#-------------------------

#INPUT DATA

#-------------------------

url = st.session_state.get("url","")

pdf = st.session_state.get("pdf_name","")

text = st.session_state.get("text","")

combined=(text+" "+url).lower()

#-------------------------

#SCORE ENGINE

#-------------------------

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

#-------------------------

#STATUS

#-------------------------

result = get_verdict(
    score,
    st.session_state.get("positives", []),
    st.session_state.get("negatives", [])
)

status = result["status"]

trustline = result["trust"]

verdict = result["verdict"]


if status == "SAFE":

    glow="#1de782"

elif status == "CAUTION":

    glow="#facc15"

elif status == "RISKY":

    glow="#ff8c00"

else:

    glow="#ef4444"


trust = status

# -------------------------
# SAVE SCAN HISTORY
# -------------------------

if "scan_history" not in st.session_state:

    st.session_state["scan_history"]=[]


current_scan={

    "status":trust,

    "score":score,

    "verdict":verdict

}


history=st.session_state["scan_history"]


if len(history)==0 or history[0]!=current_scan:

    history.insert(
        0,
        current_scan
    )


st.session_state["scan_history"]=history[:5]

positive_count=len(
st.session_state.get(
"positives",[]
)
)

negative_count=len(
st.session_state.get(
"negatives",[]
)
)

base_score=score

confidence=base_score

confidence+=(
positive_count*2
)

confidence-=(
negative_count*1
)

confidence=max(
60,
min(confidence,98)
)




#-------------------------

#CSS

#-------------------------

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
  


  
</style>""",unsafe_allow_html=True)

# -------------------------
# SCORE CARD
# -------------------------

if score >=80:

    meter_color="#19f589"
    glow="rgba(25,245,137,.65)"

elif score>=60:

    meter_color="#facc15"
    glow="rgba(250,204,21,.65)"

elif score>=40:

    meter_color="#ff8c00"
    glow="rgba(255,140,0,.65)"

else:

    meter_color="#ff4b5c"
    glow="rgba(255,75,92,.65)"


degree=(score/100)*180


st.markdown(f"""

<style>

.trust-card{{

display:flex;

align-items:center;

justify-content:space-between;

padding:30px;

border-radius:30px;

background:#07111f;

margin-bottom:25px;

border:1px solid rgba(255,255,255,.08);

box-shadow:
0 0 35px {glow};

}}

.meter{{

position:relative;

width:170px;

height:85px;

overflow:hidden;

}}

.meter:before{{

content:"";

position:absolute;

width:170px;
height:170px;

border-radius:50%;

border:14px solid #1b2433;

box-sizing:border-box;

}}

.meter-fill{{

position:absolute;

width:170px;
height:170px;

border-radius:50%;

border:14px solid {meter_color};

box-sizing:border-box;

clip-path:
inset(
0 0 50% 0
);

transform:
rotate({degree}deg);

transform-origin:center;

box-shadow:
0 0 25px {glow};

transition:1s;

}}

.meter-inner{{

position:absolute;

top:14px;
left:14px;

width:142px;
height:142px;

background:#07111f;

border-radius:50%;

}}

.score-side h1{{
    font-size:72px;
    margin:0;
    white-space:nowrap;
    color:{meter_color};
}}

.score-side h2{{
    margin-top:20px;
    margin-bottom:10px;
    color:{meter_color};
}}

.score-side p{{

color:#9aa4b2;

}}

</style>



<div class="trust-card">


<div class="meter">

<div class="meter-fill">
</div>

<div class="meter-inner">
</div>

</div>



<div class="score-side">

<h1>
{score}/100
</h1>

<h2>
{status}
</h2>

<p>
{trust}
</p>

</div>


<div>

<h3>
AI Verdict
</h3>

<p>
{verdict}
</p>

</div>

</div>

""",unsafe_allow_html=True)

#-------------------------

#GET USER INPUT DATA

#-------------------------

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

#-------------------------

#DETECT SIGNALS

#-------------------------

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


#-------------------------

#SIGNALS

#-------------------------

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

#-------------------------

#AI ANALYSIS

#-------------------------

st.markdown("""

<br>""",unsafe_allow_html=True)

st.markdown("""

<div class='card'><h3>🤖 AI Analysis

</h3></div>""",unsafe_allow_html=True)

st.markdown("""

<br>""",unsafe_allow_html=True)

st.progress(

confidence/100

)

if confidence >= 90:

    confidence_text="Very High"

elif confidence >= 75:

    confidence_text="High"

elif confidence >= 60:

    confidence_text="Moderate"

else:

    confidence_text="Low"


st.caption(
f"AI Confidence: {confidence}% ({confidence_text})"
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

st.markdown("### Company Research")

st.success(
f"""
Company:
{st.session_state.get("company","Unknown")}

Status:
{st.session_state.get("company_status","Unknown")}

Domain Reputation:
{st.session_state.get("domain_reputation","Unknown")}
"""
)

#-------------------------

#BUTTONS

#-------------------------

c1,c2=st.columns(2)

with c1:

    if st.button(
    "📄 Generate Report"
    ):

        generate_report(
            "yescape_report.pdf",
            score,
            status,
            verdict,
            positives,
            negatives,
            st.session_state.get("company","Unknown"),
            st.session_state.get("company_status","Unknown"),
            st.session_state.get("domain_reputation","Unknown")
        )


        with open(
        "yescape_report.pdf",
        "rb"
        ) as file:

            st.download_button(

            label=
            "⬇ Download PDF",

            data=file,

            file_name=
            "YEScape_Report.pdf",

            mime=
            "application/pdf"

            )

with c2:

    if st.button(

    "🔄 Scan Again"

    ):



        st.switch_page(

        "app.py"

        )