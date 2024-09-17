from Day17_Quizdata import question_data
from Day17_Quiz_question_model import Question
from Day17_Quiz_brain import quiz

question_bank = []
for question in question_data:
    new_question = Question(question['text'],question['answer'])
    question_bank.append(new_question)

Trivia = quiz(question_bank)

while Trivia.question_number < len(Trivia.question_list):
    Trivia.next_question()
    Trivia.question_number += 1

print("You have completed the quiz. Your final score is: ",Trivia.score,"/",Trivia.question_number)