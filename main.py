import time
from turtle import Screen
from paddles import Paddle  # Importing the Paddle class
from ball import Ball  # Importing the Ball class
from scoreboard import ScoreBoard, CenterLine  # Importing ScoreBoard and CenterLine classes


# Function to set up the screen properties
def modify_screen():
    screen.title("The Ping Pong")  # Setting the title of the window
    screen.bgcolor("black")  # Setting the background color to black
    screen.setup(width=800, height=600)  # Setting the window size to 800x600 pixels
    screen.tracer(0)  # Turning off the automatic screen updates for smoother animations


# Function to listen for key presses and releases
def listen_keys():
    screen.listen()  # Make the screen listen for key events

    # Right paddle controls
    screen.onkeypress(right_paddle.up, "Up")  # Move right paddle up when "Up" key is pressed
    screen.onkeyrelease(right_paddle.stop_up, "Up")  # Stop right paddle when "Up" key is released
    screen.onkeypress(right_paddle.down, "Down")  # Move right paddle down when "Down" key is pressed
    screen.onkeyrelease(right_paddle.stop_down, "Down")  # Stop right paddle when "Down" key is released

    # Left paddle controls
    screen.onkeypress(left_paddle.up, "w")  # Move left paddle up when "w" key is pressed
    screen.onkeyrelease(left_paddle.stop_up, "w")  # Stop left paddle when "w" key is released
    screen.onkeypress(left_paddle.down, "s")  # Move left paddle down when "s" key is pressed
    screen.onkeyrelease(left_paddle.stop_down, "s")  # Stop left paddle when "s" key is released


# Main setup
screen = Screen()  # Create a screen object
modify_screen()  # Call function to modify screen properties

# Create game objects
right_paddle = Paddle(350, 0)  # Right paddle at (350, 0)
left_paddle = Paddle(-350, 0)  # Left paddle at (-350, 0)
ball = Ball()  # Create the ball
scoreboard = ScoreBoard()  # Create the scoreboard
center_line = CenterLine()  # Draw the center line

listen_keys()  # Set up key listeners

# Main game loop
is_game_on = True  # Set game loop condition
while is_game_on:
    screen.update()  # Refresh the screen on each loop iteration
    ball.start_move()  # Move the ball
    time.sleep(0.1)  # Add a small delay to control the ball's speed

    # Check for paddle collisions
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320  # Ball near right paddle
            or ball.distance(left_paddle) < 50 and ball.xcor() < -320):  # Ball near left paddle
        ball.move_speed *= 0.9  # Increase ball speed slightly after each hit
        ball.bounce_x()  # Reverse ball's horizontal direction

    # Check if the ball goes out of bounds on the right
    if ball.xcor() > 375:
        scoreboard.increase_left_score()  # Increment left player's score
        ball.reverse_motion()  # Reset ball position and direction

    # Check if the ball goes out of bounds on the left
    if ball.xcor() < -375:
        scoreboard.increase_right_score()  # Increment right player's score
        ball.reverse_motion()  # Reset ball position and direction

    # Check for win condition for left player
    if scoreboard.left_score == 10:
        scoreboard.winner = "Player 1"  # Set winner to Player 1
        scoreboard.display_winner()  # Display the winner
        is_game_on = False  # End the game

    # Check for win condition for right player
    if scoreboard.right_score == 10:
        scoreboard.winner = "Player 2"  # Set winner to Player 2
        scoreboard.display_winner()  # Display the winner
        is_game_on = False  # End the game

screen.exitonclick()  # Keep the screen open until clicked