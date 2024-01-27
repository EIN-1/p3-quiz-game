# my imports.
import colorama
import time
import pycountry
import sys

from colorama import Fore, Style

colorama.init(autoreset=True)


# introduction and rules
print(f"\n{Fore.GREEN}WELCOME TO THE PYTHON QUIZ GAME\n")
print('******************************************************\n')

print(f"{Fore.YELLOW}Please select the correct answer.\n\n"
      f"{Fore.GREEN}# For each correctly answered question,"
      "answered within 12 seconds, you will earn 10 points."
      "If it takes longer than that, you earn 5 points.\n"
      "# After the game please place ANY-KEY to leave\n"
      "# To contitue playing type yes\n")
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
            print(f"{Fore.GREEN}{country.name}\n")
            print('******************************************************\n')
            break  # Exit the loop once a valid country is found
        else:
            print(f"{Fore.RED}Error, type in your country.\n")
            print('******************************************************\n')


# User name function defined
def username():
    user_name = input('What is your name? ')

    # Ensure that username is not empty
    if user_name.strip():
        print(f"{Fore.GREEN}Hello {user_name}, welcome to our quiz game!\n")
        print('******************************************************\n')


# Define to validate the answer.
def validate(answer, num_options):
    if answer.isdigit():
        int_answer = int(answer)
        if 1 <= int_answer <= num_options:
            return int_answer
    print(f"{Fore.RED}Error, please enter a valid number (1-{num_options})")
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
            answer = input(f"{Fore.BLUE}Please answer? ")
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
                print(f"{Fore.GREEN}Correct! 10 points")
                score += 10
            else:
                print(f"{Fore.GREEN}Correct! 5 points")
                score += 5
        else:
            print(f"{Fore.RED}Incorrect!")
        print('****************************************************\n')

    # Print the final score after all questions have been answered
    print(f"{Fore.BLUE}You scored: {score}\
{Fore.GREEN} out of {len(questions) * 10}{Style.RESET_ALL}\n")
    print('*****************************************************\n\n')


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


# Ask the player if they want to play again
repeat = input(f"{Fore.YELLOW}You wish to Replay, (YES/NO)? ").lower()
print('\n******************************************************\n')
# Restart the quiz
if repeat == 'yes':
    quiz(questions)
else:
    # Game over message
    print(f"{Fore.YELLOW}Goodbye, see you soon!\n")
    print('******************************************************\n')

# Exit quiz at any time "am thinking of a button"
exit_now = input("Type 'EXIT or E/e' to quit the quiz,\
    or press Enter to contitue: ").lower()
if exit_now == 'EXIT or E':
    print('Exiting the quiz now...')
    sys.exit()


    