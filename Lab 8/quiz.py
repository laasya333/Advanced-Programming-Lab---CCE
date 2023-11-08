import tkinter as tk
from tkinter import messagebox

# Define the quiz questions and answers
questions = ["What is the capital of France?",
             "Which planet is known as the Red Planet?",
             "What is the largest mammal in the world?"]

options = [["Paris", "London", "Berlin", "Madrid"],
           ["Earth", "Mars", "Jupiter", "Venus"],
           ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"]]

correct_answers = [0, 1, 1]  # Index of correct options for each question

# Function to check the answers and save the result to a file
def check_answers():
    score = 0
    user_answers = []  # List to store user's answers
    
    for i in range(len(questions)):
        selected_answer = var_list[i].get()
        user_answers.append(selected_answer)
        if selected_answer == correct_answers[i]:
            score += 1

    # Write user's answers to a file
    with open("quiz_answers.txt", "w") as file:
        file.write("User's Answers:\n")
        for i in range(len(questions)):
            file.write(f"Q{i + 1}: {options[i][user_answers[i]]}\n")
        
        file.write(f"Score: {score} out of {len(questions)}")

    messagebox.showinfo("Result", f"You scored {score} out of {len(questions)}. Answers saved to 'quiz_answers.txt'.")

# Create the tkinter window
root = tk.Tk()
root.title("Quiz Application")
root.configure(bg='#E1D9D1')

# Create tkinter variables for radio buttons
var_list = [tk.IntVar() for _ in range(len(questions))]

# Create and display quiz questions and radio buttons with custom colors
for i in range(len(questions)):
    question_label = tk.Label(root, text=f"{i + 1}. {questions[i]}", padx=10, pady=5, bg='#E1D9D1', fg='#4E595D')
    question_label.pack()

    for j in range(len(options[i])):
        radio_button = tk.Radiobutton(root, text=options[i][j], variable=var_list[i], value=j, bg='#E1D9D1', fg='#1E3D59', activebackground='#1E3D59', activeforeground='#E1D9D1')
        radio_button.pack(anchor=tk.W)

# Create and display the Submit button with custom colors
submit_button = tk.Button(root, text="Submit", command=check_answers, bg='#FF6F61', fg='#E1D9D1', padx=10, pady=5)
submit_button.pack(pady=10)

# Start the tkinter main loop
root.mainloop()
