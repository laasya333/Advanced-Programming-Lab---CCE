import tkinter as tk


def button_click(number):
    current = entry.get()
    if number == 'C':
        entry.delete(0, tk.END)  # Clear the input field if the button is 'C'
    else:
        entry.delete(0, tk.END)
        entry.insert(0, current + str(number))


def calculate():
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))

#main window
root = tk.Tk()
root.title("Calculator")
root.configure(bg="grey")

# Entry widget
entry = tk.Entry(root, width=20, borderwidth=5, font=("Arial", 16), bg="pink", fg="white")
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

#placing buttons
row_val = 1
col_val = 0
for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 16),
              command=lambda b=button: button_click(b) if b != '='
              else calculate(),
              bg="magenta", fg="white").grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
