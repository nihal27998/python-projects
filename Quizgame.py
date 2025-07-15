print("Welcome to my game🥰")
playing = input("Do you wanna play the game baby?🤔 (y/n): ").lower()
if playing == 'y':
    print("Let's play😍")
    score = 0  
    answer = input("1. Who is known as Father of Continental Drift?🤔 ").lower()
    if answer == 'sir alfred wegner':
        print("Correct baby!😁")
        score += 1
    else:
        print("I am sorry babu your answer is wrong!😔")

    answer = input("2. The Tropic of Cancer does NOT pass through which of the following?🤔 ").lower()
    if answer == 'egypt':
        print("Correct baby!😁")
        score += 1
    else:
        print("I am sorry babu your answer is wrong!😔")

    answer = input("3. Which river is known as the 'Yellow River'?🤔 ").lower()
    if answer == 'huang he':
        print("Correct baby!😁")
        score += 1
    else:
        print("I am sorry babu your answer is wrong!😔")

    answer = input("4. Which of the following is the most densely populated country?🤔 ").lower()
    if answer == 'bangladesh':
        print("Correct baby!😁")
        score += 1
    else:
        print("I am sorry babu your answer is wrong!😔")

    answer = input("5. Which of the following crops is a Kharif crop?🤔 ").lower()
    if answer == 'rice':
        print("Correct baby!😁")
        score += 1
    else:
        print("I am sorry babu your answer is wrong!😔")

    answer = input("6. Which state in India receives the highest rainfall?🤔 ").lower()
    if answer == 'meghalaya':
        print("Correct baby!😁")
        score += 1
    else:
        print("I am sorry babu your answer is wrong!😔")

    print("You got " + str(score) + " questions correct!")
    print("You got " + str((score / 6) * 100) + "%.")
    print("Congratulations!, for your score baby😘")
    print("Proud of you🥳")
    print("Thanks for playing the game baby, i love you!😘")

elif playing == 'n':
    print("Please play my game baby😭")
else:
    print("Invalid input baby!!🙄")
