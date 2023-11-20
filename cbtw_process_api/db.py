import sqlite3
from sqlite3 import Connection, Cursor
from cbtw_process_api.models import (
    Aircraft,
    CargoAircraft,
    PassengerAircraft,
    AirlineCompany
)
from typing import Optional


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
    def cursor(self) -> Cursor | None:
        self.startup()
        return self._cursor

    @cursor.setter
    def cursor(self, cursor):
        self._cursor = cursor

    def startup(self):
        self.conn = sqlite3.connect('resources/aircrafts.db')

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
