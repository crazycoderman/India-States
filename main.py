import pandas
import turtle

screen = turtle.Screen()
screen.title("FIND THE STATES")
screen.setup(600,700)
image = 'india.gif'
screen.addshape('india.gif')

turtle.shape(image)


############## CREATING THE STATES ###############
# states = {
#     'state' : [],
#     'x' : [],
#     'y' : []
# }

# turtle_of_states = turtle.Turtle()

# def move_turtle(x,y):
#     turtle_of_states.setpos(x,y)
#     state = turtle.textinput("What's the name of this state?", "Name: ").title()
#     if state == 'Close':
#         pandas.DataFrame(states).to_csv('states.csv')

#     else:
#         states['state'].append(state)
#         states['x'].append(x)
#         states['y'].append(y)


# screen.onclick(move_turtle)

# turtle.mainloop()

############## FINDING THE STATES ###############

def text(state,x,y):
    new_state = turtle.Turtle()
    new_state.ht()
    new_state.pu()
    new_state.setpos(x,y)
    new_state.write(state, move= False, align='center')

data = pandas.read_csv('states.csv')

state_list = list(data.state)

found_states = []

score = len(found_states)

while score!= 34:

    answer = (turtle.textinput(f" {score}/34 Guess all the states", "What is the another state?")).title()

    if answer == 'Exit':
        break
    
    if answer in state_list:
        state_data = data[data.state == answer]
        (x,y) = int(state_data.x), int(state_data.y)
        text(answer,x,y)
        score += 1
        found_states.append(answer)
        state_list.remove(answer)

result_data = {
    "To be Found" : state_list
}

result_final = pandas.DataFrame(result_data)

result_final.to_csv('Result.csv')
