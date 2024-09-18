from Day17_Quizdata import question_data
from Day17_Quiz_question_model import Question
from Day17_Quiz_brain import quiz

question_bank = []

# Looping through the question data and creating a new Question object for each one
for problem in question_data:
    # Extracting the question text and answer from the dictionary
    question_text = problem["question"]
    question_answer = problem["correct_answer"]
    # Creating a new Question object with the question text and answer
    new_question = Question(question_text, question_answer)
    # Appending the new Question object to the question bank list
    question_bank.append(new_question)

# Creating a new Quiz object with the question bank list
Trivia = quiz(question_bank)

# Looping through all the questions in the question bank
while Trivia.question_number < len(Trivia.question_list):
    # Calling the next question method to ask the next question
    Trivia.next_question()
    # Incrementing the question number to move to the next question
    Trivia.question_number += 1

# Printing the final score once all the questions have been asked
print("You have completed the quiz. Your final score is: ",Trivia.score,"/",Trivia.question_number)