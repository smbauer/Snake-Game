from turtle import Turtle


START_SEGMENTS = 3
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

        
    def create_snake(self) -> None:
        """create the starting segments of the snake"""
        start_x = 0
        for _ in range(START_SEGMENTS):
            start_x -= 20
            position = (start_x, 0)
            self.add_segment(position)


    def reset_snake(self) -> None:
        """reset the snake to the starting position"""
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    def add_segment(self, position):
        """creates a new segment and adds it to the snake"""
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)


    def extend(self):
        """add a new segment at the tail end of the snake"""
        position = self.segments[-1].pos()
        self.add_segment(position)


    def move(self) -> None:
        """
        move each of the tail segments to the position of the previous segment in the snake
        and move the head in the specified direction
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num - 1].pos())
        self.head.forward(20)


    def right(self) -> None:
        """move the snake to the right (face east)"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def up(self) -> None:
        """move the snake up (face north)"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def left(self) -> None:
        """move the snake to the left (face west)"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def down(self) -> None:
        """move the snake down (face south)"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def wall_collision(self) -> bool:
        """return True if the head reaches the screen boundary"""
        return abs(self.head.xcor()) >= 290 or abs(self.head.ycor()) >= 290
    

    def tail_collision(self) -> bool:
        """return True if the head overlaps any part of the body"""
        for segment in self.segments[1:]:
            if self.head.pos() == segment.pos():
                return True
        return False
