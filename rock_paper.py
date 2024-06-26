import random

Rock = '''
Rock
         _______
      ---'   ____)
            (_____)
            (_____)
    VK      (____)
      ---.__(___)
'''
Paper = '''
Paper
           _______
      ---'   ____)____
                ______)
                _______)
    VK         _______)
      ---.__________)   
'''
Scissors = '''
Scissors
          _______
      ---'   ____)____
                ______)
             __________)
    VK      (____)
      ---.__(___)
'''
game_image = [Rock, Paper, Scissors]
user_choice = int(input("enter your choice, 0 for Rock, 1 for Paper and 2 for Scissors\n"))
print(game_image[user_choice])
computer_choice = random.randint(0, 2)
print(f"Computer chose {computer_choice}")
print(game_image[computer_choice])

