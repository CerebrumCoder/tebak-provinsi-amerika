from turtle import Turtle

TEXT_FONT = ("Arial", 12, "normal")

class StatePlacing(Turtle):
    def __init__(self, user_answer, pos_x, pos_y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=pos_x, y=pos_y)
        self.write(f"{user_answer}", font=TEXT_FONT)
