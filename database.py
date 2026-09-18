import sqlite3

conn = sqlite3.connect("resume.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS resumes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    phone TEXT,
    skills TEXT,
    ats_score INTEGER,
    match_score INTEGER,
    resume_summary TEXT,
    candidate_level TEXT,
    suggestions TEXT,
    file_path TEXT
)
""")

conn.commit()


def register(username, password):
    try:
        cursor.execute(
            "INSERT INTO users(username,password) VALUES(?,?)",
            (username, password),
        )
        conn.commit()
        return True
    except:
        return False


def login(username, password):
    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password),
    )
    return cursor.fetchone()


def save_resume(
    name,
    email,
    phone,
    skills,
    ats,
    match,
    suggestions,
    path,
):
    cursor.execute(
        """
        INSERT INTO resumes
        (name,email,phone,skills,ats_score,match_score,suggestions,file_path)
        VALUES(?,?,?,?,?,?,?,?)
        """,
        (
            name,
            email,
            phone,
            skills,
            ats,
            match,
            suggestions,
            path,
        ),
    )

    conn.commit()


def get_all():
    cursor.execute("SELECT * FROM resumes")
    return cursor.fetchall()