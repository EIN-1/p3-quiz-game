# my imports.
import colorama
import time
import pycountry
import os

from colorama import Fore, Style, Back

colorama.init(autoreset=True)


# introduction and rules
print(f"\n{Fore.GREEN}WELCOME TO THE PYTHON QUIZ GAME\n")
print('******************************************************\n')

print(f"\n{Fore.BLUE}Please select the correct answer. For each question "
      f"answered correctly within 15 seconds, you will earn 10 points. "
      f"If it takes longer than that, you earn 5 points:\n\n")
print('******************************************************\n')


# which country are you in
def location():
    while True:
        # Ask the user for their country
        country_name = input('Which country are you in? ')

        # Look up the country by its name
        country = pycountry.countries.get(name=country_name)
        if country:
            print(f"{Fore.GREEN}{country.name}\n")
            break  # Exit the loop once a valid country is found
            print('******************************************************\n')
        else:
            print(f"{Fore.RED}Error, type in your country.\n")
            print('******************************************************\n')


# Call the location function to prompt for input
location()


# User name
def username():

    user_name = input('What is your name? ')

    # Ensure that username is not empty
    if user_name.strip():
        print(f"{Fore.GREEN}Hello {user_name}, welcome to our quiz game!\n")
        print('******************************************************\n')


# Call the username function to prompt for input
username()

# multi-questions quiz with options and answers numbers
questions = [
        {
            "question":
            "Which of the following is not a primitive data type in Python?",
            "options": ["1) Integer", "2) String", "3) List", "4) Function"],
            "answer": 4
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["1) Jupiter", "2) Mars", "3) Earth"],
            "answer": 1
        },
        {
            "question": "What is the result of the following code snippet?",
            "code": ["x = 7", "print(x * 3)"],
            "options": ["1) 8", "2) error", "3) 15", "4) 21"],
            "answer": 4
        },
    ]


def quiz(questions):
    score = 0
    for question in questions:
        print(question["question"])

        for option in question["options"]:
            print(option)
        answer = input(f"{Fore.BLUE}Your answer: ")

        if int(answer) == question["answer"]:
            print(f"{Fore.GREEN}Correct! 10 points\n")
            score += 10
            print('******************************************************\n')
        else:
            print(f"{Fore.RED}Incorrect!\n")
            print('******************************************************\n')
    print(f"{Fore.BLUE}You scored: {score} \
        {Fore.GREEN}out of {len(questions) * 10}\n")
    print('******************************************************\n')


quiz(questions)


# validating error in answering, not to use strings
# def validate(answers):


# if you use less than 15seconds you earn 10 points else you get 5 points
timer()


score = 0


# choice to exit or replay
print(f"{Fore.YELLOW}Do you want to play again(YES/NO)?\n")
print('******************************************************\n')


# game over message
print(f"{Fore.YELLOW}Goodbye, see you soon!\n")
print('******************************************************\n')
