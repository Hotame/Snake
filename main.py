import time
from snake import Snake
from turtle import Screen
from score_board import ScoreBoard
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

is_game = True

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while is_game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Collision With Food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    # Detect Collision With Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over()
        is_game = False

    # Detect Collision With Tail -> If Head Collides With Any Segment In The Tail, Trigger game_over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over()
            is_game = False


screen.exitonclick()
