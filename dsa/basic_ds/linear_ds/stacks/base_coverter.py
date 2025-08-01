from stack import Stack2


def base_converter(dec_number, base):
    digits = "0123456789ABCDEF"

    rem_stack = Stack2()

    while dec_number > 0:
        rem = dec_number % base
        print(f"{dec_number} % {base} -> sisa {rem}")
        rem_stack.push(rem)
        # rem_stack.show()
        prev_dec_number = dec_number
        dec_number = dec_number // base
        print(f"{prev_dec_number} // {base} = {dec_number}")

    new_string = ""
    while not rem_stack.is_empty():
        # rem_stack.show()
        new_string = new_string + digits[rem_stack.pop()]

    return new_string


# print(base_converter(25, 2))
# print(base_converter(25, 16))
# print(base_converter(25, 8))
# print(base_converter(256, 16))
# print(base_converter(26, 26))
print(base_converter(64, 10))
