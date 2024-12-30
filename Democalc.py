import tkinter as tk

# Function to update the expression
def press(key):
    expression = entry.get()
    entry.delete(0, tk.END)  # Clear the current expression
    entry.insert(tk.END, expression + key)  # Add the new key

# Function to calculate the result
def calculate():
    try:
        expression = entry.get()
        result = str(eval(expression))  # Evaluate the expression
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)  # Show the result
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the expression
def clear():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget for displaying the expression and result
entry = tk.Entry(root, width=40, borderwidth=5, font=('Arial', 14), justify='right')
entry.grid(row=0, column=0, columnspan=4)

# List of buttons for the calculator layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Add the buttons to the window
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=10, height=3, font=('Arial', 14), command=calculate)
    e
