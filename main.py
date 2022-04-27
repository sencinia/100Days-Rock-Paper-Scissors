import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
hands = [rock, paper, scissors]

cpu_choice = random.randint(0, 2)

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper, or 2 for Scissors. \n"))

print(f"Player chose: {hands[player_choice]}")
print(f"Computer chose: {hands[cpu_choice]}")

if player_choice == cpu_choice:
  print("Draw!")
elif player_choice == 0 and cpu_choice == 2:
  print("You win!")
elif player_choice == 1 and cpu_choice == 0:
  print("You win!")
elif player_choice == 2 and cpu_choice == 1:
  print("You win!")
else:
  print("You lose!")
