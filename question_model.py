class Question:
    def __init__(self, q_text, q_answer):
        """The purpose of this constructor is to create instances of a class called "Question,"
        where each instance represents a specific question and its answer.
        When you create an instance of the "Question" class and pass the question text and answer as arguments,
        the constructor initializes the "text = question" and the "answer = correct_answer" instance variables
        with those values."""
        self.text = q_text
        self.answer = q_answer


# new_q = Question("How many fingers does a hand have?", 5)
# print(new_q.text)
