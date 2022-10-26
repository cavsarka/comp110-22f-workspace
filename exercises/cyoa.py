"""EX05 - 'list' Utility Functions."""

__author__ = "730615401"

import random

CHECK_MARK = "\U00002705"
X_MARK = "\U0000274C"
DOUBLE_EXCLAMATION = "\U0000203C"
STOP_EMOJI = "\U0001F6D1"

points: int = 0
player: str = ""
running: bool = True


def greet() -> None:
    """Greets player and tells them about the game."""
    global player
    player = str(input("What's your name? "))
    print(f"Welcome to the \"Guess the Flip\" game, {player}! Enter h for heads, or t for tails to call the flip, and if you get it right, you continue. If you get it wrong, you lose and the game ends.")


def iterate_points(input: int) -> int:
    """Adds one to the global variable points after every correct guess."""
    global points
    input += 1
    points = input
    return input


def guess_and_check(user_guess: str, result: str) -> bool:
    """Checks if user guess and coin flip result is the same. If so, game continues, if not, it stops."""
    global points
    global running
    global player
    if user_guess == "quit":
        print(f"{STOP_EMOJI}{STOP_EMOJI}{STOP_EMOJI} You chose to end the game early, {player}. Your final score was {points}!")
        running = False
    elif user_guess.lower() == result:
        running = True
        iterate_points(points)
        print(f"{CHECK_MARK}{CHECK_MARK}{CHECK_MARK} Correct call, keep going! Your new score is {points}{DOUBLE_EXCLAMATION}")
    else:
        print(f"{X_MARK}{X_MARK}{X_MARK} The coin did not flip in your favor {player}, Game Over. Your final score was {points}{DOUBLE_EXCLAMATION}")
        running = False
    return running


def coin_flip() -> str:
    """Flips the coin and returns the result."""
    side = random.randint(0, 1)
    if side == 0:
        return "t"
    else:
        return "h"


def get_guess() -> str:
    """Gets a guess from the user about what they think the flip will be."""
    global player
    user_guess: str = str(input(f"What's the call {player}? (h for heads, t for tails, or \"quit\" to quit) "))
    if user_guess.lower() != "h" and user_guess.lower() != "t" and user_guess.lower() != "quit":
        user_guess: str = str(input("Input either h for heads, or t for tails: "))
    return user_guess


def main() -> None:
    """Main function."""
    greet()
    while running:
        guess_and_check(get_guess(), coin_flip())


if __name__ == "__main__":
    main()