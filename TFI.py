import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(
    page_title="TuTechy Pre-Seed Raise",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Function to check password
def check_password():
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False
    if st.session_state["password_correct"]:
        return True

    # Centered login container
    st.markdown(
        """
        <div class='login-container'>
            <h1 class='login-heading'>TuTechy Fundraise</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Password input and button inside the same container
    st.markdown("<div class='login-container' style='margin-top:0;'>", unsafe_allow_html=True)
    password = st.text_input(
        label="Password", 
        type="password", 
        placeholder="Password", 
        key="password_input_login",
        label_visibility="collapsed"
    )
    if st.button("Login", use_container_width=True):
        if password == "tutechy2025":
            st.session_state["password_correct"] = True
            st.rerun()
            return True
        else:
            st.error("Incorrect password. Please try again.")
            return False
    st.markdown("</div>", unsafe_allow_html=True)
    return False

# Custom CSS for styling - DARK MODE
custom_css = '''
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap');
    html, body, .stApp, .stMarkdown, h1, h2, h3, h4, h5, h6, p, span, div, button, input {
        font-family: 'Montserrat', sans-serif !important;
    }
    /* Force dark mode for entire site */
    .stApp {
        background-color: #0e1117;
        color: white;
    }
    
    /* Larger title fonts */
    h1 { font-size: 3rem !important; font-weight: 700 !important; color: white !important; }
    h2 { font-size: 2.5rem !important; font-weight: 600 !important; color: white !important; }
    h3 { font-size: 2rem !important; font-weight: 600 !important; color: white !important; }
    h4 { font-size: 1.5rem !important; font-weight: 600 !important; color: white !important; }
    p { color: #e0e0e0 !important; }
    
    /* Button with shadow and rounded corners */
    .stButton > button { 
        background-color: #4286F4 !important; 
        color: white !important; 
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3) !important;
        font-size: 1.2rem !important;
        transition: all 0.3s !important;
        border-radius: 8px !important;
        padding: 10px 25px !important;
        line-height: 1.5 !important;
        min-width: 120px !important;
        border: none !important;
    }
    
    .stButton > button:hover { 
        background-color: #2764CF !important; 
        box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.4) !important;
        transform: translateY(-2px) !important;
    }
    
    /* Hide Streamlit elements */
    #MainMenu, footer { visibility: hidden; }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab"] { font-size: 1.2rem !important; }
    .stTabs [data-baseweb="tab-list"] { background-color: #1a1a1a !important; }
    .stTabs [data-baseweb="tab"] { color: #e0e0e0 !important; }
    .stTabs [data-baseweb="tab"][aria-selected="true"] { 
        background-color: #4286F4 !important;
        color: white !important;
    }
    
    /* Dark table styling */
    .dark-table {
        border-radius: 10px;
        overflow: hidden;
        margin: 10px 0;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3);
    }
    
    .dark-table table {
        width: 100%;
        border-collapse: collapse;
        background-color: #1a1a1a;
        color: white;
    }
    
    .dark-table th {
        background-color: #2a2a2a;
        padding: 12px;
        text-align: left;
        font-weight: bold;
    }
    
    .dark-table td {
        padding: 12px;
        border-top: 1px solid #333;
    }
    
    .dark-table tr:nth-child(even) {
        background-color: #222;
    }
    
    /* Card styling */
    .card {
        background-color: #1a1a1a;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3);
    }
    
    /* Additional styling for columns and cards */
    .stColumn > div {
        height: 100%;
    }
    
    /* Bullet point styling */
    .bullet-point {
        display: flex;
        align-items: flex-start;
        margin-bottom: 12px;
    }
    .bullet {
        color: white;
        font-size: 1.6rem;
        line-height: 1.2;
        margin-right: 12px;
        font-weight: bold;
    }
    .bullet-text {
        color: white;
        font-size: 1.22rem;
        line-height: 1.6;
        font-weight: 500;
        font-family: 'Montserrat', sans-serif !important;
    }
    @media (max-width: 600px) {
        .bullet {
            font-size: 1.2rem;
            margin-right: 8px;
        }
        .bullet-text {
            font-size: 1.05rem;
        }
    }
    
    /* Login container styling */
    .login-container {
        max-width: 360px;
        margin: 0 auto 0 auto;
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
    }
    .login-heading {
        color: white;
        text-align: center;
        margin-top: 40px;
        font-size: 2.6rem;
        font-weight: bold;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    @media (max-width: 600px) {
        .login-container {
            max-width: 90vw;
            padding-left: 2vw;
            padding-right: 2vw;
        }
        .login-heading {
            font-size: 1.1rem;
        }
    }
    
    /* Improve spacing and appearance of Streamlit tabs */
    [data-baseweb="tab-list"] > button[data-baseweb="tab"] {
        margin-right: 24px !important;
        padding-left: 24px !important;
        padding-right: 24px !important;
        min-height: 48px !important;
        border-radius: 12px 12px 0 0 !important;
        font-size: 1.21rem !important;
        font-family: 'Montserrat', sans-serif !important;
        transition: background 0.2s;
    }
    [data-baseweb="tab-list"] > button[data-baseweb="tab"]:last-child {
        margin-right: 0 !important;
    }
    /* Optional: make the selected tab's background more prominent */
    [data-baseweb="tab-list"] > button[aria-selected="true"] {
        box-shadow: 0 2px 12px rgba(66,134,244,0.12);
        z-index: 2;
    }
    /* Make all headings Montserrat */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 700;
    }
</style>
'''
st.markdown(custom_css, unsafe_allow_html=True)

# Main logic - authenticate
if not check_password():
    st.stop()

# Top bar for authenticated users
st.markdown("""
<div style="background-color: #1E1E1E; padding: 10px 15px; display: flex; align-items: center;
     box-shadow: 0 2px 5px rgba(0,0,0,0.2); position: fixed; top: 0; left: 0; right: 0; z-index: 1000;">
    <div style="font-weight: bold; font-size: 1.2rem; color: #4286F4;">TuTechy</div>
    <div style="margin-left: 20px; color: white;">Pre-Seed Dashboard</div>
    <div style="flex-grow: 1;"></div>
    <div style="color: #aaa; font-size: 0.9rem;">January 2025</div>
</div>
<div style="height: 60px;"></div>
""", unsafe_allow_html=True)

# Executive Summary with new bullet
executive_summary_content = '''
<div>
    <div class="bullet-point"><span class="bullet">•</span><span class="bullet-text">We're raising a $320K pre-seed round to build our foundation with 16 schools and 2 colleges, targeting $600K ARR within 9 months.</span></div>
    <div class="bullet-point"><span class="bullet">•</span><span class="bullet-text">This funding allows us to secure a world-class full-time technical team at a major discount, driving faster product development and scalability.</span></div>
    <div class="bullet-point"><span class="bullet">•</span><span class="bullet-text">We'll immediately activate a strong sales pipeline through top educational conferences and showcase events to drive real adoption and growth.</span></div>
    <div class="bullet-point"><span class="bullet">•</span><span class="bullet-text">We're focused on expanding across North Carolina, South Carolina, Tennessee, and Georgia, using our warm network and advisors to accelerate school partnerships.</span></div>
    <div class="bullet-point"><span class="bullet">•</span><span class="bullet-text">These four states represent over 8,000 K-12 schools and 200+ colleges — a direct pathway to building a <strong>$100M+ revenue opportunity</strong> as we expand our footprint.</span></div>
    <div class="bullet-point"><span class="bullet">•</span><span class="bullet-text">We've already worked with amazing overseas contractors we trust, allowing us to scale technical development at heavily discounted rates without compromising quality.</span></div>
    <div class="bullet-point"><span class="bullet">•</span><span class="bullet-text">This pre-seed round is about setting the foundation to control key markets, scale nationally, and establish TuTechy as the go-to AI tutoring platform for schools.</span></div>
    <div class="bullet-point"><span class="bullet">•</span><span class="bullet-text">We've already bootstrapped the initial production of TuTechy, launching a fully-functional platform with internal resources and proving product-market fit before seeking external funding.</span></div>
</div>
'''

# Data
data = pd.DataFrame([
    {"month": "May",       "salaries": 22917, "contractors": 3500,  "sales": 2000,  "platform": 2000,  "technology": 1000, "schools_onboard": 1,  "colleges_onboarded": 0, "mrr": 2083.33,  "arr": 25000,  "mnr": -29333.67},
    {"month": "June",      "salaries": 22917, "contractors": 7000,  "sales": 5000,  "platform": 1000,  "technology": 1000, "schools_onboard": 3,  "colleges_onboarded": 0, "mrr": 6250,     "arr": 75000,  "mnr": -30667},
    {"month": "July",      "salaries": 22917, "contractors": 4000,  "sales": 5000,  "platform": 2000,  "technology": 1000, "schools_onboard": 5,  "colleges_onboarded": 0, "mrr": 10416.67, "arr": 125000, "mnr": -24500.33},
    {"month": "August",    "salaries": 22917, "contractors": 3000,  "sales": 3000,  "platform": 4000,  "technology": 1500, "schools_onboard": 6,  "colleges_onboarded": 0, "mrr": 12500,    "arr": 150000, "mnr": -21917},
    {"month": "September", "salaries": 22917, "contractors": 3000,  "sales": 3000,  "platform": 4000,  "technology": 2000, "schools_onboard": 8,  "colleges_onboarded": 0, "mrr": 16666.67, "arr": 200000, "mnr": -18250.33},
    {"month": "October",   "salaries": 22917, "contractors": 2500,  "sales": 4000,  "platform": 2500,  "technology": 1500, "schools_onboard": 10, "colleges_onboarded": 1, "mrr": 29166.67, "arr": 350000, "mnr": -4250.33},
    {"month": "November",  "salaries": 22917, "contractors": 4000,  "sales": 4500,  "platform": 1500,  "technology": 1500, "schools_onboard": 13, "colleges_onboarded": 1, "mrr": 35416.67, "arr": 425000, "mnr": 999.67},
    {"month": "December",  "salaries": 22917, "contractors": 7500,  "sales": 5000,  "platform": 2500,  "technology": 1500, "schools_onboard": 15, "colleges_onboarded": 2, "mrr": 47916.67, "arr": 575000, "mnr": 8499.67},
    {"month": "January",   "salaries": 22917, "contractors": 5000,  "sales": 5000,  "platform": 2500,  "technology": 1500, "schools_onboard": 16, "colleges_onboarded": 2, "mrr": 50000,    "arr": 600000, "mnr": 13083}
])
data["expenses"] = data[["salaries","contractors","sales","platform","technology"]].sum(axis=1)
data["month_idx"] = range(len(data))

# Page heading and tabs
st.markdown("<h1>TuTechy Pre-Seed Raise Dashboard</h1>", unsafe_allow_html=True)
tabs = st.tabs(["📊 Summary", "💰 Fundraise Breakdown", "📅 Nine-Month Overview", "📈 All Graphs", "🛡️ SAFE"])

# Summary Tab
with tabs[0]:
    st.markdown("<h2>Executive Summary</h2>", unsafe_allow_html=True)
    st.markdown(executive_summary_content, unsafe_allow_html=True)

# Fundraise Breakdown Tab
with tabs[1]:
    st.markdown("<h2>Fundraise Breakdown</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("<h3>Pre-Seed Allocation</h3>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 1.3rem;'><strong>Total Raised:</strong> $320,000</p>", unsafe_allow_html=True)
        # Salaries section
        st.markdown("<div style='background-color: #222; padding: 15px; border-radius: 10px; margin: 10px 0;'>", unsafe_allow_html=True)
        st.markdown("<h4 style='font-size: 1.4rem; color: #4286F4;'>Salaries</h4>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 1.2rem;'><strong>Amount:</strong> $206,250</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 1.2rem;'><strong>Percentage:</strong> 64.5%</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 1.2rem;'>We’re a tech-heavy team of builders — we've already built the platform and are now focused on scaling it. Our team comes from leading research labs and fast-growing companies, bringing real-world experience to everything we build. Every full-time member is working at $55,000/year, a major discount compared to their market value. This allocation covers engineering, leadership, and operations, giving us an extremely efficient structure to keep building fast while controlling burn.</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        # Contractors section
        st.markdown("<div style='background-color: #222; padding: 15px; border-radius: 10px; margin: 10px 0;'>", unsafe_allow_html=True)
        st.markdown("<h4 style='font-size: 1.4rem; color: #00BFA5;'>Contractors</h4>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 1.2rem;'><strong>Amount:</strong> $30,000</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 1.2rem;'><strong>Percentage:</strong> 9.4%</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 1.2rem;'>Over the past year, we've built and tested a vetted network of overseas developers and designers. These are people we've worked with directly — we know their quality, their speed, and their ability to execute on tight timelines. At this price point, the output is unmatched. This allocation allows us to scale quickly and cost-effectively without compromising quality.</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        # Sales section
        st.markdown("<div style='background-color: #222; padding: 15px; border-radius: 10px; margin: 10px 0;'>", unsafe_allow_html=True)
        st.markdown("<h4 style='font-size: 1.4rem; color: #FF6D00;'>Sales</h4>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 1.2rem;'><strong>Amount:</strong> $40,000</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 1.2rem;'><strong>Percentage:</strong> 12.5%</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 1.2rem;'>This allocation is dedicated to boots-on-the-ground outreach, including travel to educational conferences, building real relationships, and deploying targeted campaigns. It also supports materials, outreach tech, and pilots. It’s our engine for growth — driving us toward 16 schools, 2 colleges, and $600K ARR in under 9 months.</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        # Platform section
        st.markdown("<div style='background-color: #222; padding: 15px; border-radius: 10px; margin: 10px 0;'>", unsafe_allow_html=True)
        st.markdown("<h4 style='font-size: 1.4rem; color: #651FFF;'>Platform</h4>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 1.2rem;'><strong>Amount:</strong> $20,000</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 1.2rem;'><strong>Percentage:</strong> 6.3%</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 1.2rem;'>The platform is already built and live. This portion of the raise goes toward continuous upgrades, improving the backend infrastructure, and making UX tweaks as we onboard more schools. We’ve laid the foundation — now it’s about polish, optimization, and scale.</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        # Technology section
        st.markdown("<div style='background-color: #222; padding: 15px; border-radius: 10px; margin: 10px 0;'>", unsafe_allow_html=True)
        st.markdown("<h4 style='font-size: 1.4rem; color: #F50057;'>Technology</h4>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 1.2rem;'><strong>Amount:</strong> $23,750</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 1.2rem;'><strong>Percentage:</strong> 7.4%</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 1.2rem;'>We’ve been extremely cost-conscious with how we build — using affordable tools, efficient infrastructure, and keeping overhead low. But we’re reaching the point where a modest increase in spend on better software and hardware will significantly boost our team’s productivity. With this allocation, we expect to 2x our output without adding headcount.</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<h3>Fundraise Allocation</h3>", unsafe_allow_html=True)
        fundraise_breakdown = {
            "Category": ["Salaries", "Contractors", "Sales", "Platform", "Technology"],
            "Amount": [206250, 30000, 40000, 20000, 23750]
        }
        fundraise_df = pd.DataFrame(fundraise_breakdown)
        fig = px.pie(
            fundraise_df,
            values='Amount',
            names='Category',
            color='Category',
            color_discrete_map={
                'Salaries': '#4286F4',
                'Contractors': '#00BFA5',
                'Sales': '#FF6D00',
                'Platform': '#651FFF',
                'Technology': '#F50057'
            },
            hole=0.4,
        )
        fig.update_layout(
            height=500,
            margin=dict(t=0, b=0, l=0, r=0),
            legend=dict(font=dict(size=16, color="white")),
            font=dict(size=16, color="white"),
            paper_bgcolor="#1a1a1a",
            plot_bgcolor="#1a1a1a"
        )
        fig.update_traces(
            textinfo='percent+label',
            textfont_size=14,
            textfont_color="white"
        )
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("<h4 style='font-size: 1.4rem;'>Capital Efficiency</h4>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 1.2rem;'>The allocation strategy prioritizes talent (73.9% combined for salaries and contractors) while ensuring adequate resources for sales, platform, and technology requirements.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 1.2rem;'>This balanced approach has led to faster-than-projected growth and early profitability.</p>", unsafe_allow_html=True)

## Nine-Month Overview Tab
# ──────────────────  N I N E  –  M O N T H   O V E R V I E W  ──────────────────
with tabs[2]:
    st.markdown("<h2>Nine-Month Overview</h2>", unsafe_allow_html=True)
    # ... (existing code for the 9-month overview)

    # don’t touch the original `data` used by graphs
    df_raw = data.copy()

    # helper → returns a DataFrame exactly like the spreadsheet (cats ↓, months →)
    def make_quarter(months):
        cats = ["Salaries","Contractors","Sales","Platform","Technology",
                "Schools Onboard","Colleges Onboarded","MRR","ARR","MNR"]
        rows = []
        for cat in cats:
            row = [cat]
            for m in months:
                rec = df_raw.loc[df_raw.month==m].squeeze()
                row.append({
                    "Salaries":            rec.salaries,
                    "Contractors":         rec.contractors,
                    "Sales":               rec.sales,
                    "Platform":            rec.platform,
                    "Technology":          rec.technology,
                    "Schools Onboard":     rec.schools_onboard,
                    "Colleges Onboarded":  rec.colleges_onboarded,
                    "MRR":                 rec.mrr,
                    "ARR":                 rec.arr,
                    "MNR":                 rec.mnr,
                }[cat])
            rows.append(row)
        return pd.DataFrame(rows, columns=["Category"]+months)

    q1 = make_quarter(["May","June","July"])
    q2 = make_quarter(["August","September","October"])
    q3 = make_quarter(["November","December","January"])

    # ---------- table formatter ------------------------------------------------
    def html_table(df):
        hdr = "".join(f"<th>{h}</th>" for h in df.columns)
        body = ""
        for _, r in df.iterrows():
            # decide colour for MNR cells
            colour = ""
            if r["Category"]=="MNR":
                colour = "#E53935" if r.iloc[-1] < 0 else "#43A047"
            tds = []
            for c, v in zip(df.columns, r):
                if c=="Category":
                    txt = v
                elif r["Category"] in ["Schools Onboard","Colleges Onboarded"]:
                    txt = f"{int(v):,}"
                else:
                    txt = f"${v:,.0f}"
                tds.append(f"<td style='color:{colour if c!='Category' else ''}'>{txt}</td>")
            body += "<tr>"+"".join(tds)+"</tr>"
        return f"<div class='dark-table'><table><thead><tr>{hdr}</tr></thead><tbody>{body}</tbody></table></div>"

    # ---------- renderer -------------------------------------------------------
    def quarter(title, frame, goals):
        left, right = st.columns([3,2], gap="large")

        with left:
            st.markdown(f"<h4 style='margin-bottom:8px'>{title}</h4>", unsafe_allow_html=True)
            st.markdown(html_table(frame), unsafe_allow_html=True)

        with right:
            st.markdown(f"""
                <div style="background:#1d1d1d;border-radius:10px;padding:22px 28px;
                            box-shadow:0 4px 12px rgba(0,0,0,.35);margin-top:58px;">
                    <h5 style="margin:0 0 14px;color:#F0F0F0;">
                        {title}
                    </h5>
                    <ul style="line-height:1.55;margin:0;">
                        {''.join(f"<li style='margin-bottom:6px;'>{g}</li>" for g in goals)}
                    </ul>
                </div>
            """, unsafe_allow_html=True)

    # ---------- show all three quarters ---------------------------------------
    quarter("May – July", q1, [
        "Convert LOIs into first paying customers by closing pilots and pushing early adoption.",
        "Hit flagship education conferences hard to maximize exposure and teacher relationships.",
        "Define and pressure-test a scalable sales strategy, including initial sales hires.",
        "Refine and optimize the product based on early customer feedback to strengthen product-market fit."
    ])

    quarter("August – October", q2, [
        "Expand college footprint by onboarding initial college customers and refining outreach.",
        "Maintain an active, consistent sales cycle — adding schools and colleges monthly.",
        "Implement version two features of TuTechy",
        "Streamline network operations and support systems to scale efficiently."
    ])

    quarter("November – January", q3, [
        "Major onboarding push to bring 16+ schools and 2+ colleges fully live on TuTechy.",
        "Achieve and maintain positive net revenue month-over-month.",
        "Prepare platform for full 2nd semester deployment, setting up for massive spring growth.",
        "Lay strategic foundation for 2026 white-label expansion into business and enterprise markets."
    ])

    # Expense Line Descriptions Box (only on this page)
    st.markdown("""
    <div style="background:#1d1d1d;border-radius:10px;padding:22px 28px;box-shadow:0 4px 12px rgba(0,0,0,.35);margin-top:36px;max-width:500px;">
        <h4 style="margin-bottom:16px;color:#F0F0F0;">Expense Line Descriptions</h4>
        <ul style="line-height:1.7;margin:0 0 0 0;padding-left:18px;">
            <li><b>Salaries</b><br>Payments for full-time employees across engineering, sales, operations, and support functions.</li>
            <li><b>Contractors</b><br>Fees paid to part-time specialists or freelance teams for project-based work (e.g., marketing, development, design).</li>
            <li><b>Sales</b><br>Direct expenses to drive revenue growth, including travel, conferences, CRM software, sales enablement tools, and commissions.</li>
            <li><b>Platform</b><br>Costs to host, maintain, and continuously upgrade the TuTechy product for users (e.g., servers, APIs, core platform services).</li>
            <li><b>Technology</b><br>Investments in internal infrastructure upgrades, security improvements, and building tools that power company operations and scale.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
# ───────────────────────────────────────────────────────────────────────────────
# All Graphs Tab
with tabs[3]:
    st.markdown("<h2>Key Performance Graphs</h2>", unsafe_allow_html=True)

    # ── ARR Growth ───────────────────────────────────────────────────────────
    st.markdown("<h3>ARR Growth</h3>", unsafe_allow_html=True)
    arr_fig = make_subplots(specs=[[{"secondary_y": True}]])
    arr_fig.add_trace(
        go.Scatter(x=data.month, y=data.arr,
                   name="ARR", line=dict(color="#4286F4", width=3)),
        secondary_y=False)
    arr_fig.update_layout(
        height=420,
        title="Growth over first nine months",
        title_font=dict(size=20, color="white"),
        legend_font=dict(size=15, color="white"),
        margin=dict(t=70, b=50, l=50, r=50),
        paper_bgcolor="#1a1a1a",
        plot_bgcolor="#1a1a1a",
        font=dict(color="white")
    )
    arr_fig.update_xaxes(tickfont=dict(size=13), gridcolor="#333")
    arr_fig.update_yaxes(title_text="ARR ($)", secondary_y=False,
                         tickprefix="$", tickfont=dict(size=13), gridcolor="#333")
    st.plotly_chart(arr_fig, use_container_width=True)

    # ── Expense Breakdown ────────────────────────────────────────────────────
    st.markdown("<h3>Expense Breakdown</h3>", unsafe_allow_html=True)
    exp_fig = go.Figure()
    for col, col_color in zip(
            ["salaries", "contractors", "sales", "platform", "technology"],
            ["#4286F4", "#00BFA5", "#FF6D00", "#651FFF", "#F50057"]):
        exp_fig.add_trace(go.Bar(
            x=data.month, y=data[col], name=col.title(), marker_color=col_color))

    exp_fig.update_layout(
        barmode='stack',
        title="Monthly Expenses Breakdown",
        height=420,
        title_font=dict(size=20, color="white"),
        legend_font=dict(size=15, color="white"),
        margin=dict(t=70, b=50, l=50, r=50),
        paper_bgcolor="#1a1a1a",
        plot_bgcolor="#1a1a1a",
        font=dict(color="white")
    )
    exp_fig.update_xaxes(tickfont=dict(size=13), gridcolor="#333")
    exp_fig.update_yaxes(title_text="Amount ($)", tickprefix="$",
                         tickfont=dict(size=13), gridcolor="#333")
    st.plotly_chart(exp_fig, use_container_width=True)

# Safe Tab
with tabs[4]:
    st.markdown("<h2>SAFE</h2>", unsafe_allow_html=True)
    st.markdown("""
    <ul style='font-size:1.15rem;line-height:1.7;'>
        <li>We are raising using a SAFE (Simple Agreement for Future Equity).</li>
        <li>A SAFE is an investor-friendly agreement that allows you to invest in the company now without having to determine a valuation today.</li>
        <li>The SAFE has a $6 million valuation cap.</li>
        <li>When we raise our first priced round (traditional equity financing), your SAFE investment will convert into shares based on the $6 million cap, regardless of the new valuation at that time.</li>
        <li>This structure simplifies the fundraising process, avoids complicated negotiations early on, and allows early investors to benefit from future growth.</li>
    </ul>
    <p style='font-size:1.15rem;line-height:1.7;'><b>In short:</b><br>
    You invest now, and when we raise a larger round later, you will own a percentage of the company based on a favorable valuation.
    </p>
    """, unsafe_allow_html=True)
