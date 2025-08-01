import timeit
import random

for i in range(10000, 1000001, 20000):
    t = timeit.Timer("random.randrange(%d) in x" % i, "from __main__ import random, x")
    x = {j: None for j in range(i)}
    dictionary_time = t.timeit(number=10000)

    print("%d, %10.3f" % (i, dictionary_time))
