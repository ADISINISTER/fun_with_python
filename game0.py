from ursina import *

def update():
    if held_keys['a']:
        test_square.x -= 4 * time.dt  # test_square.y -= 1
    if held_keys['d']:
        test_square.x += 4 * time.dt  # test_square.y += 1
    if held_keys['w']:
        test_square.y += 4 * time.dt
    if held_keys['s']:
        test_square.y -= 4 * time.dt


app = Ursina()

test_square = Entity(model='quad', color=color.red, scale=(1,4), position=(5,4))




app.run()