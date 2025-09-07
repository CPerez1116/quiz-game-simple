# Import the Question class, the question data, and the QuizBrain class
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create an empty list to store Question objects
question_bank = []

# Loop through each dictionary in question_data
for question in question_data:
    # Extract the text and answer from each question
    question_text = question["text"]
    question_answer = question["answer"]

    # Create a new Question object using the text and answer
    new_question = Question(question_text, question_answer)

    # Add the new Question object to the question_bank list
    question_bank.append(new_question)

# Create a QuizBrain object and pass in the question bank
quiz = QuizBrain(question_bank)

# Keep asking questions until there are no more left
while quiz.still_has_questions():
    # Ask the next question
    quiz.next_question()

# Print final messages after the quiz is completed
print("You've completed the quiz")
print(f"Your final score was: {quiz.user_score}/{quiz.question_number}")
