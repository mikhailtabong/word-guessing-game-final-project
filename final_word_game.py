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
    return random.choice(word_bank)

def play_game(player_count):
    print("Welcome to the Word Guessing Game!")
    print("The theme of the word bank is musical instruments.")
    print("Guess the secret word by entering one letter at a time.")
    print("After guessing a letter, you must guess the word.")
    print("Each player will take turns guessing.")
    print("You have 3 attempts per turn. Let's begin!\n")

    secret_word = choose_word()

    player_scores = {}

    for current_player in range(1, player_count + 1):
        input("Press Enter to start Player {}'s turn...".format(current_player))
        print("\n" * 30)
        print("Player", current_player, ", it's your turn.")
        print("Number of letters in the word:", len(secret_word))
        print()

        guessed_letters = []
        letter_guesses = 0
        word_guesses = 0
        attempts = 3

        while attempts > 0:
            print("Attempts left:", attempts)
            guess = input("Enter a letter or guess the word: ").lower()

            if len(guess) == 1 and guess.isalpha():
                letter_guesses += 1
                if guess in guessed_letters:
                    print("You've already guessed that letter.")
                    print()
                    continue
                guessed_letters.append(guess)

                if guess in secret_word:
                    occurrences = secret_word.count(guess)
                    print(f"Good guess! The letter '{guess}' occurs {occurrences} time(s) in the word.")
                else:
                    print("Incorrect guess.")
                attempts -= 1

            elif len(guess) > 1 and guess.isalpha():
                word_guesses += 1
                if guess == secret_word:
                    print("\nCongratulations, Player", current_player, "! You guessed the word:", secret_word)
                    break
                else:
                    print("Incorrect guess.")
                    attempts -= 1
            else:
                print("Invalid input. Please enter a single letter or guess the entire word.")

            print()

        if attempts == 0:
            print("Player", current_player, ", you've run out of attempts.")
            print()

        player_scores[current_player] = (letter_guesses, word_guesses)

    print("\n" * 30)
    print("The correct word was:", secret_word)
    print("Player scores:")
    for player, score in player_scores.items():
        print("Player", player, "- Letter guesses:", score[0], ", Word guesses:", score[1])

    max_letter_guesses = max(score[0] for score in player_scores.values())
    max_word_guesses = max(score[1] for score in player_scores.values())

    winners = [player for player, score in player_scores.items() if score == (max_letter_guesses, max_word_guesses)]

    if len(winners) == 1:
        print("Player", winners[0], "wins!")
    else:
        print("It's a draw!")

def main():
    while True:
        try:
            player_count = int(input("Enter the number of players (1-4): "))
            if player_count < 1 or player_count > 4:
                raise ValueError
            break
        except ValueError:
            print("Please enter a number between 1 and 4.")

    play_game(player_count)

if __name__ == "__main__":
    main()
