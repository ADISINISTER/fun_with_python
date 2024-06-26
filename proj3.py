import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operator = operator_var.get()

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2

        result_label.config(text="Result: {:.2f}".format(result))
    except ValueError:
        result_label.config(text="Invalid input")

# Create a main window
window = tk.Tk()
window.title("Calculator")

# Create entry fields
entry1 = tk.Entry(window)
entry1.pack()

entry2 = tk.Entry(window)
entry2.pack()

# Create operator selection
operator_var = tk.StringVar()
operator_var.set("+")

operator_frame = tk.Frame(window)
operator_frame.pack()

plus_radio = tk.Radiobutton(operator_frame, text="+", variable=operator_var, value="+")
plus_radio.pack(side=tk.LEFT)

minus_radio = tk.Radiobutton(operator_frame, text="-", variable=operator_var, value="-")
minus_radio.pack(side=tk.LEFT)

multiply_radio = tk.Radiobutton(operator_frame, text="*", variable=operator_var, value="*")
multiply_radio.pack(side=tk.LEFT)

divide_radio = tk.Radiobutton(operator_frame, text="/", variable=operator_var, value="/")
divide_radio.pack(side=tk.LEFT)

# Create calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()

# Create result label
result_label = tk.Label(window, text="Result: ")
result_label.pack()

# Start the Tkinter event loop
window.mainloop()
