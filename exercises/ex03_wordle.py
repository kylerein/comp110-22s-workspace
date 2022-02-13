"""EX03 - Wordle."""

__author__ = "730403346"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(a: str, b: str) -> bool:
    """Returns True if character 'b' is in word 'a'."""
    assert len(b) == 1
    index: int = 0
    while index < len(a):
        if a[index] == b:
            return True
        index = index + 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Returns emojis that coincide with the guess input."""
    assert len(guess) == len(secret)
    index: int = 0
    output: str = ""
    while index < len(secret):
        if guess[index] == secret[index]:
            output = output + GREEN_BOX
            # if the index of the word is in the correct spot of the correct word, it will put the green box emoji
        else:
            exists: bool = False
            altindex: int = 0
            while not exists and altindex < len(secret):
                if guess[index] == secret[altindex]:
                    exists = True
                altindex = altindex + 1
            if exists:
                output = output + YELLOW_BOX
                # this is now comparing the letters entered in the guess to the secret word and identifying if that letter is in the secret word
            else:
                output = output + WHITE_BOX
                # if one of the letters guessed is not in the word, it will put a white box
        index = index + 1
    return output
