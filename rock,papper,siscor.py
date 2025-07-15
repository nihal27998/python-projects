import random
while True:
    choices = ('r','p','s')
    emojis = {'r':'🗿','s':'✂','p':'📄'}
    user_choice = input('Rock,paper or siscor? (r/p/s): ').lower()
    if user_choice not in choices:
        print("Invalid Input!")
        continue
    computer_choice = random.choice(choices)
    print(f"you choose{emojis[user_choice]}")
    print(f"computer choose{emojis[computer_choice]}")
    if user_choice == computer_choice:
        print('Tie!!')
    elif(user_choice =='r' and computer_choice=='s') or (user_choice =='s'and computer_choice =='r') or (user_choice=='p' and computer_choice=='r'):
        print('You win!')
    else:
        print('You lose!!')
    should_continue = input('comtinue? (y/n): ').lower()
    if should_continue == 'n':
        break