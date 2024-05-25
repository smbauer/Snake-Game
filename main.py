from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


# initialize screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# create snake, food, scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# bind keys
screen.onkeypress(fun=snake.right, key="Right")
screen.onkeypress(fun=snake.up, key="Up")
screen.onkeypress(fun=snake.left, key="Left")
screen.onkeypress(fun=snake.down, key="Down")
screen.onkeypress(fun=screen.bye, key="space")
screen.listen()

# run the game
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with wall
    if snake.wall_collision():
        # game_on = False
        scoreboard.reset_scoreboard()
        snake.reset_snake()

    # detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.move()
        snake.extend()

    # detect collision with tail
    if snake.tail_collision():
        # game_on = False
        scoreboard.reset_scoreboard()
        snake.reset_snake()
        

screen.exitonclick()
