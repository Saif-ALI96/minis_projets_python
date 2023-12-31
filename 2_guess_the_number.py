import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:

        guess = int(input(f"Guess a number between 1 and {x} :"))
        if guess < random_number:
            print("sorry , guess again. Too low")
        elif guess > random_number : 
            print(" sorry , guess again. Too high")

    
    print(f"Yes , congrats. You have guessed the correct number {random_number}.")


#  we ask the computer to guess the number 
def computer_guess(x):
    low = 1
    high = x
    feedback = '' 

    while feedback != 'c':

        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could be high either because low = high

        feedback = input(f"Is {guess} too high (H), too low (l), or correct (C)??")
        if feedback == "h":
            high = guess - 1
        
        elif feedback == "l":
            low = guess + 1

    print(f"Yes , the computer gussed your number, {guess}, correctly!")         

computer_guess(10)