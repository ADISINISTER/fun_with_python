import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    try:
        index = task_list.curselection()
        task_list.delete(index)
    except tk.TclError:
        pass

# Create a main window
window = tk.Tk()
window.title("To-Do List")

# Create task list
task_list = tk.Listbox(window, width=50)
task_list.pack(pady=10)

# Create scrollbar
scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Connect scrollbar to task list
task_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_list.yview)

# Create entry field
entry = tk.Entry(window, width=50)
entry.pack(pady=10)

# Create buttons
add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(window, text="Delete Task", command=delete_task)
delete_button.pack()

# Start the Tkinter event loop
window.mainloop()
