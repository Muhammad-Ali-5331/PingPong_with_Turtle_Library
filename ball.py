from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the Turtle class
        self.penup()  # Prevent the ball from drawing when it moves
        self.shape("circle")  # Set the shape of the ball to a circle
        self.color("blue")  # Set the color of the ball to white
        self.goto(0, 0)  # Start the ball at the center of the screen
        self.x_move = 5  # Set the initial movement speed in the x-direction
        self.y_move = 5  # Set the initial movement speed in the y-direction
        self.move_speed = 3  # Set the initial delay between movements (controls speed)

    # Method to start the ball's movement
    def start_move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)  # Move the ball by the x_move and y_move values

        # Detect collision with the top or bottom walls and bounce the ball
        if self.ycor() > 280 or self.ycor() < -280:  # If the ball hits the top or bottom edge of the screen
            self.bounce_y()  # Reverse the ball's y-direction to create a bouncing effect

    # Method to reverse the ball's direction along the y-axis (vertical bounce)
    def bounce_y(self):
        self.y_move *= -1  # Multiply y_move by -1 to reverse its direction

    # Method to reverse the ball's direction along the x-axis (horizontal bounce)
    def bounce_x(self):
        self.x_move *= -1  # Multiply x_move by -1 to reverse its direction

    # Method to reset the ball's position to the center and reverse its motion
    def reverse_motion(self):
        self.goto(0, 0)  # Reset the ball's position to the center of the screen
        self.move_speed = 0.1  # Reset the movement speed to its initial value
        self.bounce_x()  # Reverse the ball's x-direction to send it towards the other player