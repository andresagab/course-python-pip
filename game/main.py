# import modules
import random


def chooseOptions():

  # define available options
  options = ("rock", "paper", "scissors")
  
  # read user option
  userOption = input("Rock, Paper or Scissors: ").lower()
  
  # define default value of message
  message = f"The {userOption} is invalid! Try again."

  # check user option
  if not userOption in options:
    print(message)
    return None, None

  computerOption = random.choice(options)

  return userOption, computerOption



def checkRules(userOption, computerOption, userWins, computerWins):
  # compare user selection with IA to determinate a draw
  if (userOption == computerOption):
    message = "draw!"
  # when user choice rock
  elif (userOption == "rock"):

    if (computerOption == "scissors"):
      message = "Rock beats Scissor\nUser win!"
      userWins += 1
    else:
      message = "Paper beats Rock\nComputer win!"
      computerWins += 1
  # when user choice paper
  elif (userOption == "paper"):

    if (computerOption == "rock"):
      message = "Paper beats Rock\nUser win!"
      userWins += 1
    else:
      message = "Scissors beats Paper\nComputer win!"
      computerWins += 1
  # when user choice scissors
  elif (userOption == "scissors"):

    if (computerOption == "paper"):
      message = "Scissors beats Paper\nUser win!"
      userWins += 1
    else:
      message = "Rock beats Scissors\nComputer win!"
      computerWins += 1
  else:
    message = "Unknow result"

  return message, userWins, computerWins


def runGame():

  rounds = 1
  computerWins = 0
  userWins = 0

  while True:
  
    if userWins == 2:
      print("¡The final winner is the USER!")
      break
    elif computerWins == 2:
      print("¡The final winner is the Computer!")
      break
  
    print("*" * 10)
    print(f"ROUNDS {rounds}")
    print("*" * 10)
  
    print(f"Computer wins: {computerWins}")
    print(f"User wins: {userWins}")
  
    # increase rounds in 1
    rounds += 1
    # choose options
    userOption, computerOption = chooseOptions()
    # check rules of game
    message, userWins, computerWins = checkRules(userOption, computerOption, userWins, computerWins)
  
    print(message)

runGame()