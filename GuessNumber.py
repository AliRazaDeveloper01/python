import random
def game():
    randomNo = random.randint(1,100)
    return randomNo
while True:
    inputs = int(input("Guess a number between 1-100:   "))
    x =game()
    if inputs == x:
        print(f"You have entered the correct number.")
        break
    elif inputs<=0 or inputs>=100:
        print("you have entered the wrong number.") 
    elif inputs<x:
        print("Number is too low.")
    elif inputs>x:
        print("Input is too higth")
    print("=======================================================")
    