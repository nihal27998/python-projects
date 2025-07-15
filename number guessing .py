import random
guessing_the_number = random.randint(0,100)
while True:
    try:
        guess = int(input("guess the number between 0 to 100 😁 : "))
        if guess > guessing_the_number:
            print("Too high🤯")
        elif guess < guessing_the_number:
            print("Too low😢")
        else:
            print("Congratulations!!! YOu've guessed the number correct!!✨😘")
            break
    except ValueError:
        print("Please Enter a valid nnumber😒")
