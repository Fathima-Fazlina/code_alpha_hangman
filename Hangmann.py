import random

hangman_stages = [
    """
      |------------
      |       |
      |        
      |      
      |      
    __|_________
    """,
    """
      |------------
      |       |
      |       O
      |      
      |      
    __|_________
    """,
    """
      |------------
      |       |
      |       O
      |       |
      |      
    __|_________
    """,
    """
      |------------
      |       |
      |       O
      |      \|
      |      
    __|_________
    """,
    """
      |------------
      |       |
      |       O
      |      \|/
      |      
    __|_________
    """,
    """
      |------------
      |       |
      |       O
      |      \|/
      |      /
    __|_________
    """,
    """
      |------------
      |       |
      |       O
      |      \|/
      |      / \ 
    __|_________
    """
]
word_clue_dict = {
    'apple': 'A fruit',
    'python': 'A programming language',
    'java': 'Another programming language',
    'computer': 'A machine used for computing',
    'artificial': 'Not natural, made by humans',
    'intelligence': 'The ability to acquire and apply knowledge',
    'hangman': 'The name of this game'
}

word, clue = random.choice(list(word_clue_dict.items()))
word_display = ['_'] * len(word) 
guessed_letters = []
lives = len(hangman_stages) - 1 
print("Welcome to Hangman!")
print(f"Clue: {clue}") 
while lives > 0 and '_' in word_display:
    print(f"\nLives left: {lives}")
    print(hangman_stages[len(hangman_stages) - lives - 1]) 
    print(' '.join(word_display))
    
    guess = input("\nGuess a letter: ").lower()
    
    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
    elif guess in word:
        print(f"Good guess! {guess} is in the word.")
        for i in range(len(word)):
            if word[i] == guess:
                word_display[i] = guess  
    else:
        print(f"Wrong guess! {guess} is not in the word.")
        lives -= 1 
    
    guessed_letters.append(guess)


if '_' not in word_display:
    print(f"\nCongratulations! You've guessed the word: {''.join(word_display)}")
else:
    print(hangman_stages[-1]) 
    print(f"\nGame Over! The word was: {word}")