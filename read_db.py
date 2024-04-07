import sqlite3

def get_table_names():
    conn = sqlite3.connect('quiz_bowl.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    conn.close()
    return [table[0] for table in tables]

def get_data_from_table(table_name):
    conn = sqlite3.connect('quiz_bowl.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    data = cursor.fetchall()
    conn.close()
    return data
