import random
import time

while 1 == 1:
  moves = ['rock', 'paper', 'scissors']
  user_input = input("Choose Rock, Paper or Scissors: ")
  m = moves[random.randint(0, 2)]

  def robot_moves():
      print("robot has chosen -", m)

  robot_moves()

  def rockie():
   if user_input == "rock" and m == "paper":
      print("You lost :(")
      time.sleep(3)
   elif user_input == "rock" and m == "scissors":
      print("You won!")
      time.sleep(3)
   elif user_input == "rock" and m == "rock":
      print("Tie!")
      time.sleep(3)

  rockie()


  def paperr():
      if user_input == "paper" and m == "paper":
         print("Tie")
         time.sleep(3)
      elif user_input == "paper" and m == "scissors":
         print("You lost :(")
         time.sleep(3)
      elif user_input == "paper" and m == "rock":
         print("You won!")
         time.sleep(3)

  paperr()

  def scissors():
      if user_input == "scissors" and m == "paper":
          print("You won!")
          time.sleep(3)
      elif user_input == "scissors" and m == "rock":
          print("You lost :(")
          time.sleep(3)
      elif user_input == "scissors" and m == "scissors":
          print("Tie!")
          time.sleep(3)

  scissors()
  again = input("Wanna play again?: ")
  if again == 'yes':
      print("New game!")
  else:
      print("bye")
      break
