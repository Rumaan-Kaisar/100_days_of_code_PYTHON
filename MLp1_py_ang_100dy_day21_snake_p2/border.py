import turtle

SCRN = turtle.Screen()


class Border():
    def __init__(self):
        self.border_block = []
        # Turtle shape can be modified as follows
        SCRN.register_shape("new_defined_1", ((-5, 1), (5, 1), (5, -1), (-5, -1)))
        SCRN.register_shape("new_defined_2", ((-1, 1), (1, 1), (1, -1), (-1, -1)))
        self.create_border()

    def create_block(self):
        b_blok = turtle.Turtle()
        b_blok.color("#3c412c")
        b_blok.penup()
        b_blok.speed("fastest")
        return b_blok

    def create_border(self):
        for i in range(-354, 354, 2):
            for up_or_down in range(0, 2):
                brdr_block = self.create_block()
                brdr_block.shape("new_defined_2")
                if up_or_down == 0:
                    brdr_block.goto(i, 306)
                else:
                    brdr_block.goto(i, -306)
            self.border_block.append(brdr_block)
        
        for j in range(-306, 306, 2):
            for up_or_down in range(0, 2):
                brdr_block = self.create_block()
                brdr_block.shape("new_defined_2")
                if up_or_down == 0:
                    brdr_block.goto(354, j)
                else:
                    brdr_block.goto(-354, j)
            self.border_block.append(brdr_block)
# python border.py