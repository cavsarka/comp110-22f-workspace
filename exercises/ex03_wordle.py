"""EX03 - Wordle."""

__author__ = "730615401"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(searched_string: str, searched_char: str) -> bool:
    """Checks if the str in the first parameter has the character in the second parameter."""
    assert len(searched_char) == 1
    i = 0
    found = False
    while i < len(searched_string) and found is False:
        if searched_string[i] == searched_char:
            found = True
        else:
            i += 1
    return found


def emojified(guess: str, secret: str) -> str:
    """Creates emoji string based off 2 words."""
    i = 0
    emoji_string = ""
    while i < len(guess):
        if guess[i] == secret[i]:
            emoji_string += GREEN_BOX
        else:
            if contains_char(secret, guess[i]):
                emoji_string += YELLOW_BOX
            else: 
                emoji_string += WHITE_BOX
        i += 1
    return emoji_string


def input_guess(expected_length: int) -> str:
    """Ensure that the inputted word is the same length as the secret word."""
    guess_word: str = input(f"Enter a {expected_length} character word: ")
    while len(guess_word) != expected_length:
        guess_word = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess_word


def main() -> None:
    """The entry point of the program and the main game loop."""
    i = 0
    found = False
    while i < 6 and found is False:
        print(f"=== Turn {i + 1}/6")
        secret_word = "codes"
        guess_word = input_guess(len(secret_word))
        print(emojified(guess_word, secret_word))
        if guess_word == secret_word:
            print(f"You won in {i + 1}/6 turns!")
            found = True
        if i == 5 and found is False:
            print("X/6 - Sorry, try again tomorrow!")
        i += 1


if __name__ == "__main__":
    main()