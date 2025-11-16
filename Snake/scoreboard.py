from turtle import Turtle
FONT = ("Arial", 20, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x = 0, y = 270)
        self.pendown()
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)
        self.update_score()

    def get_high_score(self):
        with open("highscore.txt", "r") as file:
            score_string = file.read().strip()
            if score_string:  # If the file is not empty
                score = int(score_string)
            else:
                score = 0
        return score

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.high_score}", align = ALIGNMENT, font = FONT)

    def increment(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

        self.score = 0
        self.update_score()


    # def game_over(self):
    #
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align = ALIGNMENT, font = FONT)