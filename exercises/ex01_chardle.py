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
for num in range(0, 5):
    if input_word[num] == input_character:
        print(str(input_character) + " found at index " + str(num))
        match_counter += 1
    num += 1

if match_counter == 0:
    print("No intances of {} found in {}".format(input_character, input_word))
else:
    print("{} instances of {} found in {}".format(match_counter, input_character, input_word))