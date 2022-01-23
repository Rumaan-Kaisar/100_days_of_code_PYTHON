import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class quiz_ui:
    def __init__(self, quiz_brain : QuizBrain): # type-hint is used
        self.quiz = quiz_brain
        self.winDow = tkinter.Tk()
        self.winDow.title("Quizler")
        self.winDow.config(padx =20, pady = 20, bg= THEME_COLOR)
        
        self.score_label = tkinter.Label(text = "Score 0", fg = "white", bg = THEME_COLOR)
        self.score_label.grid(column = 1, row = 0)

        self.cAnvs = tkinter.Canvas(width = 300, height = 250)
        self.cAnvs.grid(column = 0, row = 1, columnspan = 2, pady = 50)
        self.question_text = self.cAnvs.create_text(
                    150, 
                    125,
                    width = 280, 
                    text = "Some text will go here", 
                    fill = THEME_COLOR,
                    font = ("Arial", 18, "italic"))

        # always remember to use keywords: "file"
        rt_btn_img = tkinter.PhotoImage(file = "./images/true.png")
        wrng_btn_img = tkinter.PhotoImage(file = "./images/false.png")

        self.crrCT = tkinter.Button(image = rt_btn_img, bd = 0, highlightthickness=0)
        self.crrCT.config(command = self.riGht, pady = 50)
        self.crrCT.grid(column = 0, row = 2)
        self.flSe = tkinter.Button(image = wrng_btn_img, bd = 0, highlightthickness=0)
        self.flSe.config(command = self.woRong, pady = 50)
        self.flSe.grid(column = 1, row = 2)

        self.next_quiz()

        self.winDow.mainloop()

    def next_quiz(self):
        self.cAnvs.config(bg = "white")
        if self.quiz.still_has_questions(): # notice "()" is used
            q_text = self.quiz.next_question()
            self.score_label.config(text = f"Score : {self.quiz.score}")
            self.cAnvs.itemconfig(self.question_text, text = q_text)
        else:
            self.cAnvs.itemconfig(self.question_text, text = "Reached to the end of the quiz")
            self.crrCT.config(state = "disabled")
            self.flSe.config(state = "disabled")

    def riGht(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    
    def woRong(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.cAnvs.config(bg = "#4DD637")
        else:
            self.cAnvs.config(bg = "#B4161B")
        self.winDow.after(1000, self.next_quiz)



    