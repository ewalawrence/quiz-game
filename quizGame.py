# Quiz Game

questions = ("Earth has how many moons?: ",
             "Which planet is the closest to the sun?: ",
             "Which planet is the largest?: ",
             "Which planet is considered earth twin?: ",
             "One of the following is not found in the solar system?: ",)
options = (("A. 1", "B. 3", "C. 5", "D. 2", "E. 8",), 
           ("A. Jupiter", "B. Mars", "C. Saturn", "D. Venus", "E. Mercury"), 
           ("A. Mars", "B. Pluto", "C. Jupiter", "D. Uranus", "E. Saturn"), 
           ("A. Saturn", "B. Jupiter", "C. Venus", "D. Mars", "E. Mercury"), 
           ("A. Asteroids", "B. Comets", "C. Moon", "D. Planets", "E. satellites"),)
answers = ("A", "B", "C", "D", "E")
guesses = []
questionNum = 0
score = 0

for question in questions:
    print("--------------")
    print(question)

    for option in options[questionNum]:
        print(option)

    guess = input("Enter (A, B, C, D, E): ").upper()
    guesses.append(guess)

    if guess == answers[questionNum]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT")
        print(f"{answers[questionNum]} is the correct answer")
        
    questionNum += 1
score = score / len(questions) * 100

print("---------------------")
print("        ANSWER       ")
print("---------------------")

print("Answers: ", end="")
for answer in answers:
     print(answer, end=" ")
print()

print("Guess: ", end="")
for guess in guesses:
     print(guess, end=" ")
print()
    
print(f"Your total score is: {score}")
print()
