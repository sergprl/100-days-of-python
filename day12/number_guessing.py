import random 

MIN_NUMBER = 1
MAX_NUMBER = 100

def print_welcome():
    print(f"""Welcome to the Number Guessing Game!
    I'm thinking of a number between {MIN_NUMBER} and {MAX_NUMBER}.""")

def choose_dificulty():
    difficulty = ""

    while difficulty != 'easy' and difficulty != 'hard':
        difficulty = input ("Choose a dificulty. Type 'easy' or 'hard': ")

    return difficulty

def get_number_of_attempts(difficulty):
    if (difficulty == 'easy'):
        return 10
    else:
        return 5

def print_hint(target, guess):
    if (guess > target):
        print("Too high.")
    elif (guess < target):
        print("Too low.")

def get_guess():
    guess = 0
    valid_guess = False

    while not valid_guess:
        try:
            guess = int(input("Make a guess: "))
            valid_guess = True
        except Exception:
            print("Enter a valid number")

    return guess

def create_target():
    return random.randint(MIN_NUMBER, MAX_NUMBER)

def play():
    print_welcome()
    total_attempts = get_number_of_attempts(choose_dificulty())
    current_attempts = 0
    print(f"You have {total_attempts} remaining to guess the number.")
    target = create_target()

    while(current_attempts < total_attempts):
        guess = get_guess()
        if target != guess:
            print_hint(target, guess)
        else:
            print("You guessed the number!")
            return
        current_attempts +=1

play()
print("Game over!")

