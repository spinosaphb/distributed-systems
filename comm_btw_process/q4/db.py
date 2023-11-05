import sqlite3
from sqlite3 import Connection, Cursor
from candidate import Candidate
from typing import Iterable, Optional


class Service:

    def __init__(self) -> None:
        self._conn: Optional[Connection] = None
        self._cursor: Optional[Cursor] = None

    @property
    def conn(self) -> Connection:
        if self._conn is None:
            raise Exception("Connection not initialized")
        return self._conn

    @conn.setter
    def conn(self, conn):
        self._conn = conn

    @property
    def cursor(self) -> Cursor:
        self.startup()
        return self._cursor

    @cursor.setter
    def cursor(self, cursor):
        self._cursor = cursor

    def startup(self):
        self.conn = sqlite3.connect('resources/voting.db')

        self._cursor = self.conn.cursor()

        self._cursor.execute('''
            CREATE TABLE IF NOT EXISTS candidates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                nvotes INTEGER
            )
        ''')

    def shutdown(self):
        self.conn.close()

    def create_candidate(self, name):
        self.cursor.execute(
            "INSERT INTO candidates (name, nvotes) VALUES (?, ?)", (name, 0)
        )
        self.conn.commit()

    def remove_candidate(self, id):
        self.cursor.execute("DELETE FROM candidates WHERE id = ?", (id,))
        self.conn.commit()

    def update_candidate(self, id, name):
        self.cursor.execute(
            "UPDATE candidates SET name = ? WHERE id = ?", (name, id)
        )
        self.conn.commit()

    def get_candidates(self) -> Iterable[Candidate]:
        cursor = self.cursor
        cursor.execute("SELECT * FROM candidates")
        candidates_data = cursor.fetchall()
        candidates = map(lambda c: Candidate(*c), candidates_data)
        return candidates
