print('Welcome to my Quiz Game')

suggestion = input('Do you want to guess and play?').lower()

count = 0
wrong = 0

if suggestion in ['yes', 'y']:
    print('Great! Let\'s start the quiz.')
    questions = {
        "What is the capital of France?": "paris",
        "What is 2 + 2?": "4",
        "What is the largest ocean on Earth?": "pacific",
        "Who wrote 'Romeo and Juliet'?": "shakespeare",
        "What is the boiling point of water in Celsius?": "100",
        "Which planet is known as the Red Planet?": "mars",
        "What is the chemical symbol for gold?": "au",
        "Which country is famous for the Great Wall?": "china",
        "Which animal is known as the 'Ship of the Desert'?": "camel",
        "What is the largest mammal in the world?": "blue whale",
        "What is the smallest prime number?": "2",
        "What is the currency of Japan?": "yen",
        "What is the tallest mountain in the world?": "everest",
        "What is the fastest land animal?": "cheetah",
        "What is the main ingredient in guacamole?": "avocado",
        "What is the largest planet in our solar system?": "jupiter",
        "What is the chemical symbol for water?": "h2o",
        "What is the capital of Australia?": "canberra",
        "What is the largest desert in the world?": "sahara",
        "What is the smallest country in the world?": "vatican city"
    }

    for question, answer in questions.items():
        user_answer = input(question + ' ').lower()
        if user_answer == answer:
            print('Correct!')
            count += 1
        else:
            print(f'Wrong! The correct answer is {answer}.')
            wrong += 1

    print(f'You got {count} correct and {wrong} wrong.')
else:
    quit()