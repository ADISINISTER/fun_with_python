import tkinter as tk

def increment_counter():
    global counter
    counter += 1
    counter_label.config(text="Counter: {}".format(counter))

counter = 0

# Create a main window
window = tk.Tk()

# Create a label
counter_label = tk.Label(window, text="Counter: {}".format(counter))
counter_label.pack()

# Create a button
button = tk.Button(window, text="Click me!", command=increment_counter)
button.pack()

# Start the Tkinter event loop
window.mainloop()
