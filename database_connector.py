"""Модуль доступу до даних (DAL): усі CRUD-операції з таблицею books."""
import sqlite3

DB_NAME = "data.db"


def create_connection():
    """Повертає з'єднання з файлом бази даних data.db."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # доступ до стовпців за назвою: row["title"]
    return conn


def create_db_table():
    """Створює таблицю books, якщо її ще немає."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id     INTEGER PRIMARY KEY AUTOINCREMENT,
            title  TEXT    NOT NULL,
            author TEXT    NOT NULL,
            genre  TEXT,
            year   INTEGER,
            pages  INTEGER,
            status TEXT    NOT NULL DEFAULT 'не прочитана'
        )
    """)
    conn.commit()
    conn.close()


def insert_item(data):
    """C: додає нову книгу. data - словник з ключами title, author, genre, year, pages, status."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO books (title, author, genre, year, pages, status) VALUES (?, ?, ?, ?, ?, ?)",
        (data["title"], data["author"], data["genre"], data["year"], data["pages"], data["status"]),
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id


def get_all_items():
    """R (All): повертає всі книги, впорядковані за id."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books ORDER BY id")
    items = cursor.fetchall()
    conn.close()
    return items


def get_item_by_id(item_id):
    """R (One): повертає одну книгу за id або None."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE id = ?", (item_id,))
    item = cursor.fetchone()
    conn.close()
    return item


def update_item(item_id, new_data):
    """U: оновлює всі поля книги з вказаним id."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE books SET title = ?, author = ?, genre = ?, year = ?, pages = ?, status = ? WHERE id = ?",
        (new_data["title"], new_data["author"], new_data["genre"], new_data["year"],
         new_data["pages"], new_data["status"], item_id),
    )
    conn.commit()
    conn.close()


def delete_item(item_id):
    """D: видаляє книгу за id."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()
