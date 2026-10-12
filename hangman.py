
import random

words = ["python", "apple", "tiger", "coding", " mango"]
word = random.choice(words).strip()
guessed_letters = []
attempts = 6

print("Welcome to Hangman Game!")
print("_ " * len(word))

while attempts > 0:
    guess = input("\nGuess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")

    else:
        attempts -= 1
        print("Wrong guess!")
        print("Attempts left:", attempts)

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)

    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You won!")
        break

if attempts == 0 and not all(letter in guessed_letters for letter in word):
    print("Game over! The word was:", word)