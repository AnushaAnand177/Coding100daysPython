class quiz:
    def __init__(self, question_list):
        self.question_number = 1
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        if self.question_number < len(self.question_list):
            current_question = self.question_list[self.question_number]
            user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
            self.check_answer(user_answer, current_question.answer)
        else:
            print("No more questions available.")

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("The answer you entered in correct")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n")