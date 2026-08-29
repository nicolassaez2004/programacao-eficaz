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
            content TEXT NOT NULL,
            favorite INTEGER NOT NULL DEFAULT 0
        )
    """)

    cursor.execute("PRAGMA table_info(note)")
    columns = [column[1] for column in cursor.fetchall()]
    if "favorite" not in columns:
        cursor.execute("ALTER TABLE note ADD COLUMN favorite INTEGER NOT NULL DEFAULT 0")

    conn.commit()
    conn.close()


def load_data(notes=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, content, favorite FROM note ORDER BY favorite DESC, id ASC")
    rows = cursor.fetchall()
    conn.close()
    notes = [{"id": row[0], "title": row[1], "content": row[2], "favorite": row[3]} for row in rows]
    return notes

def load_template(index):
    with open( "static/templates/" + index, "r", encoding="utf-8") as f:
        return f.read()
    
def delete_note(note_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM note WHERE id = ?", (note_id,))
    conn.commit()
    conn.close()

def save_note(nova_anotacao):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO note (title, content, favorite) VALUES (?, ?, 0)",
        (nova_anotacao["titulo"], nova_anotacao["detalhes"])
    )
    conn.commit()
    conn.close()


def toggle_favorite(note_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT favorite FROM note WHERE id = ?", (note_id,))
    row = cursor.fetchone()
    if row is None:
        conn.close()
        return None

    new_value = 0 if row[0] else 1
    cursor.execute("UPDATE note SET favorite = ? WHERE id = ?", (new_value, note_id))
    conn.commit()
    conn.close()
    return new_value


def get_note(note_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, title, content, favorite FROM note WHERE id = ?",
        (note_id,)
    )

    row = cursor.fetchone()
    conn.close()

    if row is None:
        return None

    return {
        "id": row[0],
        "title": row[1],
        "content": row[2],
        "favorite": row[3]
    }

def edit_note(note_id, title, content):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE note
        SET title = ?, content = ?
        WHERE id = ?
        """,
        (title, content, note_id)
    )

    conn.commit()
    conn.close()