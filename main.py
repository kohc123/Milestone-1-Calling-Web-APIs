import requests
URL = "https://opentdb.com/api.php?category=9&type=boolean&"

print("Welcome to trivia!")
print()

difficulty = input("What is the difficulty level you want to play at? \nHere are the options: easy, medium, hard: ").lower()
URL = URL + "difficulty=" + difficulty + "&"
print(URL)

questions = input("How many questions do you want? \nChoose a number between 1 and 10: ")
URL = URL + "amount=" + str(questions)

print(URL)


