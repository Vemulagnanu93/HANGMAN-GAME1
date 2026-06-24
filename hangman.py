import random

# ASCII Art stages representing the hangman scaffold
HANGMAN_STAGES = [
    # 0 wrong guesses (6 attempts remaining)
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    # 1 wrong guess (5 attempts remaining)
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    # 2 wrong guesses (4 attempts remaining)
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    # 3 wrong guesses (3 attempts remaining)
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    # 4 wrong guesses (2 attempts remaining)
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    # 5 wrong guesses (1 attempt remaining)
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    # 6 wrong guesses (0 attempts remaining)
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

# Words grouped by categories (each category has 5 words)
CATEGORIES = {
    "1": ("Animals", ["elephant", "giraffe", "dolphin", "penguin", "kangaroo"]),
    "2": ("Programming", ["python", "javascript", "compiler", "database", "algorithm"]),
    "3": ("Countries", ["canada", "brazil", "germany", "australia", "japan"])
}

def play_hangman():
    print("=== Welcome to Hangman ===")
    print("Choose a category:")
    for key, (name, _) in CATEGORIES.items():
        print(f"{key}. {name}")
        
    choice = input("Enter the number of your choice (1-3): ").strip()
    if choice not in CATEGORIES:
        print("Invalid choice. Selecting a random category.")
        choice = random.choice(list(CATEGORIES.keys()))
        
    category_name, words = CATEGORIES[choice]
    print(f"\nCategory chosen: {category_name}")
    
    # Randomly select one word for the player to guess
    word_to_guess = random.choice(words).lower()
    guessed_letters = set()
    attempts_remaining = 6
    
    # Game loop
    while attempts_remaining > 0:
        # Display the current state of the hangman figure
        wrong_guesses = 6 - attempts_remaining
        print(HANGMAN_STAGES[wrong_guesses])
        
        # Display the current state of the word
        display_word = []
        for letter in word_to_guess:
            if letter in guessed_letters:
                display_word.append(letter)
            else:
                display_word.append("_")
                
        print("Word: " + " ".join(display_word))
        print(f"Remaining attempts: {attempts_remaining}")
        
        # Check if the player has guessed the entire word
        if "_" not in display_word:
            print(f"\nCongratulations! You won! The word was: {word_to_guess}")
            break
            
        # Player guess input
        guess = input("Guess a letter: ").strip().lower()
        
        # Validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter exactly one letter.")
            continue
            
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue
            
        guessed_letters.add(guess)
        
        # Check guess
        if guess in word_to_guess:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts_remaining -= 1
            
    # Print the final stage and game over message
    if attempts_remaining == 0:
        print(HANGMAN_STAGES[6])
        print(f"\nGame Over! You ran out of attempts. The word was: {word_to_guess}")

if __name__ == "__main__":
    play_hangman()
