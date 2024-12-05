class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    """
    Es lo mismo que hacer el loop con el if return true or false 
    pero en menos lineas, pude haber escrito 
    if self.question_number < len(self.question_list):
    return True
    else:
    False    
    """

    def next_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        user_answer=input(f"Q.{self.question_number}: {current_q.text} (True/False): ")
        self.check_answer(user_answer, current_q.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score: {self.score}/{self.question_number}.")
        print("\n")
