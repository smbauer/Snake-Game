from turtle import Turtle


SCOREBOARD_LOCATION = (0, 270)
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(SCOREBOARD_LOCATION)
        self.score = 0
        self.refresh_scoreboard()


    def refresh_scoreboard(self) -> None:
        """update the scoreboard with the current score at the top of the screen"""
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    
    def game_over(self) -> None:
        """write the game over message in the middle of the screen"""
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)


    def increase_score(self) -> None:
        """increment the current score"""
        self.score += 1
        self.refresh_scoreboard()
        