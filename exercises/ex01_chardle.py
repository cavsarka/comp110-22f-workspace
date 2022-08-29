"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730615401"

input_word: str = input("Enter a 5-character word: ")

if len(input_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

input_character: str = input("Enter a single character: ")

if len(input_character) != 1:
    print("Error: Character must be a single character")
    exit()

print("Searching for " + input_character + " in " + input_word)

match_counter = 0
if input_word[0] == input_character:
    print(input_character + " found at index 0")
    match_counter += 1

if input_word[1] == input_character:
    print(input_character + " found at index 1")
    match_counter += 1

if input_word[2] == input_character:
    print(input_character + " found at index 2")
    match_counter += 1

if input_word[3] == input_character:
    print(input_character + " found at index 3")
    match_counter += 1

if input_word[4] == input_character:
    print(input_character + " found at index 4")
    match_counter += 1


if match_counter == 0:
    print("No instances of {} found in {}".format(input_character, input_word))
elif match_counter == 1:
    print("{} instance of {} found in {}".format(match_counter, input_character, input_word))
else:
    print("{} instances of {} found in {}".format(match_counter, input_character, input_word))