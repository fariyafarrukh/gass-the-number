
import random
import streamlit as st  

st.title("🎮 WELCOME TO THE GAME! 🎮")
st.subheader("🔥 This is a NUMBER GUESSING GAME!")
st.write("🎯 You have 5 attempts to guess a number between 50 and 100.")
st.write("✨ Let's start the game! 🚀")

# Session state to store the number and attempts
if "number_to_guess" not in st.session_state:
    st.session_state.number_to_guess = random.randint(50, 100)
    st.session_state.chances = 5
    st.session_state.guess_counter = 0

# Input for user guess
my_guess = st.text_input("🔢 Enter your guess:", "")

if st.button("Submit Guess"):
    if my_guess.isdigit():
        my_guess = int(my_guess)
        
        if my_guess < 50 or my_guess > 100:
            st.warning("⚠️ Please enter a number between 50 and 100!")
        else:
            st.session_state.guess_counter += 1
            
            if my_guess == st.session_state.number_to_guess:
                st.success(f"🎉 Congrats! You guessed the number {st.session_state.number_to_guess} correctly in {st.session_state.guess_counter} attempts! 🏆")
                st.session_state.number_to_guess = random.randint(50, 100)  # Reset game
                st.session_state.guess_counter = 0
            elif my_guess < st.session_state.number_to_guess:
                st.info("📉 Your guess is too low! Try again.")
            else:
                st.info("📈 Your guess is too high! Try again.")
            
            if st.session_state.guess_counter >= st.session_state.chances:
                st.error(f"❌ Oops! The number was {st.session_state.number_to_guess}. Better luck next time! 🎭")
                st.session_state.number_to_guess = random.randint(50, 100)  # Reset game
                st.session_state.guess_counter = 0
    else:
        st.warning("⚠️ Please enter a valid number!")

