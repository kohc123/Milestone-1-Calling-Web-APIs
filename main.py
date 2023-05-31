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


def trace(*args):
  print (*args)
  pass

trace ("Calling", URL)
response = requests.get(URL)
response.raise_for_status()
data = response.json()

trace ("\nText returned:", response.text)

trace ("\nHere are all the key/value pairs in the JSON response:")
for key, value in data.items():
  trace (key, ": ", value)

for result in data["results"]:
  guess = input(result["question"])
