import tkinter as tk
from tkinter import messagebox
from read_db import get_table_names, get_data_from_table

class QuizBowlGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz Bowl")
        self.geometry("400x300")

        self.main_page()

    def main_page(self):
        self.clear_screen()

        self.label = tk.Label(self, text="Choose a category:")
        self.label.pack(pady=10)

        self.table_names = get_table_names()
        self.category_var = tk.StringVar(self)
        self.category_var.set(self.table_names[0])  # Set default category

        self.category_menu = tk.OptionMenu(self, self.category_var, *self.table_names)
        self.category_menu.pack(pady=10)

        self.start_button = tk.Button(self, text="Start Quiz Now", command=self.start_quiz)
        self.start_button.pack()

    def start_quiz(self):
        category = self.category_var.get()
        data = get_data_from_table(category)

        self.clear_screen()
        self.display_questions(data)

    def display_questions(self, data):
        self.question_frame = tk.Frame(self)
        self.question_frame.pack(pady=10)

        self.questions = []
        for index, row in enumerate(data, 1):
            question_label = tk.Label(self.question_frame, text=f"{index}. {row[1]}")
            question_label.grid(row=index, column=0, sticky="w", padx=5)

            user_answer = tk.StringVar()
            user_entry = tk.Entry(self.question_frame, textvariable=user_answer)
            user_entry.grid(row=index, column=1, padx=5)

            self.questions.append((row[2].lower(), user_answer))

        submit_button = tk.Button(self, text="Submit", command=self.check_answers)
        submit_button.pack(pady=10)

    def check_answers(self):
        correct_answers = 0
        for index, (correct_answer, user_answer) in enumerate(self.questions, 1):
            if user_answer.get().lower() == correct_answer:
                correct_answers += 1

        messagebox.showinfo("Quiz Result", f"You got {correct_answers} out of {len(self.questions)} questions correct!")

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = QuizBowlGUI()
    app.mainloop()
