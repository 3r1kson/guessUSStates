import turtle
from turtle import Screen

from classes.questions import Questions

screen = Screen()
questions = Questions()
screen.title("U.S. States Game")
screen.setup(width=730, height=490)

image = "images/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

while not questions.total == questions.correct_answers:
    questions.check_answer(screen.textinput(f"States Correct {questions.correct_answers}/{questions.total}", "What's another state name?"))

    if questions.exit == True:
        break

# screen.exitonclick()