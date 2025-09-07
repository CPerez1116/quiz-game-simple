class QuizBrain:
    # Initialize the QuizBrain object
    def __init__(self, q_list):
        self.user_score = 0  # Keep track of the user's score
        self.question_number = 0  # Keep track of which question number the user is on
        self.question_list = q_list  # List of Question objects

    # Check if there are still questions left in the quiz
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # Ask the next question in the list
    def next_question(self):
        # Get the current question object from the list
        current_question = self.question_list[self.question_number]

        # Increment the question number for the next round
        self.question_number += 1

        # Ask the user for their answer
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")

        # Check if the user's answer is correct
        self.check_answer(user_answer, current_question.answer)

    # Check if the user's answer matches the correct answer
    def check_answer(self, user_answer, correct_answer):
        # Compare answers (case-insensitive)
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.user_score += 1  # Increment score if correct
        else:
            print("That's wrong.")

        # Show the correct answer and current score
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.user_score}/{self.question_number}.\n")
