import random


choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)
player = False
cpu_score = 0
player_score = 0
while True:
    # Input player's choice
    player = input("Rock, Paper or  Scissors? Enter your choice: ").capitalize()
    
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("CPU: ",computer)
            print("You lose!")
            cpu_score+=1
        else:
            print("CPU: ",computer)
            print("You win!")
            player_score+=1
    elif player == "Paper":
        if computer == "Scissors":
            print("CPU: ",computer)
            print("You lose!")
            cpu_score+=1
        else:
            print("CPU: ",computer)
            print("You win!")
            player_score+=1
    elif player == "Scissors":
        if computer == "Rock":
            print("CPU: ",computer)
            print("You lose!")
            cpu_score+=1
        else:
            print("CPU: ",computer)
            print("You win!")
            player_score+=1
    elif player=='End':
        print("Final Scores:")
        print("CPU:{}",cpu_score)
        print("Player:{}",player_score)
        break