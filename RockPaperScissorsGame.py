import random
choices = ['Rock, Paper, Scissors']
playing = True
while playing:
    user = input("Choose 1 Rock, Paper or Scissors: ")
    computer = random.choice(choices)
    if computer == user:
        print('Its a Tie Try again')
    elif (user == "Rock" and computer == "Scissors") or (user == "Scissors" and computer == "Paper") or (user == "Paper" and computer == "Rock"): 
        print("You Win Congrats")
        again = (input("Wanna try again? (Yes/No): "))
        if again =="Yes":
           continue
        break
    else:
        print("You Lose ")
        again = (input("Wanna try again? (Yes/No): "))
        if again =="Yes":
            continue
        break