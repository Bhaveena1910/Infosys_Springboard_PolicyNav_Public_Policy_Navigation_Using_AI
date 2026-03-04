import streamlit as st
import sqlite3
import bcrypt
import datetime
import time
import pandas as pd
import plotly.graph_objects as go
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import textstat
import PyPDF2
import smtplib
import secrets
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ---------------------------
# CONFIG & SECRETS
# ---------------------------
DB_NAME = "policy_secure_final.db"
ADMIN_EMAIL = "admin@infosys.com"
ADMIN_PASS = ""
EMAIL_SENDER = "bhaveenaps@gmail.com"
EMAIL_APP_PASSWORD = ""

# ---------------------------
# UTILITY FUNCTIONS
# ---------------------------
def init_db():
    conn = sqlite3.connect(DB_NAME, check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT, email TEXT PRIMARY KEY, password BLOB,
            role TEXT, status TEXT, attempts INTEGER,
            security_qn TEXT, security_ans TEXT, created_at TEXT
        )""")
    # Seed Admin
    cursor.execute("SELECT * FROM users WHERE email=?", (ADMIN_EMAIL,))
    if not cursor.fetchone():
        hashed_admin = bcrypt.hashpw(ADMIN_PASS.encode(), bcrypt.gensalt())
        cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       ("System Admin", ADMIN_EMAIL, hashed_admin, "admin", "active", 0, "None", "None", str(datetime.datetime.now())))
    conn.commit()
    return conn

def validate_email(email):
    return re.match(r'^[^@]+@[^@]+\.[a-zA-Z]{2,}$', email)

def validate_password_strength(password):
    if len(password) < 8: return False
    if not re.search(r"[a-z]", password): return False
    if not re.search(r"[A-Z]", password): return False
    if not re.search(r"\d", password): return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): return False
    return True

def send_otp_email(to_email, otp):
    msg = MIMEMultipart()
    msg['Subject'] = "🔐 OTP for Password Reset"
    msg.attach(MIMEText(f"Your secure OTP code is: {otp}", 'plain'))
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587); server.starttls()
        server.login(EMAIL_SENDER, EMAIL_APP_PASSWORD)
        server.sendmail(EMAIL_SENDER, to_email, msg.as_string()); server.quit()
        return True
    except: return False

# ---------------------------
# APP SETUP
# ---------------------------
st.set_page_config(page_title="PolicyNav | Enterprise", layout="wide")
conn = init_db()
cursor = conn.cursor()

# Global Custom CSS for Professional Dark Mode
st.markdown("""
<style>
    .stApp { background: radial-gradient(circle at top right, #1e293b, #0f172a); color: white; }
    h1, h2, h3 { font-family: 'Inter', sans-serif; font-weight: 800 !important; color: #00ffcc !important; }
    
    /* Login & UI Cards */
    [data-testid="stVerticalBlock"] > div:has(div.stButton) {
        background: rgba(255, 255, 255, 0.03);
        padding: 30px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* Modern Buttons */
    div.stButton > button {
        width: 100%;
        border-radius: 10px;
        background: linear-gradient(135deg, #00ffcc 0%, #00b386 100%);
        color: #0f172a !important;
        font-weight: bold;
        border: none;
        padding: 12px;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(0, 255, 204, 0.3); }

    /* Metric Cards Styling */
    [data-testid="stMetricValue"] { color: #00ffcc !important; }
</style>
""", unsafe_allow_html=True)

if "logged_in" not in st.session_state:
    st.session_state.update({"logged_in": False, "user": None, "role": None, "otp": None, "reset_email": None, "view": "select_role"})

# ---------------------------
# AUTHENTICATION LOGIC
# ---------------------------

# 1. SELECT ROLE PAGE
if not st.session_state.logged_in and st.session_state.view == "select_role":
    st.title("🛡️ PolicyNav Enterprise")
    st.subheader("Select your portal to continue")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🏢 ADMIN PORTAL"):
            st.session_state.active_mode = "admin"
            st.session_state.view = "login"
            st.rerun()
    with col2:
        if st.button("👥 USER PORTAL"):
            st.session_state.active_mode = "user"
            st.session_state.view = "login"
            st.rerun()

# 2. LOGIN PAGE (Fixed: removed 'kind' parameter)
elif not st.session_state.logged_in and st.session_state.view == "login":
    st.title(f"🔐 {st.session_state.active_mode.upper()} LOGIN")
    email = st.text_input("Corporate Email")
    pw = st.text_input("Password", type="password")
    
    if st.button("Sign In"):
        cursor.execute("SELECT password, role, status, attempts FROM users WHERE email=?", (email,))
        data = cursor.fetchone()
        if data:
            h_pw, role, status, att = data
            if role != st.session_state.active_mode: st.error("❌ Role mismatch.")
            elif status == "locked": st.error("🚫 ACCOUNT LOCKED. Contact Admin.")
            elif bcrypt.checkpw(pw.encode(), h_pw):
                cursor.execute("UPDATE users SET attempts = 0 WHERE email=?", (email,))
                conn.commit()
                st.session_state.update({"logged_in": True, "user": email, "role": role})
                st.rerun()
            else:
                new_att = att + 1
                cursor.execute("UPDATE users SET status=?, attempts=? WHERE email=?", ('locked' if new_att >= 3 else 'active', new_att, email))
                conn.commit()
                st.error(f"Invalid Password. Attempt {new_att}/3")
        else: st.error("User not found.")

    cols = st.columns(3)
    if st.session_state.active_mode == "user":
        if cols[0].button("Forgot Password?"): 
            st.session_state.view = "forgot"
            st.rerun()
        if cols[1].button("Register Account"): 
            st.session_state.view = "register"
            st.rerun()
    if cols[2].button("← Back"):
      st.session_state.view = "select_role"
      st.rerun()
    

# 3. REGISTRATION PAGE
elif not st.session_state.logged_in and st.session_state.view == "register":
    st.title("📝 New User Registration")
    u = st.text_input("Full Name")
    e = st.text_input("Corporate Email")
    p = st.text_input("Password", type="password")
    cp = st.text_input("Confirm Password", type="password")
    q = st.selectbox("Security Question", ["First School?", "Pet's Name?", "Mother's Maiden Name?"])
    ans = st.text_input("Security Answer")

    if st.button("Create Account"):
        if not all([u, e, p, cp, ans]): st.error("All fields mandatory.")
        elif not validate_email(e): st.error("Invalid Format.")
        elif not validate_password_strength(p): st.error("Weak Password.")
        elif p != cp: st.error("Passwords do not match.")
        else:
            try:
                hashed = bcrypt.hashpw(p.encode(), bcrypt.gensalt())
                cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (u, e, hashed, "user", "active", 0, q, ans, str(datetime.datetime.now())))
                conn.commit()
                st.success("Registration Success! Proceed to Login.")
                time.sleep(1.5)
                st.session_state.view = "login"
                st.rerun()
            except: st.error("Email already provisioned.")
    if st.button("Back to Login"): 
        st.session_state.view = "login"
        st.rerun()

# 4. FORGOT PASSWORD PAGE
elif not st.session_state.logged_in and st.session_state.view == "forgot":
    st.title("🔑 Recovery Portal")
    fe = st.text_input("Enter Registered Email")
    if st.button("Request OTP"):
        cursor.execute("SELECT 1 FROM users WHERE email=?", (fe,))
        if cursor.fetchone():
            otp = "".join([str(secrets.randbelow(10)) for _ in range(6)])
            if send_otp_email(fe, otp):
                st.session_state.otp = otp; st.session_state.reset_email = fe
                st.success("Verification Code Sent to Email!")
        else: st.error("Email not found in our records.")

    if st.session_state.otp:
        uo = st.text_input("Enter 6-Digit OTP")
        np = st.text_input("New Secure Password", type="password")
        ncp = st.text_input("Confirm New Password", type="password")
        if st.button("Reset & Update Password"):
            if uo != st.session_state.otp: st.error("Invalid OTP.")
            elif np != ncp: st.error("Passwords do not match.")
            elif not validate_password_strength(np): st.error("Password complexity not met.")
            else:
                nh = bcrypt.hashpw(np.encode(), bcrypt.gensalt())
                cursor.execute("UPDATE users SET password=?, status='active', attempts=0 WHERE email=?", (nh, st.session_state.reset_email))
                conn.commit(); st.success("Credential Updated! Redirecting..."); st.session_state.otp = None; time.sleep(1.5)
                st.session_state.view = "login"; st.rerun()
    if st.button("Cancel"): 
        st.session_state.view = "login"
        st.rerun()

# ---------------------------
# DASHBOARDS (AFTER LOGIN)
# ---------------------------
else:
    # Navigation Header
    header_col1, header_col2 = st.columns([8, 2])
    with header_col2:
        if st.button("🚪 LOGOUT"):
            st.session_state.update({"logged_in": False, "user": None, "role": None, "view": "select_role"})
            st.rerun()

    if st.session_state.role == "admin":
        st.title("👨‍✈️ Admin Control Center")
        st.subheader("User Activity & Security Management")
        
        # Enhanced Data View: Logic to "View Activity" via Created_At and Attempts
        df = pd.read_sql("""
            SELECT username as 'Name', 
                   email as 'Email', 
                   status as 'Status', 
                   attempts as 'Failed Attempts', 
                   created_at as 'Registration Date' 
            FROM users WHERE role='user'
        """, conn)
        
        st.dataframe(df, use_container_width=True)
        
        # Lock/Unlock Management
        locked_df = df[df['Status'] == 'locked']
        if not locked_df.empty:
            st.warning(f"Detected {len(locked_df)} locked accounts.")
            target = st.selectbox("Select identity to unlock:", locked_df['Email'].tolist())
            if st.button("RESTORE ACCOUNT ACCESS"):
                cursor.execute("UPDATE users SET status='active', attempts=0 WHERE email=?", (target,))
                conn.commit()
                st.success(f"Access restored for {target}")
                st.rerun()
        else:
            st.info("System Security: All user accounts currently active.")

    else:
        st.title("📊 Policy Analysis Intelligence")
        st.write(f"Authorized Session: **{st.session_state.user}**")
        
        up = st.file_uploader("Upload Policy Document (PDF or TXT)", type=['pdf', 'txt'])
        if up:
            with st.spinner("Processing semantics..."):
                text = "".join([p.extract_text() for p in PyPDF2.PdfReader(up).pages]) if up.type=="application/pdf" else up.read().decode()
                
                # Compliance Gauges
                st.markdown("### Readability & Complexity Benchmarks")
                g1, g2, g3 = st.columns(3)
                metrics = [
                    ("LIX Score", textstat.lix(text), 100), 
                    ("Fog Index", textstat.gunning_fog(text), 20), 
                    ("Dale-Chall", textstat.dale_chall_readability_score(text), 15)
                ]
                
                for col, (n, v, m) in zip([g1,g2,g3], metrics):
                    fig = go.Figure(go.Indicator(
                        mode="gauge+number", 
                        value=v, 
                        title={'text': n, 'font': {'color': '#00ffcc'}}, 
                        gauge={'axis':{'range':[0,m], 'tickcolor': "white"}, 'bar':{'color':"#00ffcc"}}
                    ))
                    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", font={'color': "white"}, height=280)
                    col.plotly_chart(fig, use_container_width=True)

                # Theme Cloud
                st.markdown("### Terminology Distribution")
                wc = WordCloud(width=1000, height=400, background_color='#0f172a', colormap='cool').generate(text)
                fig, ax = plt.subplots(figsize=(12, 5))
                ax.imshow(wc, interpolation='bilinear')
                ax.axis("off")
                fig.patch.set_facecolor('#0f172a')
                st.pyplot(fig)

                # Summary Statistics
                st.subheader("Quantitative Overview")
                s1, s2, s3, s4 = st.columns(4)
                s1.metric("Word Count", len(text.split()))
                s2.metric("Sentences", textstat.sentence_count(text))
                s3.metric("Syllables", textstat.syllable_count(text))
                s4.metric("Avg. Read Time", f"{len(text.split())//200} min")
