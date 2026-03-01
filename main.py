import streamlit as st
import pandas as pd
from sqlalchemy import text
from database import engine, create_tables

create_tables()

st.set_page_config(page_title="Library Management System", layout="wide")

# ---------------- LOGIN SYSTEM ----------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.title("🔐 Admin Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "admin123":
            st.session_state.logged_in = True
            st.success("Login Successful ✅")
            st.rerun()
        else:
            st.error("Invalid Credentials ❌")


# 🔴 STOP APP IF NOT LOGGED IN
if not st.session_state.logged_in:
    login()
    st.stop()


# ================= MAIN APP STARTS HERE =================

st.title("📚 Integrated College Library Management System")

menu = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Add Book", "Issue Book", "Return Book"]
)

if menu == "Dashboard":
    st.header("Dashboard")
    df_books = pd.read_sql("SELECT * FROM books", engine)
    df_issued = pd.read_sql("SELECT * FROM issued_books", engine)

    col1, col2 = st.columns(2)
    col1.metric("Total Books", len(df_books))
    col2.metric("Issued Books", len(df_issued))

    st.dataframe(df_books)