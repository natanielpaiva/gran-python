import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS twitter (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                post TEXT NOT NULL,
                category TEXT
            )
        """)
        self.conn.commit()

    def insert_post(self, post, category):
        self.cursor.execute("INSERT INTO twitter (post, category) VALUES (?, ?)", (post, category))
        self.conn.commit()

    def read_posts(self):
        self.cursor.execute("SELECT * FROM twitter")
        return self.cursor.fetchall()

    def __del__(self):
        self.conn.close()
