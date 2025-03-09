import random  

print("🎮 WELCOME TO THE GAME! 🎮\n")
print("🔥 This is a NUMBER GUESSING GAME!")
print("🎯 You have 5 attempts to guess a number between 50 and 100.")
print("✨ Let's start the game! 🚀\n")

number_to_guess = random.randint(50, 100)
chances = 5
guess_counter = 0

while guess_counter < chances:
    try:
        my_guess = int(input("🔢 Enter your guess: "))
    except ValueError:
        print("⚠️ Invalid input! Please enter a valid number between 50 and 100.\n")
        continue  # Invalid input, try again

    if my_guess < 50 or my_guess > 100:
        print("⚠️ Please enter a number within the range (50-100). Try again!\n")
        continue  # Skip this attempt, don't count it

    guess_counter += 1  # Only count valid attempts

    if my_guess == number_to_guess:
        print(f"🎉 Congrats! You guessed the number {number_to_guess} correctly in {guess_counter} attempts! 🏆")
        break
    elif my_guess < number_to_guess:
        print("📉 Your guess is too low! Try again. 🔄")
    else:
        print("📈 Your guess is too high! Try again. 🔄")

if guess_counter >= chances and my_guess != number_to_guess:
    print(f"❌ Oops! The number was {number_to_guess}. Better luck next time! 🎭")


