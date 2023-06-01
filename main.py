import requests
URL = "https://opentdb.com/api.php?category=9&type=boolean&"

print("Welcome to trivia!")
print()

difficulty = input("What is the difficulty level you want to play at? \nHere are the options: easy, medium, hard: ").lower()
URL = URL + "difficulty=" + difficulty + "&"
print()

questions = input("How many questions do you want? \nChoose a number between 1 and 10: ")
URL = URL + "amount=" + str(questions)

print()
print("Please answer the following questions with true or false.") 
print("Note: &#039; should be replaced by an apostrophe")
print("Note: &quot should be replaced by a quotation mark")
print("&Aring; should be replaced by a letter A")
print("_"*67)
print()


response = requests.get(URL)
response.raise_for_status()
data = response.json()


score = 0
for result in data["results"]:
  guess = input(result["question"])
  answer = result["correct_answer"]
  if guess.upper() == answer.upper():
    score += 1
    print("CORRECT")
    print()
  else:
    print("INCORRECT")
    print()

print("Congrats! You got " + str(score) + "/" + str(questions) + "questions correct!")





