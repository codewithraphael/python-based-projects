import random as rand

while True:
    options = ["rock", "paper", "scissors"]
    computer = rand.choice(options)

    print('choose rock, paper, or scissors')

    while True:
        try:

            user = input ('Enter your choice (rock, paper, scissors): ').lower()

            if user not in options:
                print('Invalid choice. Please try again.')
                continue

            if (
                (user == 'rock' and computer == 'scissors')
                or (user == 'paper' and computer == 'rock')
                or (user == 'scissors' and computer == 'paper')
            ):

                print(f'You chose {user}, computer chose {computer}. You win!'  )

            elif user == computer:
                print(f'You chose {user}, computer chose {computer}. It\'s a tie!')

            else:
                print(f'You chose {user}, computer chose {computer}. You lose!')

            break

        except ValueError as e:
            print(f'Error: {e}')

    replay_game = input('Do you want to play again? (yes/no): ').lower()
    if replay_game not in ['yes', 'y']:
        print('Thanks for playing!')
        break