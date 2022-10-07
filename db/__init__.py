import sqlite3

from config import DB_PATH


# Create db if not existed
with sqlite3.connect(DB_PATH) as conn:
    c = conn.execute('SELECT name FROM sqlite_master WHERE type=\'table\' AND name=\'student\'')
    if not c.fetchone():
        conn.execute('CREATE TABLE student ('
                     '_id INTEGER PRIMARY KEY NOT NULL, '
                     'sid TEXT NOT NULL, '
                     'last_name TEXT NOT NULL, '
                     'first_name TEXT NOT NULL, '
                     'email TEXT NOT NULL, '
                     'dob TEXT NOT NULL, '
                     'hometown TEXT NOT NULL, '
                     'gpa REAL)')
        conn.execute('CREATE UNIQUE INDEX sid_index ON student (sid)')
        conn.commit()
