from question_model import Question
# from data import question_data

from quiz_brain import QuizBrain
import ui
import html
import requests

# get questions from API
# Separate parameters from this URL:
# https://opentdb.com/api.php?amount=10&type=boolean
# "https://opentdb.com/api.php" is url and "amount=10&type=boolean" are parameters

parMs = {
    "amount" : 10,
    "type" : "boolean"
}

api_ques = requests.get(url = "https://opentdb.com/api.php", params = parMs)
api_ques.raise_for_status()
question_data = api_ques.json()["results"]

# Html code conversion: use "html" module and use unescape
# question_text = html.unescape(question["question"])

question_bank = []
for question in question_data:
    # Use unescape() for Html entities
    question_text = html.unescape(question["question"])
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

# passing question_bank to UI module & Generating UI
quiz_ui = ui.quiz_ui(quiz)


# python quiz_main_instructor.py
