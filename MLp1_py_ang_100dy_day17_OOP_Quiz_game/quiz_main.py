from quiz_angela_data import question_data
import quiz_pt_1_q_model
import quiz_quiz_brain

question_bank = []

for qes in question_data:
    # qes_text = qes["text"]
    qes_text = qes["question"]

    # qes_ans = qes["answer"]
    qes_ans = qes["correct_answer"]
    
    
    new_ques_obj = quiz_pt_1_q_model.Question(qes_text, qes_ans)
    question_bank.append(new_ques_obj)

quiz = quiz_quiz_brain.QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("The Quiz if finished !!!!")
print(f"Your final score is: {quiz.score}/{quiz.question_no}")

# python quiz_main.py