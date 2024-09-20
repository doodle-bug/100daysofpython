import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

# adding an image as the background of the turtle screen
# also turte only works with the .gif image extentions
image = "C:\\Users\\aanand2\\OneDrive - Capgemini\\Desktop\\Python\\Codes\\us-states-game\\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv(r"C:\Users\aanand2\OneDrive - Capgemini\Desktop\Python\Codes\us-states-game\50_states.csv")
all_states = data.state.to_list()

guessed_state = []

while len(guessed_state) < 50:
    # make a dialog box to take input
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":

        # states to learn(means states which are not guessed)
        missing_states = []
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pandas.DataFrame (missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    # if answer_state is one of the states in the csv
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

