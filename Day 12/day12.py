##with open("input.txt") as file:
##    input = file.read()

with open("input0.txt") as file:
    input = file.read().split("\n")
    
##with open("input1.txt") as file:
##    input = file.read()

from math import comb

def condense_map(damage_map, preference, length):
    """
        Takes a list of strings and gets rid of the surplus bonus strings
    """
    if length <= 1 or not damage_map or "#" in damage_map:
        return
    while damage_map and len(damage_map[preference]) < length:
        damage_map.pop(preference)

def condense_string(damage_segment, preference, length):
    """
        Takes a string with only # and ? and tries to figure out how
        to mash in the remaining number of broken tiles by tranforming
        each
    """
    #TODO: lots
    if preference == -1:
        string.reverse()
    if length <= 1 or not damage_segment:
        return
    while damage_map and len(damage_map[preference]) < length:
        damage_map.pop(preference)
    if preference == -1:
        string.reverse()

def what_even_is_nCr(damage_map, redundancy_check):
    

def handle_it(damage_map, redundancy_check):
    """
        Finds the answer row by row
    """
    
    # try to get an idea of which direction we should head in when all else fails:
    preference = 0
    halfway_point = int(len(redundancy_check))
    if sum(redundancy_check[halfway_point:]) > sum(redundancy_check[:halfway_point]):
        preference = -1

    print(f"uncondensed map: {damage_map}")
    
    # get rid of the stragglers at the beginning
    condense_map(damage_map, 0, redundancy_check[0])
    # get rid of the stragglers at the end
    condense_map(damage_map, -1, redundancy_check[-1])

    print(f"condensed map: {damage_map}")

    while damage_map:
        # handle the one big chunk case:
        if len(damage_map) == 1:
            if "#" not in damage_map[0]:
                yield what_even_is_nCr(damage_map[0], redundancy_check)
            damage_map.pop()
            redundancy_check = []
        # find the largest numbered side and pop off useless ones:
        elif redundancy_check[-1] > redundancy_check[0]:
            # the end has the larger number
            damage_map.pop(-1)
            yield 2
        elif redundancy_check[-1] < redundancy_check[0]:
            # the beginning has the larger number
            damage_map.pop()
            yield 2
        else:
            # more than one chunk but equal sizes
            damage_map.pop(preference)
            yield 2
    
        print(f"uncondensed map: {damage_map}")
        
        # get rid of the stragglers at the beginning
        condense_map(damage_map, 0, redundancy_check[0])
        # get rid of the stragglers at the end
        condense_map(damage_map, -1, redundancy_check[-1])
        
        print(f"condensed map: {damage_map}")

for i in input:
    running_total = 1
    i = i.split(" ")
    damage_map = [j for j in i[0].split(".") if not j == ""]
    print(damage_map)
    redundancy_check = [int(j) for j in i[1].split(",")]
    print()
    print(redundancy_check)
    print(len(damage_map) == len(redundancy_check))

    for j in handle_it(damage_map, redundancy_check):
        running_total *= j

    print(running_total)

    
##    largest_possibilities = [j for j in damage_map if len(j) >= max(redundancy_check)]

##    if len(largest_possibilities)
    
