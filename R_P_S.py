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
#player_selction
player_selection = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n")
if player_selection == "0":
    print(rock + "You chose Rock.")
elif player_selection == "1":
    print(paper + "You chose Paper.")
elif player_selection == "2":
    print(scissors + "You chose Scissors.")

#computer_selection
import random
computer_selection = random.randint(0,2)
if computer_selection == 0:
    print(rock + "Computer chose Rock.")
elif computer_selection == 1:
    print(paper + "Computer chose Paper.")
elif computer_selection == 2:
    print(scissors + "Computer chose Scissors.")

#player_wins
if player_selection =="0" and computer_selection == 2:
    print("Rock smashes Scissors! You win!")
elif player_selection == "1" and computer_selection == 0:
    print("Paper covers Rock! You win!")
elif player_selection == "2" and computer_selection == 1:
    print("Scissors slices Paper! You win!")

#player_loses
if player_selection == "0" and computer_selection == 1:
    print("Paper covers Rock! You lose!")
elif player_selection == "1" and computer_selection == 2:
    print("Scissors slices Paper! You lose!")
elif player_selection == "2" and computer_selection == 0:
    print("Rock smashes Scissors! You lose!")

#draws
if player_selection =="0" and computer_selection == 0:
    print("Draw. Try again.")
elif player_selection == "1" and computer_selection == 1:
    print("Draw. Try again.")
elif player_selection == "2" and computer_selection == 2:
    print("Draw. Try again.")