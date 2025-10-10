from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_coordinate, y_coordinate):
        super().__init__()  # Initialize the Turtle class
        self.penup()  # Prevent the paddle from drawing when it moves
        self.shape("square")  # Set the shape of the paddle to a square
        self.color("white")  # Set the color of the paddle to white
        self.speed("fastest")  # Set the animation speed of the paddle
        self.shapesize(stretch_wid=5, stretch_len=1)  # Stretch the paddle to make it a rectangle
        self.goto(x_coordinate, y_coordinate)  # Position the paddle at the specified coordinates
        self.moving_up = False  # Initialize flag to track upward movement
        self.moving_down = False  # Initialize flag to track downward movement

    # Method to handle upward movement
    def up(self):
        self.moving_up = True  # Set the upward movement flag to True
        self.move()  # Start moving the paddle

    # Method to handle downward movement
    def down(self):
        self.moving_down = True  # Set the downward movement flag to True
        self.move()  # Start moving the paddle

    # Method to stop upward movement
    def stop_up(self):
        self.moving_up = False  # Set the upward movement flag to False

    # Method to stop downward movement
    def stop_down(self):
        self.moving_down = False  # Set the downward movement flag to False

    # Method to move the paddle continuously
    def move(self):
        if self.moving_up:  # If the paddle is moving up
            self.sety(self.ycor() + 20)  # Move the paddle up by 20 units
        if self.moving_down:  # If the paddle is moving down
            self.sety(self.ycor() - 20)  # Move the paddle down by 20 units