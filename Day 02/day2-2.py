with open("input.txt") as file:
    input = file.read()

input = input.split("\n")

haha_ha = [[[j.split(" ")[1],int(j.split(" ")[0])] for j in input[i][input[i].find(":")+2:].replace(",",";").split("; ")] for i in range(len(input))]

sum_total = 0

for i in haha_ha:
    max_green = max([a[1] for a in i if a[0] == "green"])
    max_blue = max([a[1] for a in i if a[0] == "blue"])
    max_red = max([a[1] for a in i if a[0] == "red"])
    sum_total += max_green * max_blue * max_red

print(sum_total)
