from stack import Stack2


def devide_by_2(dec_number):
    rem_stack = Stack2()

    while dec_number > 0:
        rem = dec_number % 2
        rem_stack.push(rem)
        # print(rem_stack.size())
        dec_number = dec_number // 2

    bin_string = ""
    while not rem_stack.is_empty():
        bin_string = bin_string + str(rem_stack.pop())

    return bin_string


print(devide_by_2(2))
print(devide_by_2(17))
print(devide_by_2(45))
print(devide_by_2(96))
