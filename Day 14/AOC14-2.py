import numpy
import multiprocessing

with open("input.txt") as file:
    input0 = file.read().strip("\n").split("\n")
    
input0 = numpy.array(list(map(list, input0)))

with open("testInput1.txt") as file:
    input1 = file.read().strip("\n").split("\n")
    
input1 = numpy.array(list(map(list, input1)))

with open("testInput2.txt") as file:
    input2 = file.read().strip("\n").split("\n")

input2 = numpy.array(list(map(list, input2)))

def score(column, scores):
    load_score = 0
    return sum(scores[i] for i,O in enumerate(column) if O == "O")

def trillion_cycle(current_state):
    for i in range(1000000000):
        current_state= cycle(current_state)
        if i % 1000 == 0:
            print(i)
            print(current_state)
    return current_state
        

def cycle(current_state):
    current_state = shift(current_state, "north")
    current_state = shift(current_state, "west")
    current_state = shift(current_state, "south")
    current_state = shift(current_state, "east")
    return current_state

def shift(state, direction):
    
    for i in range(len(state)):
        if direction.lower() in ("north", "south"):
            row_or_column = state[:,i]
        else:
            row_or_column = state[i,:]
        shift_one(row_or_column, direction, state)
        
    return state

def shift_one(row_or_column, direction, state):
        segments = "".join(row_or_column).split("#")
        new_row_or_column = []
        if direction.lower() in ("north", "west"):
            for segment in segments:
                new_row_or_column = new_row_or_column.extend([a for a in shift_left(segment)])
        else:
            for segment in segments:
                new_segments.append(shift_right(segment))
        if direction.lower() in ("north", "south"):
            state[:,i] = numpy.array([a for a in "#".join(new_segments)])
        else:
            state[i,:] = numpy.array([a for a in "#".join(new_segments)])
    

def shift_left(segment):
    return segment.count("O")*"O"+segment.count(".")*"."

def shift_right(segment):
    return segment.count(".")*"."+segment.count("O")*"O"

for input_rows in [input1,input0, input2]:
    
    input_rows = trillion_cycle(input_rows)
    print(input_rows)
    load_score = 0
    scores = [i+1 for i in range(len(input_rows[0]))]
    scores.reverse()
    for column in zip(*input_rows):
        load_score += score(column, scores)
    print(load_score)
    print("-")




