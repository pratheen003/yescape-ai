import streamlit as st
from utils.report_generator import generate_report
from ai.verdict_generator import get_verdict
from datetime import datetime, timedelta

scan_time = datetime.utcnow() + timedelta(hours=5, minutes=30)

st.set_page_config(
    page_title="YESScore Report",
    page_icon="🛡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# -------------------------
# INPUT DATA
# -------------------------

url = st.session_state.get("url", "")
pdf = st.session_state.get("pdf_name", "")
text = st.session_state.get("text", "")
combined = (text + " " + url).lower()
trust_data = st.session_state.get("trust_data", {})

# -------------------------
# SCORE ENGINE
# -------------------------

trust_data = st.session_state.get("trust_data", {})
score = trust_data.get("overall_trust", 0)

# -------------------------
# STATUS
# -------------------------

result = get_verdict(
    score,
    st.session_state.get("positives", []),
    st.session_state.get("negatives", [])
)

status = result["status"]
trustline = result["trust"]
verdict = result["verdict"]

confidence_data = st.session_state.get(
    "confidence_data",
    {
        "confidence": 0,
        "evidence_count": 0,
        "explanation": "No confidence data available."
    }
)

if score >= 80:
    meter_color = "#19f589"
    glow = "rgba(25,245,137,.65)"
elif score >= 60:
    meter_color = "#facc15"
    glow = "rgba(250,204,21,.65)"
elif score >= 40:
    meter_color = "#ff8c00"
    glow = "rgba(255,140,0,.65)"
else:
    meter_color = "#ff4b5c"
    glow = "rgba(255,75,92,.65)"

# -------------------------
# SAVE SCAN HISTORY
# -------------------------

if "scan_history" not in st.session_state:
    st.session_state["scan_history"] = []

current_scan = {"status": status, "score": score, "verdict": verdict}
history = st.session_state["scan_history"]
if len(history) == 0 or history[0] != current_scan:
    history.insert(0, current_scan)
st.session_state["scan_history"] = history[:5]

positives = st.session_state.get("positives", [])
negatives = st.session_state.get("negatives", [])

if len(positives) == 0:
    positives = ["No major positive indicators found"]
if len(negatives) == 0:
    negatives = ["No risk indicators detected"]

positive_count = len(positives)
negative_count = len(negatives)

# -------------------------
# CSS — static rules only, no Python variables
# -------------------------

st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
a.anchor-link {display: none !important;}

.stApp {
    background: linear-gradient(180deg, #080c14, #050811);
}

/* HEADER */
.yescape-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px 20px;
    background: rgba(255,255,255,.03);
    border: 1px solid rgba(255,255,255,.05);
    border-radius: 18px;
    margin-bottom: 25px;
}

/* SCORE MAIN CARD */
.score-main-card {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0;
    padding: 25px 30px;
    border-radius: 28px;
    background: #07111f;
    border: 1px solid rgba(255,255,255,.06);
    margin-bottom: 16px;
    transition: all .35s ease;
}
.score-main-card:hover {
    transform: translateY(-6px);
    border-color: rgba(255,255,255,.12);
}

/* GAUGE */
.gauge-side {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    border-right: 1px solid rgba(255,255,255,.06);
    padding-right: 30px;
}
.gauge-wrap {
    position: relative;
    width: 220px;
    height: 120px;
    overflow: hidden;
    margin-bottom: 10px;
}
.gauge-label-zero {
    position: absolute;
    left: -5px;
    top: 110px;
    color: #8b95a7;
    font-size: 13px;
}
.gauge-label-hundred {
    position: absolute;
    right: -18px;
    top: 110px;
    color: #8b95a7;
    font-size: 13px;
}
.gauge-ring {
    position: absolute;
    width: 220px;
    height: 220px;
    border-radius: 50%;
    border: 16px solid #1b2433;
    box-sizing: border-box;
}
.gauge-inner {
    position: absolute;
    top: 16px; left: 16px;
    width: 188px; height: 188px;
    background: #07111f;
    border-radius: 50%;
}
/* needle and dot are injected via a separate dynamic <style> block */
.gauge-needle {
    position: absolute;
    width: 90px; height: 4px;
    top: 108px; left: 110px;
    transform-origin: left center;
}
.gauge-dot {
    position: absolute;
    width: 14px; height: 14px;
    border-radius: 50%;
    top: 103px; left: 103px;
}

/* SCORE TEXT */
.score-number {
    font-size: 64px;
    font-weight: 800;
    line-height: 1;
    margin-top: 5px;
}
.score-denom {
    font-size: 32px;
    font-weight: 600;
}
.score-status-label {
    font-size: 26px;
    font-weight: 700;
    letter-spacing: 1px;
    margin-top: 8px;
}
.score-trust-badge {
    display: inline-block;
    padding: 6px 20px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 1px;
    margin-top: 10px;
}

/* STATS SIDE */
.stats-side {
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding-left: 30px;
}
.stat-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 16px 0;
    border-bottom: 1px solid rgba(255,255,255,.05);
    transition: all .25s ease;
    border-radius: 8px;
}
.stat-row:last-child { border-bottom: none; }
.stat-row:hover {
    background: rgba(255,255,255,.03);
    padding-left: 8px;
    padding-right: 8px;
}
.stat-icon-wrap {
    width: 32px; height: 32px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 16px;
}
.stat-icon-wrap.green  { background: rgba(29,231,130,.15); }
.stat-icon-wrap.red    { background: rgba(239,68,68,.15); }
.stat-icon-wrap.blue   { background: rgba(96,165,250,.15); }
.stat-icon-wrap.orange { background: rgba(251,146,60,.15); }
.stat-label-text { color: #cfd6df; font-size: 16px; }
.stat-val            { font-weight: 700; font-size: 18px; }
.stat-val.green  { color: #19f589; }
.stat-val.red    { color: #ef4444; }
.stat-val.blue   { color: #60a5fa; }
.stat-val.orange { color: #fb923c; }

/* AI VERDICT CARD */
.verdict-card {
    padding: 25px 30px;
    border-radius: 24px;
    background: #07111f;
    border: 1px solid rgba(255,255,255,.06);
    box-shadow: 0 0 20px rgba(100,80,255,.15);
    margin-bottom: 20px;
    transition: all .35s ease;
}
.verdict-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 0 40px rgba(139,92,246,.45);
    border-color: rgba(139,92,246,.25);
}
.verdict-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 16px;
}
.verdict-eyebrow {
    font-size: 15px;
    font-weight: 700;
    letter-spacing: 1px;
    color: #8b5cf6;
    text-transform: uppercase;
}
.verdict-text {
    font-size: 17px;
    line-height: 2;
    color: #e8edf5;
}

/* FLAG SUBCARDS */
.subcard {
    padding: 24px;
    border-radius: 20px;
    background: #0f1624;
    border: 1px solid rgba(255,255,255,.05);
    height: 100%;
    min-height: 220px;
    box-sizing: border-box;
    transition: all .3s ease;
}
.subcard.green { border-left: 4px solid #1de782; }
.subcard.red   { border-left: 4px solid #ef4444; }
.subcard.green:hover {
    transform: translateY(-6px);
    box-shadow: 0 0 20px rgba(29,231,130,.25);
}
.subcard.red:hover {
    transform: translateY(-6px);
    box-shadow: 0 0 20px rgba(239,68,68,.25);
}
.flag-title { font-size: 22px; font-weight: 700; color: white; margin-bottom: 18px; }
.flag-item  { color: white; font-size: 16px; margin: 10px 0; }

/* GENERIC CARD */
.card {
    width: 100%;
    padding: 25px;
    border-radius: 24px;
    background: rgba(15,20,30,.95);
    border: 1px solid rgba(255,255,255,.05);
    box-shadow: 0 0 20px rgba(25,245,137,.1);
    margin-bottom: 20px;
    transition: all .35s ease;
}
.card:hover {
    transform: translateY(-6px);
    box-shadow: 0 0 35px rgba(25,245,137,.25);
}
.card h2 { color: white; font-size: 22px; margin-top: 0; margin-bottom: 16px; }
.analysis-text { font-size: 17px; line-height: 2; color: white; }

/* COMPANY RESEARCH */
.research-title { font-size: 22px; font-weight: 700; color: white; margin-bottom: 20px; }
.research-grid  { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
.research-item {
    padding: 18px;
    background: #08111f;
    border-radius: 16px;
    border: 1px solid rgba(255,255,255,.05);
    transition: all .3s ease;
}
.research-item:hover {
    transform: translateY(-5px);
    border-color: rgba(25,245,137,.25);
    box-shadow: 0 0 15px rgba(25,245,137,.15);
}
.research-item .ri-label { font-size: 13px; color: #8b95a7; margin-bottom: 6px; }
.research-item .ri-value { font-size: 18px; font-weight: 700; color: #19f589; }

/* TRUST BREAKDOWN WRAPPER */
.trust-section-card {
    width: 100%;
    padding: 25px;
    border-radius: 24px;
    background: rgba(15,20,30,.95);
    border: 1px solid rgba(255,255,255,.05);
    box-shadow: 0 0 20px rgba(25,245,137,.1);
    margin-bottom: 20px;
    transition: all .35s ease;
}
.trust-section-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 0 40px rgba(25,245,137,.25);
    border-color: rgba(25,245,137,.15);
}
.trust-section-title { font-size: 22px; font-weight: 700; color: white; margin-bottom: 20px; }
.trust-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; }

/* TRUST MINI CARDS */
.trust-mini {
    padding: 18px;
    background: #08111f;
    border-radius: 16px;
    border: 1px solid rgba(255,255,255,.05);
    display: flex;
    flex-direction: column;
    gap: 8px;
    transition: all .3s ease;
}
.trust-mini:hover {
    transform: translateY(-5px);
    box-shadow: 0 0 18px rgba(25,245,137,.18);
    border-color: rgba(25,245,137,.25);
}
.trust-mini .tm-icon  { font-size: 22px; }
.trust-mini .tm-label { color: #9aa4b2; font-size: 13px; font-weight: 600; }
.trust-mini .tm-value { font-size: 28px; font-weight: 800; }
.tm-value.high { color: #19f589; }
.tm-value.mid  { color: #facc15; }
.tm-value.low  { color: #ef4444; }
.progress-bg {
    width: 100%; height: 6px;
    background: #1b2433;
    border-radius: 999px;
    overflow: hidden;
    margin-top: 4px;
}
/* progress fills are injected via dynamic <style> block */
.progress-fill { height: 6px; border-radius: 999px; }

/* RESPONSIVE */
@media (max-width: 768px) {
    .score-main-card  { grid-template-columns: 1fr; gap: 20px; padding: 20px; }
    .gauge-side       { border-right: none; border-bottom: 1px solid rgba(255,255,255,.06); padding-right: 0; padding-bottom: 24px; }
    .stats-side       { padding-left: 0; }
    .research-grid    { grid-template-columns: 1fr; }
    .trust-grid       { grid-template-columns: repeat(2, 1fr); }
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# DYNAMIC CSS — injected separately so no f-string brace conflicts in HTML
# -------------------------

degree = int((score / 100) * 180)
needle_rotate = degree - 180

st.markdown(
    "<style>"
    ".score-main-card { box-shadow: 0 0 30px " + glow + "; }"
    ".score-main-card:hover { box-shadow: 0 0 50px " + glow + "; }"
    ".score-number, .score-status-label { color: " + meter_color + "; }"
    ".score-trust-badge { color: " + meter_color + "; border: 1px solid " + meter_color + "; }"
    ".gauge-needle { background: " + meter_color + "; transform: rotate(" + str(needle_rotate) + "deg); box-shadow: 0 0 12px " + meter_color + "; }"
    ".gauge-dot    { background: " + meter_color + "; box-shadow: 0 0 10px " + meter_color + "; }"
    "</style>",
    unsafe_allow_html=True
)

# -------------------------
# HEADER
# -------------------------

st.markdown(
    "<div class='yescape-header'>"
    "<div>"
    "<h2 style='margin:0; color:white;'>🛡 YESCAPE</h2>"
    "<div style='color:#8b95a7; font-size:13px; letter-spacing:1px;'>AI VERIFICATION REPORT</div>"
    "</div>"
    "<div style='color:#9aa4b2; font-size:14px;'>📅 " + scan_time.strftime("%d %b %Y | %I:%M %p IST") + "</div>"
    "</div>",
    unsafe_allow_html=True
)

# -------------------------
# SCORE CARD — ROW 1: Gauge + Stats
# -------------------------

trustline_text = trustline.upper() if trustline else "HIGH TRUST"

st.markdown(
    "<div class='score-main-card'>"

    "<div class='gauge-side'>"
    "<div class='gauge-wrap'>"
    "<span class='gauge-label-zero'>0</span>"
    "<span class='gauge-label-hundred'>100</span>"
    "<div class='gauge-ring'></div>"
    "<div class='gauge-inner'></div>"
    "<div class='gauge-needle'></div>"
    "<div class='gauge-dot'></div>"
    "</div>"
    "<div class='score-number'>" + str(score) + "<span class='score-denom'> /100</span></div>"
    "<div class='score-status-label'>" + str(status) + "</div>"
    "<div class='score-trust-badge'>" + trustline_text + "</div>"
    "</div>"

    "<div class='stats-side'>"

    "<div class='stat-row'>"
    "<div style='display:flex;align-items:center;gap:12px;'>"
    "<div class='stat-icon-wrap green'>✅</div>"
    "<span class='stat-label-text'>Positive Signals</span>"
    "</div>"
    "<span class='stat-val green'>" + str(positive_count) + "</span>"
    "</div>"

    "<div class='stat-row'>"
    "<div style='display:flex;align-items:center;gap:12px;'>"
    "<div class='stat-icon-wrap red'>❗</div>"
    "<span class='stat-label-text'>Negative Signals</span>"
    "</div>"
    "<span class='stat-val red'>" + str(negative_count) + "</span>"
    "</div>"

    "<div class='stat-row'>"
    "<div style='display:flex;align-items:center;gap:12px;'>"
    "<div class='stat-icon-wrap blue'>📈</div>"
    "<span class='stat-label-text'>AI Confidence</span>"
    "</div>"
    "<span class='stat-val blue'>" + str(confidence_data.get("confidence", 0)) + "%</span>"
    "</div>"

    "<div class='stat-row'>"
    "<div style='display:flex;align-items:center;gap:12px;'>"
    "<div class='stat-icon-wrap orange'>📄</div>"
    "<span class='stat-label-text'>Evidence Count</span>"
    "</div>"
    "<span class='stat-val orange'>" + str(confidence_data.get("evidence_count", 0)) + "</span>"
    "</div>"

    "</div>"
    "</div>",
    unsafe_allow_html=True
)

# -------------------------
# ROW 2: AI Verdict
# -------------------------

st.markdown(
    "<div class='verdict-card'>"
    "<div class='verdict-header'>"
    "<div style='font-size:22px;'>🌐</div>"
    "<div class='verdict-eyebrow'>AI Verdict</div>"
    "</div>"
    "<div class='verdict-text'>" + str(verdict) + "</div>"
    "</div>",
    unsafe_allow_html=True
)

# -------------------------
# GREEN & RED FLAGS
# -------------------------

positive_html = "".join("<div class='flag-item'>✔ " + item + "</div>" for item in positives)
negative_html = "".join("<div class='flag-item'>⚠ " + item + "</div>" for item in negatives)

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        "<div class='subcard green'>"
        "<div class='flag-title'>🟢 GREEN FLAGS</div>"
        + positive_html +
        "</div>",
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        "<div class='subcard red'>"
        "<div class='flag-title'>🔴 RED FLAGS</div>"
        + negative_html +
        "</div>",
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# -------------------------
# AI ANALYSIS
# -------------------------

reasoning = st.session_state.get("reasoning", "No reasoning available.")

st.markdown(
    "<div class='card'>"
    "<h2>🤖 AI Analysis</h2>"
    "<div class='analysis-text'>" + reasoning + "</div>"
    "</div>",
    unsafe_allow_html=True
)

# -------------------------
# COMPANY RESEARCH
# -------------------------

domain_age = st.session_state.get("domain_age", None)
https_status = st.session_state.get("https_status", False)
years = (str(round(domain_age / 365, 1)) + " Years") if domain_age else "Not Available"

company        = st.session_state.get("company", "Unknown")
company_status = st.session_state.get("company_status", "Unknown")
domain_rep     = st.session_state.get("domain_reputation", "Unknown")

st.markdown(
    "<div class='card'>"
    "<div class='research-title'>🏢 Company Research</div>"
    "<div class='research-grid'>"
    "<div class='research-item'><div class='ri-label'>🏢 Company</div><div class='ri-value'>" + company + "</div></div>"
    "<div class='research-item'><div class='ri-label'>📋 Status</div><div class='ri-value'>" + company_status + "</div></div>"
    "<div class='research-item'><div class='ri-label'>🌐 Domain Reputation</div><div class='ri-value'>" + domain_rep + "</div></div>"
    "<div class='research-item'><div class='ri-label'>📅 Domain Age</div><div class='ri-value'>" + years + "</div></div>"
    "</div>"
    "</div>",
    unsafe_allow_html=True
)

# -------------------------
# TRUST BREAKDOWN
# -------------------------

company_trust   = trust_data.get("company_trust", 0) or 0
recruiter_trust = trust_data.get("recruiter_trust", 0) or 0
website_trust   = trust_data.get("website_trust", 0) or 0
language_trust  = trust_data.get("language_trust", 0) or 0
context_trust   = trust_data.get("context_trust", 0) or 0
overall_trust   = trust_data.get("overall_trust", 0) or 0


def get_trust_color(v):
    if v >= 70:
        return "#19f589"
    elif v >= 40:
        return "#facc15"
    return "#ef4444"


def get_trust_cls(v):
    if v >= 70:
        return "high"
    elif v >= 40:
        return "mid"
    return "low"


# Build dynamic progress-fill styles separately — no f-strings, no brace issues
trust_items = [
    ("company_fill",   company_trust),
    ("recruiter_fill", recruiter_trust),
    ("website_fill",   website_trust),
    ("language_fill",  language_trust),
    ("context_fill",   context_trust),
    ("overall_fill",   overall_trust),
]

fill_css = "<style>"
for cls_name, val in trust_items:
    color = get_trust_color(val)
    fill_css += (
        "." + cls_name + " {"
        " width: " + str(val) + "%;"
        " background: " + color + ";"
        " box-shadow: 0 0 8px " + color + ";"
        "}"
    )
fill_css += "</style>"

st.markdown(fill_css, unsafe_allow_html=True)


def trust_mini_html(icon, label, value, fill_cls):
    cls = get_trust_cls(value)
    return (
        "<div class='trust-mini'>"
        "<div class='tm-icon'>" + icon + "</div>"
        "<div class='tm-label'>" + label + "</div>"
        "<div class='tm-value " + cls + "'>" + str(value) + "/100</div>"
        "<div class='progress-bg'>"
        "<div class='progress-fill " + fill_cls + "'></div>"
        "</div>"
        "</div>"
    )


trust_grid_html = (
    trust_mini_html("🏢", "Company Trust",   company_trust,   "company_fill")
    + trust_mini_html("👤", "Recruiter Trust", recruiter_trust, "recruiter_fill")
    + trust_mini_html("🌐", "Website Trust",   website_trust,   "website_fill")
    + trust_mini_html("💬", "Language Trust",  language_trust,  "language_fill")
    + trust_mini_html("🔍", "Context Trust",   context_trust,   "context_fill")
    + trust_mini_html("💯", "YESSCORE",        overall_trust,   "overall_fill")
)

st.markdown(
    "<div class='trust-section-card'>"
    "<div class='trust-section-title'>🛡 Trust Breakdown</div>"
    "<div class='trust-grid'>"
    + trust_grid_html +
    "</div></div>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# -------------------------
# BUTTONS
# -------------------------

c1, c2 = st.columns(2)

with c1:
    if st.button("📄 Generate Report", use_container_width=True):
        generate_report(
            "yescape_report.pdf",
            score, status, verdict, positives, negatives,
            st.session_state.get("confidence_data", {}),
            st.session_state.get("trust_data", {}),
            st.session_state.get("reasoning", ""),
            company, company_status, domain_rep,
            st.session_state.get("domain_age", None),
            st.session_state.get("https_status", False)
        )
        with open("yescape_report.pdf", "rb") as file:
            st.download_button(
                label="⬇ Download PDF",
                data=file,
                file_name="YEScape_Report.pdf",
                mime="application/pdf",
                use_container_width=True
            )

with c2:
    if st.button("🔄 Scan Again", use_container_width=True):
        st.switch_page("app.py")

st.markdown(
    "<div style='text-align:center; color:#4a5568; font-size:13px; margin-top:30px; padding-bottom:20px;'>"
    "🛡 Powered by YESCAPE AI &nbsp;|&nbsp; Trust Before You Act"
    "</div>",
    unsafe_allow_html=True
)