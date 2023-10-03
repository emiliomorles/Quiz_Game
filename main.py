from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []  # It organises the question with its correct answer
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank) # To print 12 Question objects
# print(question_bank[0].answer) # To print the 'answer' of Question(0).

quiz = QuizBrain(question_bank)  # It creates a quiz object

while quiz.still_has_questions():  # if quiz still has questions remaining:
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}\n")
