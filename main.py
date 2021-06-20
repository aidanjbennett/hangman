import random

word_list = ["hello", "youtube", "instagram", "twitch", "tiktok"]

word = random.choice(word_list)

print(word)

display = []

guess = input("Guess a letter: ").lower()

for l in range(len(word)):
    display += "_"
    
print(display)

for letter in word:
    if letter == guess:
        print(f"Good guess {guess} is in the word")
    else:
        print(f"Incorrect guess {guess} was not in the word")

