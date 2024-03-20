
with open("input.txt") as file:
    input0 = file.read().strip("\n").split(",")


input1 = ["rn=1","cm-","qp=3","cm=2","qp-","pc=4","ot=9","ab=5","pc-","pc=6","ot=7"]


def hash_algo(text):
    current_value = 0
    for character in text:
        current_value += ord(character)
        current_value = current_value*17%256

    return current_value


# set up the lenses
boxes = dict((n,dict()) for n in range(256))

for instruct in input0:
    if "=" in instruct:
        label = instruct[:instruct.find("=")]
        focal = instruct[instruct.find("=")+1:]
        boxes[hash_algo(label)][label] = int(focal)
    else:
        label = instruct[:-1]
        try:
            del boxes[hash_algo(label)][label]
        except:
            pass

# calculate focusing power:
score = 0
for i in range(256):
    lenses = list(boxes[i].values())
    for j in range(len(lenses)):
        score += (i+1)*(j+1)*lenses[j]

print(score)
