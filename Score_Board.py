from turtle import Turtle

X = 0
Y = 270

class Scoreboard:
    def __init__(self, Height):
        self.score = 0
        self.local_turtle = self.set_up(Height)

#setup Scoreboard
    def set_up(self, Height):
        local_turtle = Turtle()
        local_turtle.penup()
        local_turtle.color("white")
        local_turtle.hideturtle()
        local_turtle.setpos(0, Height/2 - 40)
        return local_turtle

    def update_Scoreboar(self):
        self.local_turtle.clear()
        scoretring = "Score %s" % self.score
        self.local_turtle.write(scoretring, False, align="center", font = ("Arial", 14, "normal"))

    def increase_score(self):
        self.score += 1
