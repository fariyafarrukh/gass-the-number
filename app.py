import random  

# رنگین ٹیکسٹ کے لیے ANSI escape codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

print(f"{CYAN}🎮 WELCOME TO THE GAME! 🎮\n")
print("🔥 This is a NUMBER GUESSING GAME!")
print("🎯 You have 5 attempts to guess a number between 50 and 100.")
print("✨ Let's start the game! 🚀\n")

number_to_guess = random.randint(50, 100)
chances = 5
guess_counter = 0

while guess_counter < chances:
    guess_counter += 1  
    my_guess = int(input(f"{YELLOW}🔢 Enter your guess: {RESET}"))

    if my_guess == number_to_guess:
        print(f"{GREEN}🎉 Congrats! You guessed the number {number_to_guess} correctly in {guess_counter} attempts! 🏆{RESET}")
        break
    elif guess_counter >= chances and my_guess != number_to_guess:
        print(f"{RED}❌ Oops! The number was {number_to_guess}. Better luck next time! 🎭{RESET}")
    elif my_guess < number_to_guess:
        print(f"{CYAN}📉 Your guess is too low! Try again. 🔄{RESET}")
    elif my_guess > number_to_guess:
        print(f"{CYAN}📈 Your guess is too high! Try again. 🔄{RESET}")
