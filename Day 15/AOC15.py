
with open("input.txt") as file:
    input0 = file.read().strip("\n").split(",")


input1 = ["rn=1","cm-","qp=3","cm=2","qp-","pc=4","ot=9","ab=5","pc-","pc=6","ot=7"]


def hash_algo(text):
    current_value = 0
    for character in text:
        current_value += ord(character)
        current_value = current_value*17%256

    return current_value


print(sum(hash_algo(i) for i in input0))
