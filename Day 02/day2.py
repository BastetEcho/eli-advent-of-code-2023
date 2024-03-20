input = input.split("\n")

lookup_dict = dict()
lookup_dict["red"] = 12
lookup_dict["green"] = 13
lookup_dict["blue"] = 14

sum([int(sum([lookup_dict[j.split(" ")[1]] < int(j.split(" ")[0]) for j in input[i][input[i].find(":")+2:].replace(",",";").split("; ")])== 0)*(i+1) for i in range(len(input))])
