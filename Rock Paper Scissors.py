# Rock, Paper, Scissors Game
from random import randint

# moves for the player
moves = ["rock", "paper", "scissors"]

# while loop and true boolean
while True:
    computer = moves[randint(0, 2)]
    player_move = input("rock, paper or scissors? (or end game, enter end the game)").lower()
    if player_move == "end the game":
        print("The game has ended")
        break
    elif player_move == computer:
        print("tie")
    elif player_move == "rock":
        if computer == "paper":
            print ("You lose! ", computer, " beats ", player_move)
        else:
            print("You win! ", player_move, " beats ", computer)

    elif player_move == "paper":
        if computer == "scissors":
            print ("You lose! ", computer, " beats ", player_move)
        else:
            print("You win! ", player_move, " beats ", computer)

    elif player_move == "scissors":
        if computer == "rock":
            print ("You lose! ", computer, " beats ", player_move)
        else:
            print("You win! ", player_move, " beats ", computer)




