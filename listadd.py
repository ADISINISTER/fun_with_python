import random

string_split = input("enter name of all your friends separating by comma : ")
names = string_split.split(", ")
num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_who_will_Pay = names[random_choice]
print(person_who_will_Pay + " is going to pay for the bills of meals today")