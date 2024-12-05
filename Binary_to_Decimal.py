accept = ["0", "1"]
binary_list = []
binary_length = 0
number = 0
binary_number = ""

def b_to_d():
    global binary_length
    global number
    global binary_number
    while binary_length != 8:
            binary_length = 0
            binary_number = (input("Please enter a binary number, eight bits in length >>> "))
            for i in binary_number:
                binary_length += 1

    while (all(bit in accept for bit in binary_number)) == False:
            binary_length = 0
            binary_number = (input("Please enter a binary number, eight bits in length >>> "))
            for i in binary_number:
                binary_length += 1

        # if all(bit in accept for bit in binary_number) == True:
    for i in binary_number:
                binary_list.append(i)
    if binary_list[0] == "1":
                number += 128

    if binary_list[1] == "1":
                number += 64

    if binary_list[2] == "1":
                number += 32

    if binary_list[3] == "1":
                number += 16

    if binary_list[4] == "1":
                number += 8

    if binary_list[5] == "1":
                number += 4

    if binary_list[6] == "1":
                number += 2

    if binary_list[7] == "1":
                number += 1

    print(binary_number, "converted to decimal is >>> ",number)

b_to_d()