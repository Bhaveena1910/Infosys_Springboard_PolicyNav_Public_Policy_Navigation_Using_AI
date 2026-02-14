
import streamlit as st
import sqlite3
import re
import base64
from sqlite3 import IntegrityError

# ---------------------------
# CONFIG
# ---------------------------
DB_NAME = "users.db"

st.set_page_config(
    page_title="PolicyNav Authentication",
    layout="wide"
)

# ---------------------------
# SESSION STATE
# ---------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------------------------
# BACKGROUND IMAGE
# ---------------------------
def set_bg_from_local(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()

    st.markdown(
        f"""
        <style>
        header {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        #MainMenu {{visibility: hidden;}}

        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        .block-container {{
            background: transparent;
            padding-top: 3rem;
        }}

        h1 {{
            text-align:center;
            color:#FFA94D;
            font-weight:800;
        }}

        div.stButton > button {{
            background-color:#E76F51;
            color:white;
            border-radius:8px;
            border:none;
            padding:0.6em 1.5em;
            font-weight:bold;
        }}

        div.stButton > button:hover {{
            background-color:#D62828;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg_from_local("/content/bg.png")

# ---------------------------
# DATABASE
# ---------------------------
conn = sqlite3.connect(DB_NAME, check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT NOT NULL,
    email TEXT PRIMARY KEY,
    password TEXT NOT NULL,
    security_question TEXT NOT NULL,
    security_answer TEXT NOT NULL
)
""")
conn.commit()

# ---------------------------
# VALIDATION
# ---------------------------
def valid_email(email):
    pattern = r'^[^@]+@[^@]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

def valid_password(password):
    return password.isalnum() and len(password) >= 8

# ==========================================================
# HOME PAGE
# ==========================================================
if st.session_state.page == "home":

    st.markdown("<h1>PolicyNav Authentication</h1>", unsafe_allow_html=True)
    st.markdown("### Choose an option")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Login"):
            st.session_state.page = "login"
            st.rerun()

    with col2:
        if st.button("Sign Up"):
            st.session_state.page = "signup"
            st.rerun()

    with col3:
        if st.button("Forgot Password"):
            st.session_state.page = "forgot"
            st.rerun()

# ==========================================================
# SIGN UP
# ==========================================================
elif st.session_state.page == "signup":

    st.markdown("<h1>Create Account</h1>", unsafe_allow_html=True)

    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    security_question = st.selectbox(
        "Security Question",
        [
            "What is your pet name?",
            "What is your mother’s maiden name?",
            "What is your favorite teacher?"
        ]
    )

    security_answer = st.text_input("Security Answer")

    if st.button("Create Account"):

        if not all([username, email, password, confirm_password, security_answer]):
            st.warning("All fields are mandatory!")

        elif not valid_email(email):
            st.error("Invalid email format!")

        elif not valid_password(password):
            st.error("Password must be minimum 8 alphanumeric characters!")

        elif password != confirm_password:
            st.error("Passwords do not match!")

        else:
            try:
                cursor.execute(
                    "INSERT INTO users VALUES (?, ?, ?, ?, ?)",
                    (username, email, password, security_question, security_answer)
                )
                conn.commit()
                st.success("Signup Successful!")
            except IntegrityError:
                st.error("Email already registered!")

    if st.button("Back"):
        st.session_state.page = "home"
        st.rerun()

# ==========================================================
# LOGIN
# ==========================================================
elif st.session_state.page == "login":

    st.markdown("<h1>Login</h1>", unsafe_allow_html=True)

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        cursor.execute("SELECT username FROM users WHERE email=? AND password=?", (email, password))
        user = cursor.fetchone()

        if user:
            st.session_state.username = user[0]
            st.session_state.page = "dashboard"
            st.rerun()
        else:
            st.error("Invalid Email or Password")

    if st.button("Back"):
        st.session_state.page = "home"
        st.rerun()

# ==========================================================
# DASHBOARD
# ==========================================================
elif st.session_state.page == "dashboard":

    st.markdown("<h1>Dashboard</h1>", unsafe_allow_html=True)

    st.success(f"Welcome, {st.session_state.username} 👋")

    if st.button("Logout"):
        del st.session_state.username
        st.session_state.page = "home"
        st.rerun()

# ==========================================================
# FORGOT PASSWORD
# ==========================================================
elif st.session_state.page == "forgot":

    st.markdown("<h1>Recover Password</h1>", unsafe_allow_html=True)

    email = st.text_input("Enter Registered Email")

    if st.button("Verify Email"):

        cursor.execute("SELECT security_question FROM users WHERE email=?", (email,))
        result = cursor.fetchone()

        if result:
            st.session_state.reset_email = email
            st.session_state.question = result[0]
        else:
            st.error("Email not found!")

    if "question" in st.session_state:
        st.info(st.session_state.question)

        answer = st.text_input("Enter Answer")

        if st.button("Submit Answer"):

            cursor.execute("SELECT security_answer FROM users WHERE email=?",
                           (st.session_state.reset_email,))
            correct_answer = cursor.fetchone()

            if correct_answer and answer == correct_answer[0]:
                st.success("Your password is: " + correct_answer[0])
            else:
                st.error("Incorrect Answer!")

    if st.button("Back"):
        st.session_state.page = "home"
        st.rerun()
