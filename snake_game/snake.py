from turtle import Turtle

# creating constants which remains same throughout the working of the program
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# creating class snake
class Snake:

    # init is used to intialize the instance of the class
    # self represents the instance of the class
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # creating differnet methods for different behaviour of the snake
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("White")
        new_segment.penup()
        new_segment.setposition(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    # extending the snake from the last by adding a segment
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        """ the snake is moving segment wise from back to front...like the 3rd segment
            is taking the postion of the 2nd, the 2nd is taking the position of the 
            1st and then 1st segment is moving forward """
        # range(start = len(segments)-1, stop = 0, step = -1)

        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



    