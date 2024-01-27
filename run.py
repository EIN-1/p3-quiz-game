# my imports.
import colorama
import time
import pycountry

from colorama import Fore, Style

colorama.init(autoreset=True)


# introduction and rules
print(f"\n{Fore.GREEN}WELCOME TO THE PYTHON QUIZ GAME\n")
print('******************************************************\n')

print(f"\n{Fore.BLUE}Please select the correct answer. For each question\n"
      f"answered correctly within 15 seconds, you will earn 10 points.\n"
      f"If it takes longer than that, you earn 5 points:\n\n")
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


# The main function for the quiz
def quiz(questions):
    score = 0
    for question in questions:
        print(question["question"])
        for option in question["options"]:
            print(option)

    # Loop until a valid answer is entered
    while True:
        answer = input(f"{Fore.BLUE}Please answer\
        (1-{len(question['options'])}): ")
        int_answer = validate(answer, len(question["options"]))
        if int_answer is not None:
            # Exit the loop when the answer is valid
            break

        # Start the timer
        start_time = time.time()
        # End the timer
        end_time = time.time()
        # Calculate elapsed time
        elapsed_time = end_time - start_time

        if int_answer == question["answer"]:
            # if the participant answers within 15 seconds, earns 10 points
            if elapsed_time <= 15:
                print(f"{Fore.GREEN}Correct! 10 points")
                score += 10
            else:
                # or else participant earns only 5 points if more than 15sec.
                print(f"{Fore.GREEN}Correct! 5 points")
                score += 5
        # checking if answer is false then print incorrect.
        else:
            print(f"{Fore.RED}Incorrect!")
        print('****************************************************\n')

        # This print statement is the final quiz and shows the final score.
    print(f"{Fore.BLUE}You scored: {score}\
    {Fore.GREEN}out of {len(questions) * 10}{Style.RESET_ALL}\n")
    print('*****************************************************\n\n')


# Call the location and username function here
location()
username()

# multi-questions quiz with options and answers numbers
# define the quiz quection list
questions = [{
        "question":
        "Which of the following is not a primitive data type in Python?",
        "options": ["1) Integer", "2) String", "3) List", "4) Function"],
        "answer": 4
    }, {
        "question": "What is the largest planet in our solar system?",
        "options": ["1) Jupiter", "2) Mars", "3) Earth"],
        "answer": 1
    }, {
        "question": "What is the result of the following code snippet?\
        \ncode: x = 7, followed by (x * 3)?",
        "options": ["1) 8", "2) error", "3) 15", "4) 21"],
        "answer": 4
    }]


# Call the quiz function with the questions to start the quiz
quiz(questions)


# Ask the player if they want to play again
repeat = input(f"{Fore.YELLOW}Do you want to play again (YES/NO)? ").lower()
print('******************************************************\n')

if repeat == 'yes':
    quiz(questions)  # Restart the quiz
else:
    # Game over message
    print(f"{Fore.YELLOW}Goodbye, see you soon!\n")
    print('******************************************************\n')
