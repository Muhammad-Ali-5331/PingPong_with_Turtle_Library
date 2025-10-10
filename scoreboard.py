from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the Turtle class
        self.color("white")  # Set the color of the scoreboard text to white
        self.hideturtle()  # Hide the turtle cursor since we only need to display text
        self.penup()  # Lift the pen to prevent drawing when moving
        self.left_score = 0  # Initialize the score for the left player
        self.right_score = 0  # Initialize the score for the right player
        self.winner = ""  # Variable to store the winner's name
        self.display_score()  # Display the initial score

    # Method to display the current score on the screen
    def display_score(self):
        self.clear()  # Clear the previous score display
        self.goto(-120, 200)  # Move to the position to display the left score
        self.write(self.left_score, align="center", font=("Arial", 80, "normal"))  # Display left player's score
        self.goto(120, 200)  # Move to the position to display the right score
        self.write(self.right_score, align="center", font=("Arial", 80, "normal"))  # Display right player's score

    # Method to increase the left player's score
    def increase_left_score(self):
        self.left_score += 1  # Increment the left player's score
        self.display_score()  # Update the score display

    # Method to increase the right player's score
    def increase_right_score(self):
        self.right_score += 1  # Increment the right player's score
        self.display_score()  # Update the score display

    # Method to display the winner on the screen
    def display_winner(self):
        self.home()  # Move to the center of the screen
        self.color("orange")  # Set the text color to orange for the winner announcement
        self.write(f"{self.winner} Won the Game!", align="center", font=("Arial", 20, "normal"))  # Display the winner

class CenterLine(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the Turtle class
        self.color("white")  # Set the color of the center line to white
        self.hideturtle()  # Hide the turtle cursor
        self.penup()  # Lift the pen to prevent drawing when moving
        self.goto(0, 290)  # Move to the top-center position
        self.setheading(270)  # Set the direction of the turtle to downwards (270 degrees)
        self.pensize(4)  # Set the pen size to make the line thicker
        self.draw_center_line()  # Draw the dashed center line

    # Method to draw the dashed center line on the screen
    def draw_center_line(self):
        for _ in range(30):  # Draw 30 segments of the dashed line
            self.pendown()  # Put the pen down to draw
            self.forward(10)  # Draw a short line segment
            self.penup()  # Lift the pen to skip a space
            self.forward(10)  # Move forward to create the gap in the dashed line