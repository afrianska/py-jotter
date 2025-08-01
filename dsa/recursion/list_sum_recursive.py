def list_sum_recursion(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum_recursion(num_list[1:])


print(list_sum_recursion([1, 3, 5, 7, 9]))
#  (1 +(3+(5+(7+9))))
