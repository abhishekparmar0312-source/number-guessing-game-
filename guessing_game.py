# NUMBER GUESSING GAME
import random

MAX_ATTEMPTS = 3
LOW, HIGH = 1, 5

secret = random.randint(LOW, HIGH)
print(20 * "=")
print("NUMBER GUESSING GAME")
print(20 * "=")
print(f"GUESS THE NUMBER BETWEEN {LOW} AND {HIGH}")

attempts = 1
while attempts <= MAX_ATTEMPTS:
    try:
        guess = int(input(f"Attempt {attempts}/{MAX_ATTEMPTS} - Enter your guess: "))
    except ValueError:
        print("⚠️ Please enter a valid number!")
        continue  # doesn't use up an attempt

    if not LOW <= guess <= HIGH:
        print(f"⚠️ Please guess between {LOW} and {HIGH}!")
        continue

    if guess == secret:
        print("🤩CORRECT GUESS!!")
        break

    hint = "too low" if guess < secret else "too high"
    print(f"😞WRONG GUESS, {hint}. TRY AGAIN!!")
    attempts += 1
else:
    print("😞GAME OVER, NO CHANCES LEFT")
    print(f"The secret number was {secret}")
