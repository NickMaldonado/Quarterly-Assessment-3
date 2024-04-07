import sqlite3

class DatabaseManager:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_file)
            self.cursor = self.connection.cursor()
            print("Connected to the database successfully!")
        except sqlite3.Error as e:
            print("Error connecting to the database:", e)

    def create_table(self):
        try:
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS questions (
                                id INTEGER PRIMARY KEY,
                                category TEXT NOT NULL,
                                question TEXT NOT NULL,
                                option_a TEXT NOT NULL,
                                option_b TEXT NOT NULL,
                                option_c TEXT NOT NULL,
                                option_d TEXT NOT NULL,
                                correct_answer TEXT NOT NULL
                                )''')
            print("Table 'questions' created successfully!")
        except sqlite3.Error as e:
            print("Error creating table:", e)

    def insert_question(self, category, question, option_a, option_b, option_c, option_d, correct_answer):
        try:
            self.cursor.execute('''INSERT INTO questions (category, question, option_a, option_b, option_c, option_d, correct_answer) 
                                VALUES (?, ?, ?, ?, ?, ?, ?)''',
                                (category, question, option_a, option_b, option_c, option_d, correct_answer))
            self.connection.commit()
            print("Question inserted successfully!")
        except sqlite3.Error as e:
            print("Error inserting question:", e)

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Connection to the database closed.")
