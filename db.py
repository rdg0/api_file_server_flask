import sqlite3
from typing import Optional


def start_db() -> None:
    """Создание БД."""
    try:
        con = sqlite3.connect('db.sqlite')
        cur = con.cursor()
        cur.execute('''
        CREATE TABLE IF NOT EXISTS file(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            extention TEXT,
            size REAL NOT NULL,
            hash TEXT
        );
        ''')
        con.commit()
    except Exception as error:
        print('Db not ok :(', error)
    finally:
        con.close()


def get_file_by_name(filename: str) -> Optional[sqlite3.Cursor]:
    """Получаем файл по имени."""

    with sqlite3.connect('db.sqlite') as con:
        cur = con.cursor()
        cur.execute('''
        SELECT * FROM file
        WHERE name = ?;
        ''', (filename,)
        )
    return cur


def get_file_by_hash(hsh: str) -> Optional[sqlite3.Cursor]:
    """Получаем файл по хэшу."""

    with sqlite3.connect('db.sqlite') as con:
        cur = con.cursor()
        cur.execute('''
        SELECT * FROM file
        WHERE hash = ?;
        ''', (hsh,)
        )
    return cur


def get_file_list() -> Optional[sqlite3.Cursor]:
    """Получаем из БД список всех файлов."""
    with sqlite3.connect('db.sqlite') as con:
        cur = con.cursor()
        cur.execute('''
        SELECT * FROM file;
        ''')
    return cur


def get_file_list_by_extention(extention: str) -> Optional[sqlite3.Cursor]:
    """Получаем из БД все файлы с определенным расширением."""
    with sqlite3.connect('db.sqlite') as con:
        cur = con.cursor()
        cur.execute('''
        SELECT * FROM file
        WHERE extention = ?;
        ''', (extention,)
        )
    return cur


def create_file(
        filename: str, extention: str, size: float, hash: str
    ) -> Optional[sqlite3.Cursor]:
    """Добавляем в БД новый файл."""
    with sqlite3.connect('db.sqlite') as con:
        cur = con.cursor()
        cur.execute("""
        INSERT INTO file
        VALUES(NULL, ?, ?, ?, ?);
        """, (filename, extention, size, hash)
        )
    return cur


def delete_file(filename) -> Optional[sqlite3.Cursor]:
    """Удаляем из БД запись по определенному файлу."""
    with sqlite3.connect('db.sqlite') as con:
        cur = con.cursor()
        cur.execute("""
        DELETE FROM file
        WHERE name = ?;""", (filename,)
        )
    return cur
