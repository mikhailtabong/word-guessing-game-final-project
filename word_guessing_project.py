import random

word_bank = [
    "viola", "banjo", "cello", "drum", "euphonium", "flute",
    "guitar", "harp", "violin", "trombone", "trumpet", "saxophone",
    "clarinet", "piano", "harmonica", "ukulele", "mandolin", "oboe",
    "xylophone", "bagpipes", "bassoon", "didgeridoo", "dulcimer",
    "fiddle", "marimba", "clarineo", "timpani", "synthesizer", "theremin",
    "zither", "accordion", "tabla", "bongo", "chimes", "conga", "digeridoo",
    "maracas", "panpipe", "sitar", "tambourine", "tuba", "accordion",
    "balalaika", "bouzouki", "djembe", "flugelhorn", "glockenspiel",
    "kazoo", "lute", "lyre", "melodica", "ocarina", "shamisen", "sitar",
    "vibraphone", "washboard", "whistle", "zurna"
]

def choose_word():
    """Selects a random word from the word bank."""
    return random.choice(word_bank)

def display_word(word, guessed_letters):
    """Displays the word with guessed letters filled in."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def main():
    print("Welcome to the Word Guessing Game!")
    print("Guess the secret word by entering one letter at a time.")
    print("You have 3 attempts. Let's begin!\n")

    secret_word = choose_word()
    guessed_letters = []
    attempts = 3

    while attempts > 0:
        print("Word:", display_word(secret_word, guessed_letters))
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Good guess!")
        else:
            print("Incorrect guess.")
            attempts -= 1
            print("Attempts left:", attempts)

        if "_" not in display_word(secret_word, guessed_letters):
            print("\nCongratulations! You guessed the word:", secret_word)
            break

    if attempts == 0:
        print("\nSorry, you've run out of attempts. The word was:", secret_word)

if __name__ == "__main__":
    main()
