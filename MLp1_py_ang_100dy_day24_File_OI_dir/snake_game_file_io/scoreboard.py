import turtle
ALIGNMENT = 'center'
FONT = ('Arial', 16, 'normal')

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("#3c412c")
        self.penup()
        self.speed("fastest")
        self.goto(0, 310)
        self.score = 0
        # ----------- Absolute path -------------
        # with open(file= "L:/1_Development/z-codes-2.1-PYTHON/MLp1_py_ang_100dy_day24_File_OI_dir/data/high_score_record.txt", mode="r") as data:
        with open(file= "../data/high_score_record.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.update_scoreboard()

    # def gameover(self):
    #     self.goto(0 , 0)
    #     self.write(f"GAME OVER", move= False, align= ALIGNMENT, font= FONT)

    def reset_score(self):
        # Updating high_score
        if self.score > self.high_score:
            self.high_score = self.score
            # record = open(file = "high_score_record.txt", mode="a")
            # ----------- Relative path -------------
            record = open(file = "../data/high_score_record.txt", mode="w")
            record.write(str(self.high_score))
            record.close()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} \t High Score : {self.high_score}", move= False, align= ALIGNMENT, font= FONT)

    def icrease_score(self):
        self.score += 1
        self.update_scoreboard()
        
# python scoreboard.py