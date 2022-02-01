"""EX02 - One Shot Wordle."""

__author__ = "730403346"

secretword: str = "python"
word: str = input("What is your 6-letter guess? ")
index: int = 0
output: str = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(word) != 6:
    word = input("That was not 6 letters! Try again: ")

while index < len(secretword):
    if word[index] == secretword[index]:
        output = output + GREEN_BOX
        # if the index of the word is in the correct spot of the correct word, it will put the green box emoji
    else:
        exists: bool = False
        altindex: int = 0
        while not exists and altindex < len(secretword):
            if word[index] == secretword[altindex]:
                exists = True
            altindex = altindex + 1
        if exists:
            output = output + YELLOW_BOX
            # this is now comparing the letters entered in the guess to the secret word and identifying if that letter is in the secret word
        else:
            output = output + WHITE_BOX
            # if one of the letters guessed is not in the word, it will put a white box
    index = index + 1

print(output)

if word == secretword:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")