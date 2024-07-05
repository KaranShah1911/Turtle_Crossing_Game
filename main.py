import time
from turtle import Screen
from player import Player
from car import Cars
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car = Cars()
scoreboard = Scoreboard()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move()

    # Collision with Car
    for car in car.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Successful Crossing
    if player.finish():
        player.go_to_start()
        car.next_level()
        scoreboard.new_level()

screen.exitonclick()


