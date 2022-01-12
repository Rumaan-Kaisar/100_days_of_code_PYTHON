import time
import turtle
import turtle_crossing_player
import turtle_crossing_car_manager
import turtle_crossing_scoreboard


sc_reen = turtle.Screen()
sc_reen.bgcolor("#ff00ff")
sc_reen.setup(width=1200, height=700)
sc_reen.tracer(0)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    sc_reen.update()


# python rough.py