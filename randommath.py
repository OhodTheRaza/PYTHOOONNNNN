import random 
secret_number = str(random.randint(0,10))
print("I have generated a number try to guess it right good luck !!")
playing = True
while playing:
    users_input = input("Enter Your Best Guess: \n")
    if users_input == secret_number:
        print("Good job you got it right ")
        break
    else:
        print("Bad guess Try to guess the number again !")