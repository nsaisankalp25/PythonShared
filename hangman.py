import random

def choose_word():
    words = ["truck", "grape", "orange", "car", 'jackfruit', 'peas']
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

word = choose_word()
guessed_letters = []
attempts = 8

print("Welcome to Hangman!")
print("You have 8 attempts to guess the word.")

while attempts > 0:
    print("\n" + display_word(word, guessed_letters))

    if "_" not in display_word(word, guessed_letters):
        print("Congratulations! You've guessed the word:", word)
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You've already guessed that letter. Try again.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        attempts -= 1
        print(f"Wrong! You have {attempts} attempts left.")

    if attempts == 0:
        print("\nGame over! The word was:", word)
