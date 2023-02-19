'''Simple calculator with GUI'''

import tkinter as tk

# Function to perform the selected operation
def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    choice = operation.get()
    if choice == 'add':
        result = num1 + num2
        label_result.config(text="Result: " + str(result))
    elif choice == 'subtract':
        result = num1 - num2
        label_result.config(text="Result: " + str(result))
    elif choice == 'multiply':
        result = num1 * num2
        label_result.config(text="Result: " + str(result))
    elif choice == 'divide':
        if num2 == 0:
            label_result.config(text="Error: Division by Zero")
        else:
            result = num1 / num2
            label_result.config(text="Result: " + str(result))

# Create an Application Window
root = tk.Tk()
root.title("Calculator")

# Create widgets to enter data and select operation
label1 = tk.Label(root, text="The first number:")
label1.grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)
label2 = tk.Label(root, text="The second number:")
label2.grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)
operation = tk.StringVar()
operation.set('add')
label3 = tk.Label(root, text="Select operation:")
label3.grid(row=2, column=0)
add_radio = tk.Radiobutton(root, text="Addition", variable=operation, value='add')
add_radio.grid(row=3, column=0)
subtract_radio = tk.Radiobutton(root, text="Subtraction", variable=operation, value='subtract')
subtract_radio.grid(row=3, column=1)
multiply_radio = tk.Radiobutton(root, text="Multiplication", variable=operation, value='multiply')
multiply_radio.grid(row=4, column=0)
divide_radio = tk.Radiobutton(root, text="Division", variable=operation, value='divide')
divide_radio.grid(row=4, column=1)

# Create a button to perform the operation
button = tk.Button(root, text="Perform", command=calculate)
button.grid(row=5, column=0)

# Create a label to display the result
label_result = tk.Label(root, text="Result:")
label_result.grid(row=5, column=1)

# Start the main event processing cycle
root.mainloop()
