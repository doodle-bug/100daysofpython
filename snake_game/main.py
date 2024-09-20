# importing all the classes from library and the other file source
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# creating a screen and describing its characteristics
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.title("Snake Game")

# tracer(0) is used to turn off the automatic screen updates
screen.tracer(0)

# creaking a snake from the snake class
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# describing the behaviour of the snake on pressing different arrow keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    # refreshes the screen with the new content
    screen.update()
    # delays the execution of next statement by 0.1 sec
    time.sleep(0.1)
    snake.move()

    # Detect collision from food 
    # here the value is taken 15 by hit and trial as the size of segment is 20x20
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    # Creating a boundry and 290 is taken as the size of segment is 20x20
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            

scoreboard.game_over()

screen.exitonclick()

