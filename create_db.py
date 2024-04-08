import sqlite3

def create_database():
    # Connect to the SQLite database
    conn = sqlite3.connect('quiz_bowl.db')
    cursor = conn.cursor()

    # Create a single table for all categories
    cursor.execute('''CREATE TABLE IF NOT EXISTS QuizQuestions (
                        id INTEGER PRIMARY KEY,
                        category TEXT,
                        question TEXT,
                        option_a TEXT,
                        option_b TEXT,
                        option_c TEXT,
                        option_d TEXT,
                        answer TEXT
                     )''')

    # Commit changes and close connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
