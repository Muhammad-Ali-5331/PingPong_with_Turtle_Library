from turtle import Turtle

PaddleSegments = 5

class Paddle(Turtle):
    def __init__(self,x_coordinate):
        super().__init__()
        self.X_coordinate = x_coordinate
        self.created_paddle_segments = []
        self.create_paddle()
        self.first_segment = self.created_paddle_segments[0]


    def make_paddle_segments(self):
        for paddle_segment in range(PaddleSegments):
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.speed("fastest")
            new_segment.penup()
            self.created_paddle_segments.append(new_segment)


    def position_paddle(self):
        for seg in range(len(self.created_paddle_segments)):
            self.created_paddle_segments[seg].teleport(self.X_coordinate, seg * 20)


    def create_paddle(self):
        self.make_paddle_segments()
        self.position_paddle()


    def up(self):
        for segments in self.created_paddle_segments:
            if self.first_segment.ycor() < 280 or self.first_segment.ycor() > -280:
                segments.sety(segments.ycor() + 50)


    def down(self):
        for segments in self.created_paddle_segments:
            if self.first_segment.ycor() < 280 or self.first_segment.ycor() > -280:
                segments.sety(segments.ycor() - 50)


