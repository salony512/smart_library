import pandas as pd
from database import session, Book, Issue
from sqlalchemy import func
from datetime import datetime

def get_all_books():
    books = session.query(Book).all()
    data = [{
        "ID": b.id,
        "Title": b.title,
        "Category": b.category,
        "Available": b.available_copies,
        "Total": b.total_copies
    } for b in books]

    return pd.DataFrame(data)

def get_most_issued_books():
    results = session.query(
        Issue.book_id,
        func.count(Issue.book_id).label("count")
    ).group_by(Issue.book_id).all()

    return pd.DataFrame(results, columns=["Book ID", "Issue Count"])

def get_category_distribution():
    books = session.query(Book).all()
    data = [b.category for b in books]
    return pd.Series(data).value_counts()

def get_total_fine():
    total = session.query(func.sum(Issue.fine)).scalar()
    return total if total else 0