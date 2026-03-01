import pandas as pd
from database import session, Issue
from collections import Counter

def recommend_books(student_name):
    issues = session.query(Issue).all()
    
    data = [(i.student_name, i.book_id) for i in issues]
    df = pd.DataFrame(data, columns=["student", "book"])

    student_books = df[df["student"] == student_name]["book"].tolist()
    
    similar_students = df[df["book"].isin(student_books)]["student"].unique()
    
    recommended = df[df["student"].isin(similar_students)]["book"]
    
    counter = Counter(recommended)
    
    return counter