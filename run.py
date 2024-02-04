# my imports,"these need to be installed"
import colorama
# for color and autorest to the orignal color.
from colorama import Fore, Style
# ASCII art text.
import pyfiglet
from pyfiglet import Figlet
from pyfiglet import fonts

# my imports,"installation not needed"
import time
import pycountry

colorama.init(autoreset=True)

# introduction( title and rules)
print((colored(pyfiglet.figlet_format("PYTHON QUIZ", font='anishadow',
                                      color='green', justify='center',
                                      width=70))))
print(f"{Fore.LIGHTYELLOW_EX}       Please select the correct answer.\n\n"
      f"{Fore.LIGHTGREEN_EX}     # For each correctly answered question,\n"
      "   answered within 12 seconds, you will earn 10 points.\n"
      "   If it takes longer than that, you earn 5 points.\n"
      "     # After the game to exit type NO/no.\n"
      "     # To replay the game type YES/yes.\n"
      "     # At the end of the game you will get a final score.\n")
print('******************************************************\n')


# define location function
# which country are you in
def location():
    while True:
        # Ask the user for their country
        country_name = input('Which country are you in? ')

        # Look up the country by its name
        country = pycountry.countries.get(name=country_name)
        if country:
            print(f" {Fore.LIGHTGREEN_EX}{country.name}\n")
            print('******************************************************\n')
            break  # Exit the loop once a valid country is found
        else:
            print(f" {Fore.LIGHTRED_EX}  Error, type in your country.\n")
            print('******************************************************\n')


# User name function defined
def username():
    user_name = input('What is your name? ')

    # Ensure that username is not empty
    if user_name.strip():
        print(f"    {Fore.LIGHTGREEN_EX}Hello \
{user_name}, welcome to our quiz game!\n")
        print('******************************************************\n')


# Define to validate the answer.
def validate(answer, num_options):
    if answer.isdigit():
        int_answer = int(answer)
        if 1 <= int_answer <= num_options:
            return int_answer
    print(f"{Fore.LIGHTRED_EX}Error, enter a valid number (1-{num_options})")
    return None


# The main quiz function
def quiz(questions):
    score = 0
    for question in questions:
        print(question["question"])
        for option in question["options"]:
            print(option)

        # Start the timer
        start_time = time.time()
        # I set elapsed_time to 12 seconds
        elapsed_time = 12

        while True:
            answer = input(f"{Fore.LIGHTBLUE_EX}  Please answer?  ")
            (f"(1-{len(question['options'])}): ")
            int_answer = validate(answer, len(question["options"]))
            if int_answer is not None:
                # End the timer and calculate elapsed time
                end_time = time.time()
                elapsed_time = end_time - start_time
                break

        if int_answer == question["answer"]:
            # Changed to check if under or equal to 12 seconds
            if elapsed_time <= 12:
                print(f"{Fore.LIGHTGREEN_EX} Correct! 10 points ")
                score += 10
            else:
                print(f"{Fore.LIGHTGREEN_EX} Correct! 5 points ")
                score += 5
        else:
            print(f"{Fore.LIGHTRED_EX} Incorrect! ")
        print('****************************************************\n')

    # Print the final score after all questions have been answered
    print(f"{Fore.LIGHTBLUE_EX}You scored: {score}\
{Fore.LIGHTGREEN_EX} out of {len(questions) * 10}\n")
    print('*****************************************************\n')


# Call the location and username functions
location()
username()

# Define the list of quiz questions
questions = [
    {
        "question": "Which of the following is \
not a primitive data type in Python?",
        "options": ["1) Integer", "2) String", "3) List", "4) Function"],
        "answer": 4
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["1) Jupiter", "2) Mars", "3) Earth"],
        "answer": 1
    },
    {
        "question": "What is the result of the following code snippet?\n"
                    "code: x = 7, followed by (x * 3)?",
        "options": ["1) 8", "2) error", "3) 15", "4) 21"],
        "answer": 4
    },
    {
        "question":
        "Which programming language is known as the 'language of the web'?",
        "options": ["1) Python", "2) Java", "3) JavaScript"],
        "answer": 3
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["1) define", "2) func", "3) def", "4) function"],
        "answer": 3
    },
    {
        "question":
        "What does the 'self' parameter refer to in a class method in Python?",
        "options": [
            "1) It refers to the current object instance",
            "2) It refers to the parent class",
            "3) It refers to the derived class",
            "4) It refers to the static class"
        ],
        "answer":
        1
    },
    {
        "question":
        "Which module in Python is used for working with regular expressions?",
        "options": ["1) datetime", "2) math", "3) os", "4) re"],
        "answer": 4
    },
    {
        "question": "How do you comment a line of code in Python?",
        "options":
        ["1) // comment", "2) /* comment */", "3) # comment", "4) n"],
        "answer": 3
    },
]

# Start the quiz
quiz(questions)

while True:
    # Ask the player if they want to play again
    repeat = input(f"{Fore.LIGHTYELLOW_EX}\
you wish Replay, (YES/NO)? ").lower()
    print('\n**************************************************************\n')
    # Restart the quiz
    if repeat == 'yes':
        quiz(questions)
    elif repeat == 'no':
        # Game over message
        print(pyfiglet.figlet_format("Goodbye, see you soon!", font='slant',
                                     justify='center', width=65))
        print(f"{Fore.LIGHTYELLOW_EX}\n************************************\n")
        print('\n   Exiting the quiz now... \n')

        break
    else:
        print(f"{Fore.LIGHTRED_EX} Invalid response. please type yes or no!\n")
