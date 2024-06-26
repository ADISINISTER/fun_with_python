from string import *
from itertools import product

value =ascii_letters+digits+punctuation

for i in range(1,4):
    for j in product(value, repeat = 3): # repeat = i or 1 or 2 or 3
        word = "".join(j)
        p = open("password.txt","a")
        p.write(word)
        p.write("\n")

