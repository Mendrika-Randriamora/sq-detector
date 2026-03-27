import sqlite3
from config import DB_NAME

def connexion():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    file TEXT NOT NULL,
                    value INTEGER
                )
        """)
    conn.commit()
    return conn


def upload_data(data: dict):
    conn = connexion()
    
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO data (file, value) VALUES (?, ?)",
        (data["file"], data["value"])
    )
    conn.commit()
    
def get(limit=None):
    conn = connexion()
    
    cursor = conn.cursor()
    
    if limit:
        cursor.execute("SELECT * FROM data LIMIT ?", (limit,))
    else:
        cursor.execute("SELECT * FROM data")
        
    return cursor.fetchall()
    
def get_by_id(id):
    conn = connexion()
    
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM data WHERE id=?", (id,))
    
    return cursor.fetchone()    