import time
import turtle
import turtle_crossing_player
import turtle_crossing_car_manager
import turtle_crossing_scoreboard


screen = turtle.Screen()
screen.setup(width=700, height=700)
screen.tracer(0)

plaYer = turtle_crossing_player.Player()
car_manage = turtle_crossing_car_manager.CarManager()
score = turtle_crossing_scoreboard.Scoreboard()

screen.listen()

screen.onkeypress(plaYer.move_forwrd, "Up")
screen.onkeypress(plaYer.move_back, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    # create and move cars
    car_manage.create_car()
    car_manage.move_cars()
    
    screen.update()

    # Deteet collision with car and turtle
    for cAr in car_manage.all_cars:
        if plaYer.distance(cAr) < 20:
            game_is_on = False
            score.game_over()


    # Detect successfull reach at finish line
    if plaYer.is_at_finish_line():
        plaYer.go_to_start_position()
        car_manage.level_up()
        score.increase_score()

screen.exitonclick()

# python turtle_crossing_main.py