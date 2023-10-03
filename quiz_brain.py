class QuizBrain:

    def __init__(self, q_list):
        """This constructor sets up the initial state of the quiz.
        It initializes the instance variables that store the list of questions,
        the current question number, and the user's score."""
        self.question_list = q_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        """This method checks whether there are more questions to be asked based on the current question number
        and the total number of questions in the question list."""
        return self.question_number < len(self.question_list)
        # Tt is exactly the same as:
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     return False

    def next_question(self):
        """It retrieves the item at the current 'question_number' from the 'question_list'.
        And it also asks for the user's answer"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """This method is used to evaluate the user's response to a question, provide feedback on whether
        the answer is correct or not, and keep track of the user's score. The score is updated based
        on the correctness of the answer., and the user is given information about the correct answer
        and their current score."""
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right.")
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
