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
import random

rps_game = [rock, paper, scissors]

player_selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors \n"))

player_hand_pick = (rps_game[player_selection])
print(player_hand_pick)

if player_selection == 0:
  print("You selected Rock")
elif player_selection == 1:
  print("You Selected Paper")
else:
  print("You selected Scissors")

rps_output = random.randint(0, 2)

if rps_output == 0:
  print(rock)
  print("Computer Selects Rock")
elif rps_output == 1:
  print(paper)
  print("Computer selects Paper")
else:
  print(scissors)
  print("Computer Selects Scissors\n")


if player_selection == rps_output:
  print("\nIt is a draw, both you and the computer think the same.")
elif player_selection < rps_output:
  print("\nYou beat the computer")
else:
  print("\nComputer beats you")
