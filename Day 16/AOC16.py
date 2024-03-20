import numpy
import multiprocessing

with open("input.txt") as file:
    input0 = file.read().strip("\n").split("\n")
    
input0 = numpy.array(list(map(list, input0)), dtype=str)

with open("testInput1.txt") as file:
    input1 = file.read().strip("\n").split("\n")
    
input1 = numpy.array(list(map(list, input1)), dtype=str)

##
##with open("testInput2.txt") as file:
##    input2 = file.read().strip("\n").split("\n")
##
##input2 = numpy.array(list(map(list, input2)))

def get_equivalent_directions(direction):
    if direction in "<>":
        return "<>2"
    elif direction in "^v":
        return "^v2"
    return direction

def change_direction(original, direction):
    if (original == "2") or ((original in "<>") and (direction in "^v")) or ((original in "^v") and (direction in "<>")):
        return "2"
    return direction

for input in [input1, input0]:
    # get the length of the rows
    max_row = len(input)
    # get the length of the columns
    max_column = len(input[0,:])
    # make an array filled with zeros that's the same size
    activated = numpy.zeros((max_row, max_column), dtype = int)
    # use it to count the activated cells as they are activated

    # let's just start coding.
    
    starting_positions = [[0,0,">"]]

    while starting_positions:
        (row_i, column_j, direction) = starting_positions.pop()
        # check what the next square has in it
        try:
            if row_i < 0 or column_j < 0:
                continue
            if input[row_i, column_j] in "-|/\\":
                (next_row_i, next_column_j) = (row_i, column_j)
            elif direction == ">":
                if input[row_i, column_j] in "<>2":
                    continue
                (next_row_i, next_column_j) = (row_i, column_j+1)
            elif direction == "v":
                if input[row_i, column_j] in "^v2":
                    continue
                (next_row_i, next_column_j) = (row_i+1, column_j)
            elif direction == "^":
                if input[row_i, column_j] in "^v2":
                    continue
                (next_row_i, next_column_j) = (row_i-1, column_j)
            elif direction == "<":
                if input[row_i, column_j] in "<>2":
                    continue
                (next_row_i, next_column_j) = (row_i, column_j-1)
                
            if not input[row_i, column_j] in "-|/\\":
                input[row_i, column_j] = change_direction(input[row_i, column_j], direction)
            activated[row_i, column_j] = 1
                
            while input[next_row_i, next_column_j] in "-|/\\":
                activated[next_row_i, next_column_j] = 1
                if input[next_row_i, next_column_j] == "-":
                    if direction == ">":
                        (next_row_i, next_column_j) = (next_row_i, next_column_j+1)
                    elif direction == "<":
                        (next_row_i, next_column_j) = (next_row_i, next_column_j-1)
                    elif direction == "v":
                        starting_positions.append([next_row_i, next_column_j-1, "<"])
                        (next_row_i, next_column_j, direction) = (next_row_i, next_column_j+1, ">")
                    elif direction == "^":
                        starting_positions.append([next_row_i, next_column_j-1, "<"])
                        (next_row_i, next_column_j, direction) = (next_row_i, next_column_j+1, ">")
                        
                elif input[next_row_i, next_column_j] == "|":
                    if direction == ">":
                        starting_positions.append([next_row_i-1, next_column_j, "^"])
                        (next_row_i, next_column_j, direction) = (next_row_i+1, next_column_j, "v")
                    elif direction == "<":
                        starting_positions.append([next_row_i-1, next_column_j, "^"])
                        (next_row_i, next_column_j, direction) = (next_row_i+1, next_column_j, "v")
                    elif direction == "v":
                        (next_row_i, next_column_j) = (next_row_i+1, next_column_j)
                    elif direction == "^":
                        (next_row_i, next_column_j) = (next_row_i-1, next_column_j)
                        
                elif input[next_row_i, next_column_j] == "/":
                    if direction == ">":
                        (next_row_i, next_column_j, direction) = (next_row_i-1, next_column_j, "^")
                    elif direction == "<":
                        (next_row_i, next_column_j, direction) = (next_row_i+1, next_column_j, "v")
                    elif direction == "v":
                        (next_row_i, next_column_j, direction) = (next_row_i, next_column_j-1, "<")
                    elif direction == "^":
                        (next_row_i, next_column_j, direction) = (next_row_i, next_column_j+1, ">")
                        
                elif input[next_row_i, next_column_j] == "\\":
                    if direction == ">":
                        (next_row_i, next_column_j, direction) = (next_row_i+1, next_column_j, "v")
                    elif direction == "<":
                        (next_row_i, next_column_j, direction) = (next_row_i-1, next_column_j, "^")
                    elif direction == "v":
                        (next_row_i, next_column_j, direction) = (next_row_i, next_column_j+1, ">")
                    elif direction == "^":
                        (next_row_i, next_column_j, direction) = (next_row_i, next_column_j-1, "<")

            if next_row_i < 0 or next_column_j < 0:
                continue
            elif input[next_row_i, next_column_j] in get_equivalent_directions(direction):
                continue
            else:
                starting_positions.append([next_row_i, next_column_j, direction])
        except LookupError:
            pass
    print(input)
    print(activated)
    print(numpy.sum(activated))
    
    
