import json, sqlite3

DB_NAME = "banco.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS note (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def load_data(notes):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, content FROM note")
    rows = cursor.fetchall()
    conn.close()
    notes = [{"id": row[0], "title": row[1], "content": row[2]} for row in rows]
    return notes

def load_template(index):
    with open( "static/templates/" + index, "r", encoding="utf-8") as f:
        return f.read()

def delete_note(note_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM note WHERE id = ?', (note_id,))
    conn.commit()
    conn.close()

def save_note(nova_anotacao):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO note (title, content) VALUES (?, ?)",
        (nova_anotacao["titulo"], nova_anotacao["detalhes"])
    )
    conn.commit()
    conn.close()