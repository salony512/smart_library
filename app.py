import streamlit as st
from database import session, Book, Issue
from analytics import get_most_issued_books, get_total_fine
from recommendation import recommend_books
from datetime import datetime, timedelta
import pandas as pd
import plotly.express as px
menu = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Add Book", "Issue Book", "Return Book", "Analytics"]
)

if menu == "Dashboard":
    st.subheader("📈 Library Overview")

    books = session.query(Book).all()
    issues = session.query(Issue).all()

    total_books = len(books)
    total_issues = len(issues)
    total_fine = get_total_fine()

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Books", total_books)
    col2.metric("Total Issues", total_issues)
    col3.metric("Total Fine Collected", f"₹{total_fine}")

    st.divider()

    st.subheader("📚 Book Inventory")
    from analytics import get_all_books
    book_df = get_all_books()
    st.dataframe(book_df)

    st.subheader("📊 Category Distribution")
    from analytics import get_category_distribution
    cat_data = get_category_distribution()

    if not cat_data.empty:
        fig = px.pie(values=cat_data.values,
                     names=cat_data.index,
                     title="Books by Category")
        st.plotly_chart(fig)