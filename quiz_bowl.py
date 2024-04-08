# ['Business Strategy', 'Entrepreneurship', 'Business Ethics', 'Business Analytics', 'Econometrics']
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import random

class Question:
    def __init__(self, question_text, options, correct_answer):
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer

class QuizGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Bowl")

        # Create main window widgets
        self.category_label = tk.Label(root, text="Select Category:")
        self.category_label.pack()

        self.category_var = tk.StringVar()
        self.category_options = ['Business Strategy', 'Entrepreneurship', 'Business Ethics', 'Business Analytics', 'Econometrics']
        self.category_dropdown = tk.OptionMenu(root, self.category_var, *self.category_options)
        self.category_dropdown.pack()

        self.start_button = tk.Button(root, text="Start Quiz Now", command=self.start_quiz)
        self.start_button.pack()

    def start_quiz(self):
        selected_category = self.category_var.get()
        if selected_category:
            self.root.destroy()  # Close the main window
            self.display_quiz(selected_category)
        else:
            messagebox.showerror("Error", "Please select a category before starting the quiz.")

    def display_quiz(self, category):
        # Connect to the SQLite database and fetch questions based on the selected category
        conn = sqlite3.connect('quiz_bowl.db')
        cursor = conn.cursor()
        cursor.execute("SELECT question, option_a, option_b, option_c, option_d, answer FROM QuizQuestions WHERE category=?", (category,))
        question_records = cursor.fetchall()
        conn.close()

        # Create a list of Question objects
        self.questions = []
        for question_data in question_records:
            question_text, option_a, option_b, option_c, option_d, correct_answer = question_data
            options = [option_a, option_b, option_c, option_d]
            question = Question(question_text, options, correct_answer)
            self.questions.append(question)

        # Shuffle questions to randomize quiz order
        random.shuffle(self.questions)

        # Create quiz window
        self.quiz_window = tk.Toplevel()
        self.quiz_window.title("Quiz - " + category)

        # Create canvas and scrollbar
        self.canvas = tk.Canvas(self.quiz_window)
        self.scrollbar = tk.Scrollbar(self.quiz_window, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Create frame inside canvas to hold questions and options
        self.questions_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0,0), window=self.questions_frame, anchor="nw")

        # Display questions and options
        self.selected_answers = []
        for i, question in enumerate(self.questions, start=1):
            question_frame = tk.Frame(self.questions_frame)
            question_frame.pack(pady=10)

            question_label = tk.Label(question_frame, text=f"{i}. {question.question_text}")
            question_label.pack()

            option_var = tk.StringVar()
            option_var.set("")  # Set default value
            for j, option in enumerate(question.options, start=65):  # ASCII code for 'A'
                option_button = tk.Radiobutton(question_frame, text=option, variable=option_var, value=chr(j))
                option_button.pack(anchor='w')

            self.selected_answers.append(option_var)

        # Update the canvas scroll region
        self.questions_frame.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        submit_button = tk.Button(self.quiz_window, text="Submit", command=self.submit_quiz)
        submit_button.pack()

    def submit_quiz(self):
        # Check answers and provide feedback
        correct_answers = 0
        total_questions = len(self.selected_answers)
        for i, option_var in enumerate(self.selected_answers):
            selected_option = option_var.get()
            if selected_option == "":
                messagebox.showwarning("Warning", f"You haven't answered question {i+1}.")
                return
            elif selected_option == chr(ord('A') + ord('Z')):  # Check if an option is selected
                messagebox.showwarning("Warning", f"You haven't answered question {i+1}.")
                return
            elif selected_option == self.questions[i].correct_answer:
                correct_answers += 1

        score = correct_answers / total_questions * 100
        messagebox.showinfo("Quiz Result", f"You got {correct_answers} out of {total_questions} correct. Your score: {score:.2f}%")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGUI(root)
    root.mainloop()
