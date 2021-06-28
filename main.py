import random
from hangman_words import word_list
from hangman_art import logo, stages

print(logo)

word = random.choice(word_list)

lives = 6

word_length = len(word)

display = []

end_of_game = False

while not end_of_game: 

    guess = input("Guess a letter: ").lower()

    if guess in display:
      print(f"You have already guessed {guess}")

    for l in range(word_length):
      display += "_"
        
    print(display)

    for pos in range(word_length):

        letter = word[pos]

        if letter == guess:
            display[pos] = letter

    print(f"{' '.join(display)}")

    if guess not in word:
        print(f"You guessed {guess} which is not in the word. You loose a life.")
        lives -= 1
        print
        if lives == 0:
            end_of_game = True
            print("You loose the game")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win")
    
    print(stages[lives])
