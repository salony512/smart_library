from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///library.db")

def create_tables():
    with engine.connect() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                author TEXT,
                quantity INTEGER
            )
        """))

        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS issued_books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_name TEXT,
                book_title TEXT,
                issue_date TEXT
            )
        """))
        conn.commit()