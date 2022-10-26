"""EX02 - One Shot Wordle."""

__author__ = "730615401"

# from typing import final


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret_word = "python"
word_length = len(secret_word)

user_guess = str(input(f"What is your {word_length}-letter guess? "))
while len(user_guess) != word_length:
    user_guess = str(input(f"That was not {word_length} letters! Try again: "))

final_string = ""

i = 0

while i < (len(secret_word)):
    if user_guess[i] == secret_word[i]:
        final_string += GREEN_BOX
        i += 1
    else:
        letter_found = False
        alt_index = 0
        while letter_found is False and alt_index < len(secret_word):
            if user_guess[i] == secret_word[alt_index]:
                letter_found = True
            alt_index += 1
        if letter_found is True:
            final_string += YELLOW_BOX
        else:
            final_string += WHITE_BOX
        i += 1

print(final_string)

right_ans = ""

for i in range(6):
    right_ans += GREEN_BOX

if final_string == right_ans:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")




def love(subject: str) -> str:
    return f"I love you {subject}"

print(love("sosa"))