from numpy import loadtxt

def score(column):
    load_score = 0
    scores = [i for i in range(len(column))]
    scores.reverse()

    # find the first square rock
    while "#" in column:
        square_index = column.find("#")
        load_count = column[:square_index].count("O")
        load_score += sum(scores[:load_count])
        column = column[square_index+1:]
        scores = scores[square_index+1:]

    
    return load_score

with open("input.txt") as file:
    input0 = file.read().strip("\n").split("\n")

with open("testInput1.txt") as file:
    input1 = file.read().strip("\n").split("\n")

with open("testInput2.txt") as file:
    input2 = file.read().strip("\n").split("\n")

for input_rows in [input1, input2, input0]:
    load_score = 0
    for column in zip(*input_rows):
        load_score += score("".join(list(column))+"#")
    print(load_score)
    print("-")




