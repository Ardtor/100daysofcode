class QuizBrain:
    def __init__(self, q_list) -> None:
        self.q_number = 0
        self.q_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.q_number < len(self.q_list)

    def next_question(self):
        question = self.q_list[self.q_number]
        self.q_number += 1
        user_answer = input(f"Q.{self.q_number}. {question.text} ([T]rue or [F]alse): ")
        self.check_question(user_answer, question.answer)

    def check_question(self, user_answer, question_answer):
        if user_answer.lower() == question_answer.lower():
            self.score += 1
            print(f"\nCorrect! Your score is now {self.score}/{self.q_number}\n")
        else:
            print(f"\nIncorrect, the answer was {question_answer}. Your score is still {self.score}/{self.q_number}\n")
