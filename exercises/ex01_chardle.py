"""Second Excercise"""

_author_ = "730487032"

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    quit()

character: str = input("Enter a single character: ")
if len(character) != 1:
    print("Error: Character must be a single character.")
    quit()
else:
    print("Searching for " + character + " in " + word)

number: int = 0

if character == word[0]:
    print(character + " found at index 0")
    number = number + 1
if character == word[1]:
    print(character + " found at index 1")
    number = number + 1
if character == word[2]:
    print(character + " found at index 2")
    number = number + 1
if character == word[3]:
    print(character + " found at index 3")
    number = number + 1
if character == word[4]:
    print(character + " found at index 4")
    number = number + 1

if number == 1:
    print("1 instance of " + character + " found in " + word)
if number == 0:
    print("No instances of " + character + " found in " + word)
if number > 1:
    print(str(number) + " instances of " + character + " found in " + word)