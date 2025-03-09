import random  

print("🎮 WELCOME TO THE GAME! 🎮\n")
print("🔥 This is a NUMBER GUESSING GAME!")
print("🎯 You have 5 attempts to guess a number between 50 and 100.")
print("✨ Let's start the game! 🚀\n")

number_to_guess = random.randint(50, 100)
chances = 5
guess_counter = 0

while guess_counter < chances:
    guess_counter += 1  
    my_guess = int(input("🔢 Enter your guess: "))

    if my_guess == number_to_guess:
        print(f"🎉 Congrats! You guessed the number {number_to_guess} correctly in {guess_counter} attempts! 🏆")
        break
    elif my_guess < number_to_guess:
        print("📉 Your guess is too low! Try again. 🔄")
    elif my_guess > number_to_guess:
        print("📈 Your guess is too high! Try again. 🔄")

if guess_counter >= chances and my_guess != number_to_guess:
    print(f"❌ Oops! The number was {number_to_guess}. Better luck next time! 🎭")

