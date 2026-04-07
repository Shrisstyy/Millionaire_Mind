import time
import pyttsx3
from ai_engine import generate_question

engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()



base_prize = 1000
level = 0
total_won = 0

speak("Welcome to Millionaire Mind!")

while True:

    next_prize = base_prize * (2 ** level)

    speak(f"If you want to quit, quit before i ask the question.")
    speak(f"If you quit now, you will take home {total_won} rupees.")
    speak("Press P to play or Q to quit")


    choice = input("Press P to play or Q to quit: ").upper()
    

    if choice == "Q":
        speak(f"You decided to quit. You won {total_won} rupees.")
        break

    # QUESTION IS STARTING
    question_data = generate_question()

    speak(f"This question is for {next_prize} rupees.")
    speak(question_data["question"])

    letters = ["A", "B", "C", "D"]

    for idx, option in enumerate(question_data["options"]):
        speak(f"{letters[idx]}) {option}")

    while True:
        answer = input("Enter your answer (A/B/C/D): ").upper()
        if answer in ["A", "B", "C", "D"] :
            break
        else:
            print("Please enter only A, B, C or D.")

    speak("Computer ji, lock kiya jaye?")
    time.sleep(1)

    speak("And the correct answer is...")
    time.sleep(1)

    correct_letter = letters[
        question_data["options"].index(question_data["correct"])
    ]

    if answer == correct_letter:
        total_won = next_prize
        speak(f"Correct! You have won {total_won} rupees.")
        level += 1
        time.sleep(1)
    else:
        speak("Wrong answer. Game Over.")
        speak(f"You go home with {total_won} rupees.")
        break