from read_db import get_table_names, get_data_from_table
from color import color

def quiz_bowl_app():
    print("Welcome to Quiz Bowl!")
    print("Choose a category:")

    table_names = get_table_names()
    for i, name in enumerate(table_names, 1):
        print(f"{i}. {name}")

    choice = int(input("Enter the number of the category: "))
    print()
    selected_table = table_names[choice - 1]
    data = get_data_from_table(selected_table)

    for index, row in enumerate(data, 1):
        print(f"{index}. {row[1]}")  # Prints question in second column
        user_input = input("Your answer: ")
        if user_input == row[2].lower():
            print(color.GREEN + "Correct!" + color.END)
        else:
            print(color.RED + "Incorrect. The answer is: " + row[2] + color.END)

if __name__ == "__main__":
    quiz_bowl_app()
