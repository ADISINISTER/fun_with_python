import tkinter as tk
import random

def start_game():
    global score
    score = 0
    update_score()

    # Remove start button and show targets
    start_button.pack_forget()
    for target in targets:
        target.show()

def update_score():
    score_label.config(text="Score: {}".format(score))

def increment_score():
    global score
    score += 1
    update_score()

class Target:
    def __init__(self, canvas):
        self.canvas = canvas
        self.size = 40
        self.x = random.randint(self.size, canvas_width - self.size)
        self.y = random.randint(self.size, canvas_height - self.size)
        self.shape = canvas.create_oval(self.x - self.size, self.y - self.size,
                                        self.x + self.size, self.y + self.size,
                                        fill="red")
        self.canvas.tag_bind(self.shape, "<Button-1>", self.hit)

    def hit(self, event):
        self.hide()
        increment_score()

    def show(self):
        self.canvas.itemconfigure(self.shape, state=tk.NORMAL)

    def hide(self):
        self.canvas.itemconfigure(self.shape, state=tk.HIDDEN)

canvas_width = 400
canvas_height = 400
num_targets = 10
targets = []

# Create a main window
window = tk.Tk()
window.title("Target Game")

# Create canvas
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height)
canvas.pack()

# Create score label
score_label = tk.Label(window, text="Score: 0")
score_label.pack()

# Create targets
for _ in range(num_targets):
    target = Target(canvas)
    targets.append(target)

# Create start button
start_button = tk.Button(window, text="Start Game", command=start_game)
start_button.pack()

# Start the Tkinter event loop
window.mainloop()
