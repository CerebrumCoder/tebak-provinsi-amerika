import turtle
import pandas
from state_placing import StatePlacing
# Turtle only works with gif images

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
total_states = len(data.state)
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{total_states}", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # Dokumentasi kode kemarin
    # for state in data.state:
    #     if state not in guessed_states:
    #         missing_states.append(state)
    #
    # data_dict = {
    #     "Not Guessed States": not_guessed_states,
    # }

    if answer_state in all_states:
        guessed_states.append(answer_state)
        print("benar")
        state_data = data[data.state == answer_state]
        state_pos_x = state_data['x'].values[0]
        state_pos_y = state_data['y'].values[0]

        StatePlacing(user_answer=answer_state, pos_x=state_pos_x, pos_y=state_pos_y)

            # Get a particular value from that row
            # StatePlacing(user_answer=state_data.state.item(), pos_x=state_pos_x, pos_y=state_pos_y)


# states_to_learn.csv

# print(guessed_states)

