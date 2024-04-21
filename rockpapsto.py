print("Welcome to the Rock, Paper and Scissors Game!")
a = int(input("Choose one: Rock(0) , Paper(1) , Scissors(2)\n"))
if a == 0:
  print('''  
  You chose Rock:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''')
elif a == 1:
  print('''
  You chose Paper:
      _______
  ---'   ____)____
            ______)
            _______)
           _______)
  ---.__________)
  ''')
elif a == 2:
  print('''
  You chose Scissor:
      _______
  ---'   ____)____
            ______)
         __________)
        (____)
  ---.__(___)
  ''')
else:
  print("This is an invalid option. You lose!")
import random
random_int = random.randint(0,2)
if(random_int == 0):
  print('''
  Computer chose Rock:
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
  ''') 
elif random_int == 1:
  print('''
  Computer chose Paper: 
      _______
  ---'   ____)____
            ______)
            _______)
           _______)
  ---.__________)
  ''')
else:
  print('''
  Computer chose Scissors: 
      _______
  ---'   ____)____
            ______)
         __________)
        (____)
  ---.__(___)
  ''')

if(a == 0 and random_int == 0):
  print("You draw!")
elif(a == 1 and random_int == 1):
  print("You draw!")
elif(a == 2 and random_int == 2):
  print("You draw!")
elif(a == 0 and random_int == 2):
  print("You won!")
elif(a == 1 and random_int == 0):
  print("You won!")
elif(a == 2 and random_int == 1):
  print("You won!")
else:
  print("You lose. ")

