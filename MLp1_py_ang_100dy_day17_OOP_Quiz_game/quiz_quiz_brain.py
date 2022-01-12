
class QuizBrain:
    def __init__(self, q_list):
        self.score = 0
        self.question_no = 0
        self.question_list = q_list

    def still_has_questions(self):
        # Return "True" or "False" directly
        return self.question_no < len(self.question_list)
                # Equivalent to following::
        # if self.question_no < len(self.question_list):
        #     return True
        # else:
        #     return False

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        ans = input(f"Q. {self.question_no}: {current_question.text}, True/False: ")
        # not using a dictionary so dont use self.question_list[self.question_no]['text']. Use "." for object
        self.is_correct(ans, current_question.answer) #always use "self" to recocnise the current object's method
    
    def is_correct(self, u_ans, actual_ans):
        if u_ans.lower() == actual_ans.lower():
            print("You are right")
            self.score += 1
        else:
            print("Soory you are wrong")
        
        print(f"yor score is {self.score}/{self.question_no}")
        print("\n")


# python quiz_quiz-brain.py