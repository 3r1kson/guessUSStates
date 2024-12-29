from turtle import Turtle

import pandas

# IN THE COURSE THE STATES_LIST IS CONVERTED TO LIST BEFORE STARTING TO USE THE DATA
STATES_LIST = pandas.read_csv("./csv/50_states.csv")

class Questions(Turtle):
    def __init__(self):
        super().__init__()
        self.answer = ""
        self.correct_answers = 0
        self.bag_of_answers = []
        self.total = len(STATES_LIST)
        self.exit = False

    def check_answer(self, answer):
        lower_states = STATES_LIST['state'].str.lower()
        answer_lower = answer.lower()

        if answer_lower in lower_states.values and answer_lower not in self.bag_of_answers:
            self.bag_of_answers.append(answer_lower)

            state_index = lower_states[lower_states == answer_lower].index[0]
            x = STATES_LIST.loc[state_index, "x"]
            y = STATES_LIST.loc[state_index, "y"]
            self.set_state_on_screen(STATES_LIST.loc[state_index, "state"], x, y)

        if answer_lower == "exit":
            self.generate_not_used_states()

    def set_state_on_screen(self, answer, x, y):
        self.correct_answers += 1
        self.penup()
        self.hideturtle()
        self.goto(x=x, y=y)
        self.write(answer, align="center")

    def generate_not_used_states(self):
        states = STATES_LIST.state.to_list()
        not_used_states = [state for state in states if state.lower() not in self.bag_of_answers]
        not_used_states_df = pandas.DataFrame(not_used_states, columns=["state"])
        not_used_states_df.to_csv("states_to_learn.csv", index=False)
        self.exit = True
