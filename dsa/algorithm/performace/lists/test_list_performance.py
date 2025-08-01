# Import the timeit module
# import timeit

# Import the Timer class defined in the module
from timeit import Timer

# Import function that need to test
from concat import concat_list
from append import append_list
from comprehension import comprehension_list
from list_range import list_range

# Test
t1 = Timer("concat_list()", "from __main__ import concat_list")
print("contcat (test 1): ", t1.timeit(number=1000), "milliseconds")

t2 = Timer("append_list()", "from __main__ import append_list")
print("append (test 2): ", t2.timeit(number=1000), "milliseconds")

t3 = Timer("comprehension_list()", "from __main__ import comprehension_list")
print("comprehension (test 3): ", t3.timeit(number=1000), "milliseconds")

t4 = Timer("list_range()", "from __main__ import list_range")
print("list range (test 4): ", t4.timeit(number=1000), "milliseconds")
