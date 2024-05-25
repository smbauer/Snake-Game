from turtle import Turtle
import time


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
        self.high_score = self.get_high_score()
        self.refresh_scoreboard()


    def refresh_scoreboard(self) -> None:
        """update the scoreboard with the current score at the top of the screen"""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    
    def reset_scoreboard(self) -> None:
        """
        write game over message in middle of the screen.
        update the high score if necessary and reset the score and scoreboard.
        """
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score()
        self.score = 0
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        time.sleep(2)
        self.goto(SCOREBOARD_LOCATION)
        self.refresh_scoreboard()

    
    def increase_score(self) -> None:
        """increment the current score"""
        self.score += 1
        self.refresh_scoreboard()


    def get_high_score(self) -> int:
        with open("high_score.txt") as f:
            high_score = int(f.read())
        return high_score
    

    def update_high_score(self) -> None:
        with open("high_score.txt", mode="w") as f:
            f.write(str(self.high_score))
        