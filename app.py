import streamlit as st
import base64

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="YESCAPE AI",
    page_icon="🛡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- LOAD BACKGROUND IMAGE ----------------

def get_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

bg = get_base64("assets/bg.jpg")

# ---------------- CSS ----------------

st.markdown(f"""
<style>

#MainMenu {{
visibility:hidden;
}}

footer {{
visibility:hidden;
}}

header {{
visibility:hidden;
}}

[data-testid="stSidebar"]{{
display:none;
}}

/* Main background */

.stApp{{

background:
linear-gradient(
rgba(0,0,0,.82),
rgba(0,0,0,.90)
),

url("data:image/jpg;base64,{bg}");

background-size:cover;
background-position:center;
background-attachment:fixed;

overflow:hidden;
}}

/* Bottom neon wave */

.stApp:after{{

content:"";

position:fixed;

bottom:-120px;

left:-10%;

width:120%;

height:320px;

background:
radial-gradient(
circle,
rgba(0,255,140,.45),
transparent 70%
);

filter:blur(75px);

z-index:-1;
}}

/* Hero section */

.hero{{

margin-top:120px;

text-align:center;
}}

/* Logo */

.logo{{

font-size:65px;

font-weight:800;

color:#1dd66f;

}}

/* Heading */

.title{{

margin-top:60px;

font-size:58px;

font-weight:800;

line-height:1.3;

color:white;

max-width:1000px;

margin-left:auto;

margin-right:auto;
}}

/* Description */

.subtitle{{

margin-top:25px;

font-size:22px;

color:#c4c4c4;
}}

/* Button */

.stButton>button{{

background:#18c37e;

color:white;

font-size:22px;

padding:16px 55px;

border-radius:999px;

border:none;

margin-top:50px;

font-weight:700;

box-shadow:
0px 0px 35px rgba(0,255,150,.45);

transition:.3s;
}}

.stButton>button:hover{{

transform:scale(1.04);

background:#22e88f;
}}

.stButton{{
text-align:center;
}}

</style>
""", unsafe_allow_html=True)

# ---------------- UI ----------------

st.markdown("""

<div class='hero'>

<div class='logo'>

🛡 YES-cape

</div>

<div class='title'>

Trust Your Internship Offer.<br>
Scan for Peace of Mind.

</div>

<div class='subtitle'>

AI-powered internship verification and scam detection platform.

</div>

</div>

""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])

with col2:
    if st.button("START VERIFICATION"):
        st.switch_page("pages/1_Verification.py")